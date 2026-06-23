# SECOND-KNOWLEDGE-BRAIN — Digital Art Restoration & Preservation

## Core Concepts & Frameworks
- **Conservation ethics** — minimal intervention, **reversibility**, retreatability, full documentation, respect for original material (AIC Code of Ethics; ICOM-CC).
- **Digitization standards** — FADGI (US) star ratings; Metamorfoze (NL) preservation imaging guidelines; ISO 19264 image-quality; color targets, resolution, bit depth.
- **Imaging techniques** — high-res RGB, multispectral/hyperspectral (reveals under-drawing, faded ink), RTI (Reflectance Transformation Imaging) for surface texture, IR/UV.
- **Digital restoration** — non-destructive inpainting, color correction (to documented reference), denoising, dewarping — all on derivatives, never the master.
- **Preservation (OAIS)** — Open Archival Information System reference model; ingest, archival storage, fixity (checksums), migration.
- **Archival formats** — uncompressed/lossless TIFF, JPEG2000; rich metadata (Dublin Core, METS, PREMIS).

## Key Reference Frameworks (citable)
| Framework | Source | Use |
|-----------|--------|-----|
| FADGI guidelines | US Federal Agencies | Capture specs |
| Metamorfoze | NL National Archive | Preservation imaging |
| AIC Code of Ethics | AIC | Conservation ethics |
| OAIS (ISO 14721) | CCSDS/ISO | Long-term preservation |

## Key Research / References
| Title | Source | Year | Link | Relevance |
|-------|--------|------|------|-----------|
| FADGI Technical Guidelines | FADGI | ongoing | digitizationguidelines.gov | Imaging specs |
| OAIS Reference Model | CCSDS | 2012 | public.ccsds.org | Archival model |

## State-of-the-Art Methods & Tools
ML inpainting (respecting documentation); multispectral imaging systems; RTI capture; IIIF for access; fixity/checksum tools; format-migration pipelines.

## Authoritative Data Sources
digitizationguidelines.gov (FADGI); metamorfoze.nl; culturalheritage.org (AIC); ICOM-CC; getty.edu conservation; ISO.

## Analytical Frameworks
Degradation→imaging mapping; reversibility check; master-vs-derivative discipline; OAIS preservation plan; documentation completeness audit.

## Self-Update Protocol
`knowledge_updater.py` weekly: crawl conservation/digitization/heritage-science sources; dedup by URL hash; append below.

## Knowledge Update Log
- 2026-06-18 — Seed: ethics, FADGI/Metamorfoze, OAIS, imaging captured.
