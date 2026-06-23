# PROJECT-detail.md — Digital Restoration & Preservation of Ancient Artworks

## Executive Summary
A harness for heritage holders that plans ethical digital restoration and durable preservation of ancient artworks and documents. It assesses degradation, prescribes a standards-compliant digitization workflow (FADGI/Metamorfoze), plans reversible, well-documented digital restoration (inpainting, color correction, denoising), and designs a long-term archival strategy (OAIS, archival formats). It scores fidelity, reversibility, and preservation longevity.

## Problem Statement
Naive "restoration" can erase historical evidence and is often irreversible. Heritage work demands minimal intervention, full documentation, and durable formats. Institutions and collectors need a principled, standards-grounded plan.

## Target Users & Use Cases
- **Museum/archivist** — "Digitize and restore a faded manuscript ethically." → workflow + restoration plan.
- **Conservator** — "What imaging reveals under-drawing?" → multispectral/RTI recommendation.
- **Collector** — "Preserve a damaged painting digitally." → restoration + archival plan.
- **Heritage NGO** — "Preservation strategy for a photo collection." → OAIS-based plan.
- **Researcher** — "Color-correct without distorting evidence." → documented, reversible steps.

## Harness Architecture
```
/digital-art-restoration-preservation
  Stage 1 Intake     → sub-requirements-gatherer        → artifact/condition/goal
  Stage 2 Framework  → sub-evaluation-framework-selector→ digitization std + ethics
  Stage 3 Assess     → sub-condition-assessor           → degradation + imaging needs
  Stage 4 Plan       → sub-restoration-planner          → reversible steps + archival
  Stage 5 Scoring    → sub-scoring-engine               → fidelity/reversibility/longevity
  Stage 6 Roadmap    → execution + documentation plan
```

## Full Sub-Skill Catalog
| Sub-skill | Purpose | Inputs | Outputs | Tools | Quality gate |
|-----------|---------|--------|---------|-------|--------------|
| requirements-gatherer | Brief | user | artifact/goal | Read | Type + condition + goal |
| framework-selector | Standards | profile | std + ethics | WebSearch | FADGI/Metamorfoze + ethics chosen |
| condition-assessor | Diagnose | artifact | degradation + imaging | WebSearch | Imaging matched to degradation |
| restoration-planner | Plan | assessment | reversible steps + archival | — | Reversibility + documentation |
| scoring-engine | Score | plan | scores | — | Fidelity+reversibility+longevity |

## Skill File Format Specification
Standard Claude skill format. See `skills/main.md`.

## E2E Execution Flow
Intake → framework → assess → plan → score → roadmap. Fallback to cached standards if web down. Error: physical (not digital) intervention requested → defer to a qualified conservator; keep scope digital.

## SECOND-KNOWLEDGE-BRAIN Integration
`knowledge_updater.py` crawls conservation/digitization/heritage-science sources; dated append.

## Quality Gates
- Digitization workflow cites a standard (FADGI/Metamorfoze) with capture specs.
- Restoration steps are reversible (non-destructive) and fully documented.
- Original/master preserved unaltered; restoration on a derivative.
- Archival strategy uses durable formats + OAIS principles.
- Conservation ethics (minimal intervention) respected.

## Test Scenarios
See `tests/test-scenarios.md` (6 scenarios).

## Key Design Decisions
1. Master scan preserved untouched; all edits on derivatives.
2. Minimal-intervention + reversibility are hard ethics gates.
3. Full documentation of every restoration step.
4. Durable archival formats (TIFF/JPEG2000) + OAIS.
5. Physical conservation deferred to qualified professionals.
