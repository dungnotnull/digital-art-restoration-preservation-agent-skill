---
name: sub-scoring-engine
description: Scores restoration and preservation plans on fidelity, reversibility, and longevity dimensions; flags ethics violations as blockers; provides actionable improvement recommendations. Shared across science-industry cluster.
---

## Purpose
Quantify the ethical and technical quality of a digital restoration and preservation plan. Scores guide decision-making and ensure plans meet conservation ethics and long-term preservation standards before execution.

## Procedure

### Step 1 — Fidelity Scoring
Assess how faithfully the restoration reflects original evidence.

**Fidelity dimensions (0-100 each; weighted average for overall fidelity):**

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| **Color accuracy** | 0.30 | Color corrections match reference targets (ColorChecker, known values) |
| **Detail preservation** | 0.25 | No artificial sharpening that creates detail; fine details preserved |
| **Absence of invention** | 0.25 | No invented content beyond documented reconstruction |
| **Evidence-based intervention** | 0.20 | Every change justified by evidence; no arbitrary "improvements" |

**Scoring rubric (each dimension):**

| Score | Quality | Description |
|-------|---------|-------------|
| 90-100 | Excellent | At or exceeds FADGI 4-star / Metamorfoze Preservation; ΔE < 2.0; no invention |
| 75-89 | Good | Meets FADGI 3-star / Metamorfoze Access; minor deviations from target; no invention |
| 60-74 | Acceptable | Minor color/exposure deviations; some over-sharpening; no major invention |
| 40-59 | Marginal | Noticeable color/exposure shifts; visible artifacts; some invention |
| 0-39 | Poor | Severe deviations; heavy-handed editing; significant invention; obscures original |

**Color accuracy scoring:**
- **90-100**: ΔE < 2.0 from target (imperceptible difference); all color patches within tolerance
- **75-89**: ΔE 2.0-5.0 (acceptable but not imperceptible); most patches within tolerance
- **60-74**: ΔE 5.0-10.0 (noticeable but not egregious)
- **40-59**: ΔE 10.0-20.0 (clearly visible color cast or shift)
- **0-39**: ΔE > 20.0 (severe color distortion; colors unrecognizable)

**Detail preservation scoring:**
- **90-100**: No artificial sharpening halos; fine detail (brushwork, paper texture) preserved; no noise reduction artifacts
- **75-89**: Mild sharpening, no halos; detail preserved in key areas
- **60-74**: Noticeable sharpening; some detail loss in flat areas from noise reduction
- **40-59**: Heavy sharpening with halos; significant detail loss
- **0-39**: Oversharpened or oversmoothed; fine detail destroyed

**Absence of invention scoring:**
- **90-100**: No invented content; reconstruction clearly labeled and separated; all changes recovery-based
- **75-89**: Reconstruction labeled but some ambiguous areas; no major invention
- **60-74**: Minor reconstruction without explicit labeling; mostly recovery-based
- **40-59**: Some invention (e.g., filling losses without documentation)
- **0-39**: Significant invention presented as if original (major ethics violation)

**Evidence-based intervention scoring:**
- **90-100**: Every change justified by documented evidence; arbitrary improvements absent
- **75-89**: Most changes evidence-based; minor aesthetic adjustments documented
- **60-74**: Some arbitrary adjustments (e.g., "made it look better") but mostly evidence-based
- **40-59**: Significant arbitrary changes; poor documentation
- **0-39**: Changes based on whim or aesthetics; no evidence base

**Overall fidelity score:**
```
fidelity = (color_accuracy * 0.30) + (detail_preservation * 0.25) +
          (absence_of_invention * 0.25) + (evidence_based * 0.20)
```

### Step 2 — Reversibility Scoring
Assess whether all interventions are reversible and retreatable.

**Reversibility dimensions (0-100 each; weighted average):**

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| **Master preservation** | 0.40 | Master file untouched and archived |
| **Non-destructive editing** | 0.30 | All edits on layers/adjustments; no direct pixel editing |
| **Editability** | 0.20 | Layered file preserved; steps can be revisited |
| **Documentation completeness** | 0.10 | Every step documented with parameters |

**Scoring rubric (each dimension):**

**Master preservation:**
- **100**: Master file confirmed untouched; stored separately; checksum verified
- **80**: Master file untouched but not checksum-verified
- **60**: Master file preserved but derivative workflow unclear
- **40**: Master file risk of confusion with derivatives (poor naming)
- **0**: Master file edited or overwritten (BLOCKER)

**Non-destructive editing:**
- **90-100**: All edits on layers/adjustments; no direct pixel modification
- **70-89**: Mostly non-destructive; minor direct edits on separate layers
- **50-69**: Mix of destructive and non-destructive; some layers not preserved
- **30-49**: Primarily destructive editing; few layers preserved
- **0-29**: Fully destructive editing (BLOCKER for reversibility)

**Editability:**
- **90-100**: Layered file (PSD/XCF) saved; all layers editable; history preserved
- **70-89**: Layered file saved; some layers merged; most edits still revisable
- **50-69**: Layered file saved but many layers merged; limited editability
- **30-49**: Limited layer structure; most edits flattened
- **0-29**: Flattened file; no editability (BLOCKER for reversibility)

**Documentation completeness:**
- **90-100**: Every step documented with what, why, parameters, layer reference
- **70-89**: Most steps documented; minor gaps
- **50-69**: Some steps documented; major gaps or vague descriptions
- **30-49**: Minimal documentation; mostly "color corrected" without details
- **0-29**: No documentation (BLOCKER for reversibility)

**Overall reversibility score:**
```
reversibility = (master_preservation * 0.40) + (non_destructive * 0.30) +
                 (editability * 0.20) + (documentation * 0.10)
```

### Step 3 — Longevity Scoring
Assess preservation strategy for long-term viability.

**Longevity dimensions (0-100 each; weighted average):**

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| **Format durability** | 0.30 | Use of preservation formats (TIFF, JPEG2000) |
| **Metadata richness** | 0.25 | Comprehensive descriptive + administrative metadata |
| **Fixity strategy** | 0.20 | Checksums + verification schedule |
| **Storage redundancy** | 0.15 | Multiple copies (minimum 3) in separate locations |
| **Migration planning** | 0.10 | Format monitoring + planned migrations |

**Scoring rubric (each dimension):**

**Format durability:**
- **90-100**: Master in uncompressed TIFF or JPEG2000 lossless; access in JPEG/JPEG2000; no proprietary formats
- **75-89**: Master in TIFF (LZW compression acceptable); appropriate access formats
- **60-74**: Master in preservation format but some access in less durable format
- **40-59**: Master in acceptable format but some risk (e.g., older TIFF variant)
- **0-39**: Master in lossy or proprietary format (BLOCKER)

**Metadata richness:**
- **90-100**: Dublin Core + PREMIS + technical (EXIF/IPTC/XMP) + structural (METS/BagIt)
- **75-89**: Dublin Core + PREMIS + technical metadata
- **60-74**: Dublin Core + basic technical metadata
- **40-59**: Minimal metadata (title, identifier only)
- **0-29**: No metadata (BLOCKER for preservation)

**Fixity strategy:**
- **90-100**: SHA-256 checksums for all files; stored separately; annual verification schedule
- **75-89**: SHA-256 checksums; periodic verification (every 2-3 years)
- **60-74**: Checksums generated but no verification schedule
- **40-59**: Some checksums (e.g., master only)
- **0-29**: No fixity strategy (BLOCKER)

**Storage redundancy:**
- **90-100**: 3+ copies in geographically separate locations; access tier separate from preservation
- **75-89**: 3 copies; backups in separate locations
- **60-74**: 2 copies (primary + 1 backup)
- **40-59**: Single copy with promise of backup
- **0-29**: Single copy with no backup (BLOCKER)

**Migration planning:**
- **90-100**: Format monitoring defined; migration every 5 years; migration pipeline tested
- **75-89**: Planned migration every 5-10 years
- **60-74**: Recognition that migration will be needed but no specific plan
- **40-59**: Vague commitment to "migrate when needed"
- **0-29**: No awareness of format obsolescence risk

**Overall longevity score:**
```
longevity = (format_durability * 0.30) + (metadata * 0.25) +
            (fixity * 0.20) + (redundancy * 0.15) + (migration * 0.10)
```

### Step 4 — Ethics Violation Check
Identify deal-breaker ethics violations.

**Blocker ethics violations (any of these = plan rejected):**

1. **Master file edited or overwritten** — Master discipline violated
2. **Destructive editing only** — No non-destructive alternatives used; cannot undo changes
3. **Reconstruction presented as original** — Invented content not labeled as interpretive
4. **No documentation** — Steps not documented; cannot audit or replicate
5. **Physical treatment without qualified conservator** — Scope creep beyond digital
6. **Destruction of historical evidence** — "Improvements" that erase original characteristics

**Warning ethics violations (should be fixed but not blockers):**

1. **Poor documentation** — Steps documented but vaguely or incompletely
2. **Minimal metadata** — Some metadata but missing key fields
3. **Insufficient backups** — Less than 3 copies or geographically co-located
4. **No verification schedule** — Fixity not periodically verified
5. **Reconstruction ambiguity** — Reconstruction exists but not clearly labeled

### Step 5 — Overall Assessment & Recommendations

**Overall quality tier:**

| Overall Score | Tier | Meaning |
|---------------|------|---------|
| 90-100 | Excellent | Exceeds standards; ready for production |
| 75-89 | Good | Meets standards; minor improvements recommended |
| 60-74 | Acceptable | Meets minimum standards; improvements needed |
| 40-59 | Marginal | Below standards; significant revisions required |
| 0-39 | Poor | Fails standards; plan rejected |

**Improvement recommendations:**
- Identify lowest-scoring dimensions
- Provide specific actions to improve each dimension
- Prioritize: address blockers first, then warnings, then enhancements

## Outputs

**Scorecard:**
```yaml
scorecard:
  fidelity:
    overall: [0-100]
    dimensions:
      color_accuracy:
        score: [0-100]
        rationale: "[specific feedback; e.g., ΔE 3.2 from target]"
      detail_preservation:
        score: [0-100]
        rationale: "[e.g., mild sharpening halos visible at 200%]"
      absence_of_invention:
        score: [0-100]
        rationale: "[e.g., all changes evidence-based; reconstruction labeled]"
      evidence_based:
        score: [0-100]
        rationale: "[e.g., every change justified by documentation]"
    improvement_actions:
      - "[specific action to improve fidelity]"
  
  reversibility:
    overall: [0-100]
    dimensions:
      master_preservation:
        score: [0-100]
        rationale: "[e.g., master confirmed untouched; checksum verified]"
      non_destructive_editing:
        score: [0-100]
        rationale: "[e.g., all edits on layers; no direct pixel modification]"
      editability:
        score: [0-100]
        rationale: "[e.g., layered PSD saved; all layers editable]"
      documentation_completeness:
        score: [0-100]
        rationale: "[e.g., every step documented with parameters]"
    improvement_actions:
      - "[specific action to improve reversibility]"
  
  longevity:
    overall: [0-100]
    dimensions:
      format_durability:
        score: [0-100]
        rationale: "[e.g., TIFF master; JPEG2000 access; no proprietary formats]"
      metadata_richness:
        score: [0-100]
        rationale: "[e.g., Dublin Core + PREMIS + technical metadata]"
      fixity_strategy:
        score: [0-100]
        rationale: "[e.g., SHA-256 checksums; annual verification]"
      storage_redundancy:
        score: [0-100]
        rationale: "[e.g., 3 copies in geographically separate locations]"
      migration_planning:
        score: [0-100]
        rationale: "[e.g., format monitoring; migration every 5 years]"
    improvement_actions:
      - "[specific action to improve longevity]"
  
  overall:
    score: [0-100]  # Weighted average: fidelity*0.35 + reversibility*0.35 + longevity*0.30
    tier: [Excellent | Good | Acceptable | Marginal | Poor]
    ready: [yes | no]
    rationale: "[summary of why this tier]"
  
  ethics_check:
    blockers:
      - "[list any blocker violations; plan rejected if any]"
    warnings:
      - "[list any warning violations; should be fixed]"
    passed: [yes | no]
```

**Summary narrative** (2-3 paragraphs):
- Overall quality tier and what that means
- Key strengths (highest-scoring areas)
- Key weaknesses (lowest-scoring areas)
- Priority improvements (blockers first, then high-impact improvements)

## Quality Gates

**Must achieve before execution:**
1. [ ] All three dimensions scored (fidelity, reversibility, longevity)
2. [ ] Ethics check completed (blockers and warnings identified)
3. [ ] Overall score calculated
4. [ ] Improvement recommendations provided for dimensions below 75
5. [ ] If ethics blockers present → plan rejected; user must revise and resubmit

**Passing thresholds:**
- **For execution**: overall score ≥ 60 AND no ethics blockers
- **For publication**: overall score ≥ 75 AND no ethics warnings
- **For museum/archival use**: overall score ≥ 90 AND ethics blockers and warnings both empty

## Error Handling

**If scoring criteria are ambiguous:**
- Make conservative assumption (score lower rather than higher)
- Flag ambiguity in rationale; suggest clarification

**If plan has ethics blockers:**
- Reject plan; do not proceed
- Provide specific guidance on what must change
- Allow user to revise and resubmit for re-scoring

**If insufficient information to score:**
- Flag as incomplete; request missing information
- Do not guess or assume; score only what is documented

## Fallback Mechanisms

- If color target not available, cannot score color accuracy → flag as limitation; score other dimensions
- If metadata schema not specified, assume minimal → score accordingly; recommend upgrade
- If migration planning absent, score lowest on that dimension; recommend planning

## Notes for Next Stage

- Scores inform final go/no-go decision before execution
- Improvement recommendations guide plan revision
- High scores (≥75) on all dimensions indicate plan is ready for production execution
