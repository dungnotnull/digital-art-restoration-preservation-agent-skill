# CLAUDE.md — Digital Restoration & Preservation of Ancient Artworks (Idea 225)

**Skill name:** `digital-art-restoration-preservation`
**Tagline:** Plans ethical digital restoration and long-term preservation of ancient artworks and documents, grounded in museum conservation and digitization standards.
**Cluster:** `science-industry`
**Source idea:** 225
**Current phase:** Full deliverable set scaffolded

## Problem This Skill Solves
Cultural-heritage holders need to digitally restore degraded artworks/documents and preserve them long-term — without violating conservation ethics (reversibility, minimal intervention, documentation). This skill assesses condition, recommends a digitization workflow to museum standards (FADGI/Metamorfoze), plans ethical digital restoration (inpainting, color/denoise), and a preservation/archival strategy, scoring fidelity and reversibility.

## Harness Flow Summary
1. **Intake** → `sub-requirements-gatherer` — artifact type, condition, goal, equipment.
2. **Framework selection** → `sub-evaluation-framework-selector` — digitization standard + conservation ethics.
3. **Condition assessment** → `sub-condition-assessor` — degradation diagnosis, imaging needs.
4. **Restoration & preservation plan** → `sub-restoration-planner` — reversible digital steps + archival strategy.
5. **Scoring** → `sub-scoring-engine` — fidelity + reversibility + preservation-longevity score.
6. **Roadmap** → execution + documentation plan.

## Sub-skills
- `sub-requirements-gatherer.md`
- `sub-evaluation-framework-selector.md`
- `sub-condition-assessor.md`
- `sub-restoration-planner.md`
- `sub-scoring-engine.md`

## Tools Required
WebSearch, WebFetch, Read, Write, Bash.

## Knowledge Sources
FADGI & Metamorfoze digitization guidelines; ISO digitization standards; conservation ethics (AIC/ICOM-CC, minimal intervention, reversibility); heritage science; multispectral/RTI imaging; OAIS preservation model; file-format/archival standards (TIFF, JPEG2000).

## Supporting Tools
- `tools/knowledge_updater.py` — crawls conservation + digitization + heritage-science sources.

## Active Development Tasks
- [x] Scaffold deliverables
- [ ] Add degradation→imaging mapping table
- [ ] Track archival format standards

## Reference Docs
`PROJECT-detail.md`, `PROJECT-DEVELOPMENT-PHASE-TRACKING.md`, `SECOND-KNOWLEDGE-BRAIN.md`.
