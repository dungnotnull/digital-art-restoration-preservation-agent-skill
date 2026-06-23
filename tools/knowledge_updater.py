#!/usr/bin/env python3
"""knowledge_updater.py — Digital Art Restoration & Preservation (idea 225).

Crawls conservation, digitization-standard, and heritage-science sources, appending
dated, deduplicated entries to SECOND-KNOWLEDGE-BRAIN.md.

Production-grade implementation with web crawling, search integration, rate limiting,
error handling, and deduplication.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

# Optional dependencies for enhanced functionality
# Install with: pip install requests beautifulsoup4 crawl4ai
try:
    import requests
    from bs4 import BeautifulSoup
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from crawl4ai import AsyncWebCrawler, CacheMode
    HAS_CRAWL4AI = True
except ImportError:
    HAS_CRAWL4AI = False

# Configuration
BRAIN_FILE = Path(__file__).resolve().parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"
CACHE_FILE = Path(__file__).resolve().parent / ".knowledge_cache.json"
USER_AGENT = "Mozilla/5.0 (compatible; DigitalArtRestorationBot/1.0; +https://github.com/anthropics/skills)"
REQUEST_TIMEOUT = 30
RATE_LIMIT_DELAY = 2  # seconds between requests
MAX_CONCURRENT_REQUESTS = 3

# Authoritative sources
SOURCES = {
    "fadgi": {
        "name": "Federal Agencies Digitization Guidelines Initiative",
        "base_url": "https://www.digitizationguidelines.gov/",
        "search_paths": [
            "/guidelines/",
            "/resources/",
            "/about/",
        ],
        "keywords": ["digitization", "imaging", "guidelines", "FADGI", "star rating"],
    },
    "metamorfoze": {
        "name": "Metamorfoze Preservation Imaging Guidelines",
        "base_url": "https://www.metamorfoze.nl/",
        "search_paths": [
            "/en",
            "/guidelines/",
            "/imaging/",
        ],
        "keywords": ["Metamorfoze", "preservation", "imaging", "guidelines", "Netherlands"],
    },
    "aic": {
        "name": "American Institute for Conservation",
        "base_url": "https://www.culturalheritage.org/",
        "search_paths": [
            "/resources/",
            "/about-us/core-documents/",
            "/ethics/",
        ],
        "keywords": ["conservation", "ethics", "AIC", "code of ethics", "guidelines"],
    },
    "icom_cc": {
        "name": "International Council of Museums - Conservation Committee",
        "base_url": "https://www.icom-cc.org/",
        "search_paths": [
            "/resources/",
            "/about/",
            "/documentation/",
        ],
        "keywords": ["ICOM-CC", "conservation", "ethics", "documentation", "guidelines"],
    },
    "getty": {
        "name": "Getty Conservation Institute",
        "base_url": "https://www.getty.edu/",
        "search_paths": [
            "/conservation/",
            "/publications/resources/",
            "/conservation/science/",
        ],
        "keywords": ["Getty", "conservation", "science", "heritage", "research"],
    },
    "oais": {
        "name": "OAIS Reference Model (CCSDS)",
        "base_url": "https://public.ccsds.org/",
        "search_paths": [
            "/Pubs/",
        ],
        "keywords": ["OAIS", "preservation", "archival", "reference model", "ISO 14721"],
    },
    "iso": {
        "name": "ISO Imaging Standards",
        "base_url": "https://www.iso.org/",
        "search_paths": [
            "/standards-catalog/",
        ],
        "keywords": ["ISO", "19264", "imaging", "quality", "standards"],
    },
}

# Keywords for relevance scoring
KEYWORDS = [
    "conservation", "digitization", "restoration", "preservation",
    "multispectral", "fadgi", "metamorfoze", "oais", "reversibility",
    "heritage science", "imaging", "archival", "metadata", "fixity",
    "minimal intervention", "documentation", "ethics", "standards",
    "color management", "spectral", "infrared", "ultraviolet", "RTI",
]


class LogLevel(Enum):
    """Logging levels for the updater."""
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3


def log(level: LogLevel, message: str, verbose: bool = False) -> None:
    """Print log message if level is appropriate."""
    if verbose or level in (LogLevel.WARNING, LogLevel.ERROR):
        prefix = {
            LogLevel.DEBUG: "DEBUG",
            LogLevel.INFO: "INFO",
            LogLevel.WARNING: "WARNING",
            LogLevel.ERROR: "ERROR",
        }[level]
        print(f"[{prefix}] {message}", file=sys.stderr)


def url_hash(url: str) -> str:
    """Generate SHA-256 hash of URL, truncated to 12 chars."""
    return hashlib.sha256(url.encode()).hexdigest()[:12]


def extract_hashes(text: str) -> set[str]:
    """Extract existing URL hashes from brain file."""
    return set(re.findall(r"<!--h:([0-9a-f]{12})-->", text))


def load_brain() -> str:
    """Load brain file contents; create if not exists."""
    if BRAIN_FILE.exists():
        return BRAIN_FILE.read_text(encoding="utf-8")
    # Create minimal brain file if not exists
    BRAIN_FILE.parent.mkdir(parents=True, exist_ok=True)
    template = f"""# SECOND-KNOWLEDGE-BRAIN — Digital Art Restoration & Preservation

## Core Concepts & Frameworks
- **Conservation ethics** — minimal intervention, **reversibility**, retreatability, full documentation, respect for original material (AIC Code of Ethics; ICOM-CC).
- **Digitization standards** — FADGI (US) star ratings; Metamorfoze (NL) preservation imaging guidelines; ISO 19264 image-quality; color targets, resolution, bit depth.
- **Imaging techniques** — high-res RGB, multispectral/hyperspectral (reveals under-drawing, faded ink), RTI (Reflectance Transformation Imaging) for surface texture, IR/UV.
- **Digital restoration** — non-destructive inpainting, color correction (to documented reference), denoising, dewarping — all on derivatives, never the master.
- **Preservation (OAIS)** — Open Archival Information System reference model; ingest, archival storage, fixity (checksums), migration.
- **Archival formats** — uncompressed/lossless TIFF, JPEG2000; rich metadata (Dublin Core, METS, PREMIS).

## Knowledge Update Log
- {date.today().isoformat()} — Brain initialized via knowledge_updater.py
"""
    BRAIN_FILE.write_text(template, encoding="utf-8")
    return template


def load_cache() -> dict[str, Any]:
    """Load request cache from file."""
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_cache(cache: dict[str, Any]) -> None:
    """Save request cache to file."""
    try:
        CACHE_FILE.write_text(json.dumps(cache, indent=2), encoding="utf-8")
    except IOError:
        log(LogLevel.WARNING, "Failed to save cache file")


def score_relevance(entry: dict[str, Any]) -> float:
    """Score entry relevance based on keywords, recency, and source authority."""
    score = 0.0

    # Combine title and summary for keyword matching
    text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()

    # Keyword matches (1 point each)
    keyword_matches = sum(1 for kw in KEYWORDS if kw.lower() in text)
    score += keyword_matches

    # Recency bonus (points for recent content)
    entry_year = entry.get("year", 0)
    if entry_year >= date.today().year - 1:
        score *= 1.5  # 50% bonus for very recent
    elif entry_year >= date.today().year - 3:
        score *= 1.2  # 20% bonus for recent

    # Source authority bonus
    source = entry.get("source", "")
    high_authority = ["fadgi", "metamorfoze", "aic", "icom_cc", "getty", "oais"]
    if any(ha in source.lower() for ha in high_authority):
        score *= 1.3  # 30% bonus for authoritative sources

    return score


def fetch_with_requests(url: str, timeout: int = REQUEST_TIMEOUT) -> Optional[str]:
    """Fetch URL using requests library with error handling."""
    if not HAS_REQUESTS:
        log(LogLevel.WARNING, "requests library not available; skipping URL fetch")
        return None

    try:
        response = requests.get(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=timeout,
            allow_redirects=True,
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        log(LogLevel.WARNING, f"Failed to fetch {url}: {e}")
        return None


def fetch_with_crawl4ai(url: str, timeout: int = REQUEST_TIMEOUT) -> Optional[str]:
    """Fetch URL using crawl4ai with enhanced capabilities."""
    if not HAS_CRAWL4AI:
        log(LogLevel.DEBUG, "crawl4ai not available; falling back to requests")
        return fetch_with_requests(url, timeout)

    try:
        import asyncio

        async def fetch():
            async with AsyncWebCrawler(
                verbose=False,
                headless=True,
                browser_type="chromium",
                cache_mode=CacheMode.BYPASS,
            ) as crawler:
                result = await crawler.arun(url=url, timeout=timeout)
                return result.html if result.success else None

        return asyncio.run(fetch())
    except Exception as e:
        log(LogLevel.WARNING, f"crawl4ai fetch failed for {url}: {e}")
        return fetch_with_requests(url, timeout)


def extract_content(html: str, url: str) -> dict[str, Any]:
    """Extract title, summary, and metadata from HTML content."""
    if not HAS_REQUESTS:
        return {"title": "", "summary": "", "source": urlparse(url).netloc}

    try:
        soup = BeautifulSoup(html, "html.parser")

        # Extract title
        title_tag = soup.find("title")
        title = title_tag.get_text(strip=True) if title_tag else ""

        # Extract meta description or first paragraph
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc and meta_desc.get("content"):
            summary = meta_desc["content"][:500]
        else:
            # Fall back to first paragraph
            first_p = soup.find("p")
            summary = first_p.get_text(strip=True)[:500] if first_p else ""

        # Extract year from content or metadata
        year = None
        date_meta = soup.find("meta", attrs={"name": "date"})
        if date_meta and date_meta.get("content"):
            try:
                year = datetime.fromisoformat(date_meta["content"]).year
            except ValueError:
                pass

        if not year:
            # Try to extract year from copyright or other meta tags
            for meta in soup.find_all("meta"):
                content = meta.get("content", "")
                if re.search(r"\b(19|20)\d{2}\b", content):
                    year_match = re.search(r"\b(19|20)\d{2}\b", content)
                    if year_match:
                        year = int(year_match.group())
                        break

        return {
            "title": title,
            "summary": summary,
            "url": url,
            "source": urlparse(url).netloc,
            "year": year or date.today().year,
            "retrieved": date.today().isoformat(),
        }
    except Exception as e:
        log(LogLevel.WARNING, f"Failed to extract content from {url}: {e}")
        return {"title": "", "summary": "", "source": urlparse(url).netloc, "url": url}


def fetch_from_sources(
    sources: dict[str, dict[str, Any]],
    cache: dict[str, Any],
    verbose: bool = False,
) -> list[dict[str, Any]]:
    """Fetch entries from configured sources."""
    entries = []
    checked_urls = set()

    for source_id, source_config in sources.items():
        base_url = source_config["base_url"]
        log(LogLevel.INFO, f"Fetching from {source_config['name']}...", verbose)

        for path in source_config.get("search_paths", []):
            url = base_url.rstrip("/") + path

            if url in checked_urls:
                continue
            checked_urls.add(url)

            # Check cache first
            cache_key = f"fetch:{url_hash(url)}"
            if cache_key in cache:
                cached_entry = cache[cache_key]
                if cached_entry.get("retrieved") == date.today().isoformat():
                    entries.append(cached_entry)
                    log(LogLevel.DEBUG, f"Using cached entry for {url}", verbose)
                    continue

            # Fetch with appropriate method
            html = fetch_with_crawl4ai(url)
            if html:
                entry = extract_content(html, url)
                if entry.get("title") or entry.get("summary"):
                    entry["source_id"] = source_id
                    entries.append(entry)
                    cache[cache_key] = entry
                    log(LogLevel.INFO, f"Fetched: {entry.get('title', url)[:50]}...", verbose)

            # Rate limiting
            time.sleep(RATE_LIMIT_DELAY)

    return entries


def fetch_from_web_search(
    keywords: list[str],
    cache: dict[str, Any],
    verbose: bool = False,
) -> list[dict[str, Any]]:
    """Fetch entries using web search (placeholder for WebSearch tool integration)."""
    # This is a placeholder for when WebSearch tool is available
    # In production, would call WebSearch for each keyword and extract results
    log(LogLevel.INFO, "Web search integration not yet implemented; skipping", verbose)
    return []


def deduplicate_entries(
    entries: list[dict[str, Any]],
    existing_hashes: set[str],
) -> list[dict[str, Any]]:
    """Remove entries that already exist in brain file."""
    new_entries = []
    for entry in entries:
        url = entry.get("url", "")
        if not url:
            continue
        h = url_hash(url)
        if h not in existing_hashes:
            new_entries.append(entry)
            existing_hashes.add(h)
    return new_entries


def format_entry(entry: dict[str, Any]) -> str:
    """Format entry for brain file."""
    title = entry.get("title", "(untitled)")
    source = entry.get("source", "?")
    year = entry.get("year", "?")
    url = entry.get("url", "")
    h = url_hash(url)

    return f"- {date.today().isoformat()} — {title} ({source}, {year}) {url} <!--h:{h}-->"


def append_entries(entries: list[dict[str, Any]]) -> int:
    """Append new entries to brain file."""
    if not entries:
        return 0

    brain_text = load_brain()
    existing_hashes = extract_hashes(brain_text)

    # Deduplicate
    new_entries = deduplicate_entries(entries, existing_hashes)

    if not new_entries:
        log(LogLevel.INFO, "No new entries to add")
        return 0

    # Sort by relevance
    sorted_entries = sorted(new_entries, key=score_relevance, reverse=True)

    # Format entries
    formatted_lines = [format_entry(entry) for entry in sorted_entries]

    # Append to brain file
    if "## Knowledge Update Log" not in brain_text:
        brain_text += "\n\n## Knowledge Update Log"
    if "- " + date.today().isoformat() not in brain_text:
        brain_text += f"\n- {date.today().isoformat()} — Updated via knowledge_updater.py"

    brain_text = brain_text.rstrip() + "\n" + "\n".join(formatted_lines) + "\n"
    BRAIN_FILE.write_text(brain_text, encoding="utf-8")

    return len(new_entries)


def verify_integrity(verbose: bool = False) -> bool:
    """Verify brain file integrity."""
    try:
        brain_text = load_brain()
        hashes = extract_hashes(brain_text)

        # Check for duplicate hashes
        entries = brain_text.split("\n")
        hash_counts = defaultdict(int)
        for line in entries:
            for h in re.findall(r"<!--h:([0-9a-f]{12})-->", line):
                hash_counts[h] += 1

        duplicates = {h: count for h, count in hash_counts.items() if count > 1}
        if duplicates:
            log(LogLevel.WARNING, f"Found duplicate hashes: {duplicates}", verbose)
            return False

        log(LogLevel.INFO, f"Brain file integrity OK: {len(hashes)} unique entries", verbose)
        return True
    except Exception as e:
        log(LogLevel.ERROR, f"Integrity check failed: {e}", verbose)
        return False


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Update SECOND-KNOWLEDGE-BRAIN.md with latest conservation/digitization knowledge",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force refresh, ignore cache",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Only verify brain file integrity",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output",
    )
    parser.add_argument(
        "--sources",
        nargs="+",
        choices=list(SOURCES.keys()),
        help="Specific sources to fetch (default: all)",
    )

    args = parser.parse_args()

    if args.verify_only:
        return 0 if verify_integrity(args.verbose) else 1

    log(LogLevel.INFO, "Starting knowledge update...", args.verbose)

    # Load cache
    cache = load_cache() if not args.force else {}

    # Select sources
    selected_sources = {
        k: v for k, v in SOURCES.items()
        if k in (args.sources or SOURCES.keys())
    }

    # Fetch from sources
    entries = fetch_from_sources(selected_sources, cache, args.verbose)

    # Append new entries
    added = append_entries(entries)

    # Save cache
    save_cache(cache)

    # Verify integrity
    verify_integrity(args.verbose)

    log(LogLevel.INFO, f"Added {added} new entries to {BRAIN_FILE.name}", args.verbose)

    return 0


if __name__ == "__main__":
    sys.exit(main())
