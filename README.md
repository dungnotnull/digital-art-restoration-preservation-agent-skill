# Digital Art Restoration & Preservation

**Skill name:** `digital-art-restoration-preservation`
**Tagline:** Plans ethical digital restoration and long-term preservation of ancient artworks and documents, grounded in museum conservation and digitization standards.
**Cluster:** `science-industry`
**Source idea:** 225
**Status:** Production-ready, open-source ready
**Version:** 1.0.0

## Overview

This skill helps cultural-heritage holders (museums, archives, collectors, researchers) plan ethical digital restoration and preservation of degraded artworks and documents. It enforces conservation ethics (minimal intervention, reversibility, documentation), applies museum digitization standards (FADGI/Metamorfoze), and designs OAIS-compliant preservation strategies.

## What It Does

- **Assess condition** of artworks/documents and recommend imaging (multispectral, IR, UV, RTI) matched to degradation
- **Select appropriate digitization standards** (FADGI star ratings or Metamorfoze tiers) with capture specifications
- **Plan reversible digital restoration** on derivatives (never the master) with full documentation
- **Design preservation strategies** following OAIS model (archival formats, metadata, fixity, migration)
- **Score plans** on fidelity, reversibility, and longevity; flag ethics violations as blockers

## Target Users

- Museum/archivists digitizing collections
- Conservators needing digital workflow guidance
- Collectors preserving damaged artworks
- Heritage NGOs planning preservation strategies
- Researchers color-correcting without distorting evidence

## Key Features

### Conservation Ethics (Non-Negotiable)
- **Minimal intervention** — do only what's necessary; respect original material
- **Reversibility** — all digital interventions are non-destructive (layers, masks, adjustments)
- **Documentation** — every decision, technique, and parameter logged
- **Respect for original** — master file preserved untouched; derivatives for editing
- **Revelation vs. reconstruction** — recovering existing info ≠ inventing missing info

### Technical Standards
- **FADGI** (US Federal Agencies) — 1-4+ star ratings with capture specs
- **Metamorfoze** (Netherlands National Archive) — Access/Preservation/Special tiers
- **OAIS** — Open Archival Information System reference model for long-term preservation
- **Formats** — Uncompressed TIFF or JPEG2000 lossless for masters; JPEG for access

### Quality Assurance
- **6-stage workflow** — Intake → Framework → Condition → Planning → Scoring → Roadmap
- **Quality gates** at each stage
- **Ethics violation detection** — blockers (master overwrite, destructive editing) and warnings
- **Comprehensive scoring** — fidelity, reversibility, longevity (0-100 each)

## Installation

This is a Claude Code skill. Install via:

```bash
npx skills add digital-art-restoration-preservation
```

Or clone and reference in your Claude skills directory.

## Usage

### Basic Workflow

1. **Invoke the skill** and provide artifact details:
   - Artifact type (painting, manuscript, photograph, etc.)
   - Material and condition
   - Goal (restoration, preservation, access, research)
   - Available equipment

2. **Receive a comprehensive plan** including:
   - Digitization standard and capture specifications
   - Imaging recommendations (multispectral, IR, UV as needed)
   - Step-by-step restoration workflow (non-destructive)
   - Preservation/archival strategy (OAIS-compliant)
   - Quality scorecard with improvement recommendations
   - Execution roadmap with timeline and deliverables

### Example Input

```
I have a faded 15th-century parchment manuscript with faded iron gall ink.
We want to digitize it and make the text legible again.
We have a Nikon D850 and an IR-modified camera available.
```

### Example Output

The skill generates a structured plan with:
- **Standards applied:** FADGI 4-Star with IR imaging
- **Imaging plan:** High-res RGB baseline + IR to reveal faded ink
- **Restoration steps:** Non-destructive curves adjustment → IR channel extraction
- **Archival strategy:** TIFF master, JPEG2000 access, SHA-256 checksums, 3-copy storage
- **Scorecard:** Fidelity 85, Reversibility 90, Longevity 88 — Tier: Good

## Project Structure

```
/digital-art-restoration-preservation
  skills/
    main.md                          # Main orchestration skill
    sub-requirements-gatherer.md     # Stage 1: Intake
    sub-evaluation-framework-selector.md  # Stage 2: Framework selection
    sub-condition-assessor.md        # Stage 3: Condition assessment
    sub-restoration-planner.md       # Stage 4: Restoration & preservation planning
    sub-scoring-engine.md            # Stage 5: Quality scoring
  tools/
    knowledge_updater.py             # Knowledge base crawler
  tests/
    test_suite.py                    # Comprehensive test suite
  CLAUDE.md                          # Skill configuration
  PROJECT-detail.md                  # Project documentation
  PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Development tracking
  CLUSTER-INTEGRATION.md             # Cluster shared components
  SECOND-KNOWLEDGE-BRAIN.md          # Knowledge base
  README.md                          # This file
```

## Development

### Running Tests

```bash
python tests/test_suite.py
```

Covers 6 scenarios plus edge cases and integration tests.

### Updating Knowledge Base

```bash
python tools/knowledge_updater.py
```

Fetches latest from conservation/digitization sources and appends to SECOND-KNOWLEDGE-BRAIN.md.

## Standards Compliance

This skill implements and references:

- **FADGI** — https://www.digitizationguidelines.gov/
- **Metamorfoze** — https://www.metamorfoze.nl/en
- **AIC Code of Ethics** — https://www.culturalheritage.org/about-us/core-documents-of-the-profession
- **ICOM-CC** — https://www.icom-cc.org/
- **OAIS (ISO 14721)** — https://public.ccsds.org/Pubs/650x0m2.pdf
- **Dublin Core** — https://www.dublincore.org/
- **PREMIS** — https://www.loc.gov/standards/premis/

## Cluster Integration

This skill shares components with the science-industry cluster:

- **`sub-evaluation-framework-selector`** — shared with Ideas 97, 116
- **`sub-scoring-engine`** — shared with Ideas 97, 116

See CLUSTER-INTEGRATION.md for details.

## License

[Specify your open-source license here]

## Contributing

Contributions welcome! Please read CONTRIBUTING.md (to be added) for guidelines.

## Citation

If you use this skill in your work, please cite:

```
Digital Art Restoration & Preservation Skill (Idea 225).
Anthropic Skills Registry. https://github.com/anthropics/skills
```

## Acknowledgments

Developed as part of the Claude Skills ecosystem. Incorporates standards from:
- Federal Agencies Digitization Guidelines Initiative (FADGI)
- Metamorfoze (Netherlands National Archive)
- American Institute for Conservation (AIC)
- International Council of Museums - Conservation Committee (ICOM-CC)
- Getty Conservation Institute

## Version History

- **1.0.0** (2026-06-23) — Initial release. All phases complete. Production-ready.
