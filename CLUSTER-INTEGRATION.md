# Cluster Integration — Digital Art Restoration & Preservation (Idea 225)

## Science-Industry Cluster Shared Components

This skill shares components with related skills in the science-industry cluster:

### Shared Sub-Skills

#### `sub-evaluation-framework-selector`
**Shared with:**
- Idea 97: Scientific Data Preservation (hypothetical)
- Idea 116: Research Digitization Standards (hypothetical)
- Any skill requiring FADGI/Metamorfoze standard selection

**Purpose:** Select digitization standards (FADGI/Metamorfoze) and conservation/ethics frameworks.

**Shared content:**
- FADGI star rating system (1-4+)
- Metamorfoze preservation tiers (Access, Preservation, Special)
- Capture specifications (PPI, bit depth, color space, Delta E targets)
- Conservation ethics principles (minimal intervention, reversibility, documentation)

**Integration points:**
- Standard selection logic identical across cluster
- Ethics framework shared (AIC Code of Ethics, ICOM-CC)
- Archival model (OAIS) applicable to all preservation-focused skills

#### `sub-scoring-engine`
**Shared with:**
- Idea 97: Scientific Data Preservation
- Idea 116: Research Digitization Standards
- Any quality-assessment focused skill

**Purpose:** Score plans on fidelity, reversibility, longevity; flag ethics violations.

**Shared content:**
- Fidelity scoring: color accuracy, detail preservation, absence of invention, evidence-based intervention
- Reversibility scoring: master preservation, non-destructive editing, editability, documentation completeness
- Longevity scoring: format durability, metadata richness, fixity strategy, storage redundancy, migration planning
- Ethics blocker/warning classification

**Integration points:**
- Scoring rubrics applicable to any digitization/preservation plan
- Ethics blockers (master overwrite, destructive editing, no documentation) universal
- Improvement recommendations framework shared

## Cross-Cluster References

### Related Skills (Science-Industry Cluster)

| Idea ID | Skill Name | Shared Components | Relationship |
|---------|------------|-------------------|--------------|
| 97 | Scientific Data Preservation | `sub-evaluation-framework-selector`, `sub-scoring-engine` | Both apply digitization standards and quality scoring; different artifact types (scientific data vs. cultural heritage) |
| 116 | Research Digitization Standards | `sub-evaluation-framework-selector` | Both select FADGI/Metamorfoze; different use cases (research output vs. cultural artifacts) |
| 225 | Digital Art Restoration & Preservation (this skill) | `sub-evaluation-framework-selector`, `sub-scoring-engine` | Origin of shared components; focuses on cultural heritage |

### Integration Benefits

**Standardization:**
- Consistent framework selection across cluster ensures compatibility
- Shared scoring rubric enables cross-project quality comparison
- Unified ethics framework prevents scope drift

**Reusability:**
- `sub-evaluation-framework-selector` can be invoked by any digitization-focused skill
- `sub-scoring-engine` provides quality assessment for any preservation plan
- Reduces duplication; changes to shared components benefit all skills

**Interoperability:**
- Plans scored with shared rubric can be compared across projects
- Standard metadata (Dublin Core, PREMIS) enables cross-repository discovery
- OAIS preservation model ensures long-term compatibility

## External Standards References

This skill integrates with external standards bodies:

### Digitization Standards
- **FADGI (Federal Agencies Digitization Guidelines Initiative)**
  - URL: https://www.digitizationguidelines.gov/
  - Used by: US federal agencies, libraries, archives
  - Reference: Star rating system for image quality

- **Metamorfoze (Netherlands National Archive)**
  - URL: https://www.metamorfoze.nl/en
  - Used by: European archives, libraries
  - Reference: Preservation imaging guidelines

### Conservation Ethics
- **AIC (American Institute for Conservation) Code of Ethics**
  - URL: https://www.culturalheritage.org/about-us/core-documents-of-the-profession
  - Reference: Minimal intervention, reversibility, documentation

- **ICOM-CC (International Council of Museums - Conservation Committee)**
  - URL: https://www.icom-cc.org/
  - Reference: International conservation ethics standards

### Preservation Models
- **OAIS (Open Archival Information System, ISO 14721)**
  - URL: https://public.ccsds.org/Pubs/650x0m2.pdf
  - Reference: Long-term preservation reference model

### Metadata Standards
- **Dublin Core**
  - URL: https://www.dublincore.org/
  - Reference: Descriptive metadata schema

- **PREMIS (PREservation Metadata: Implementation Strategies)**
  - URL: https://www.loc.gov/standards/premis/
  - Reference: Preservation metadata

## Implementation Notes

### For Skill Developers

**To use shared components in your skill:**

1. **Reference shared sub-skill:**
   - In your main.md, add to sub-skills list:
     ```markdown
     Sub-skills Available:
     - sub-evaluation-framework-selector.md (shared)
     - sub-scoring-engine.md (shared)
     ```

2. **Invoke shared sub-skill:**
   - Use same invocation pattern as other stages:
     ```markdown
     **Invoke**: Sub-skill `sub-evaluation-framework-selector.md`
     ```

3. **Adapt to your context:**
   - Shared components provide framework; you provide artifact-specific context
   - Example: Scientific data skill uses FADGI but for different artifact types

### For Maintainers

**When updating shared components:**

1. **Update in this skill first (Idea 225)** as origin
2. **Propagate to cluster skills** (97, 116) by copying updated file
3. **Update this CLUSTER-INTEGRATION.md** with any new shared components
4. **Version tag** shared components with date and change description

**Version history:**
- 2026-06-23: Initial shared components (`sub-evaluation-framework-selector`, `sub-scoring-engine`)

## Future Cluster Expansion

Potential future shared components:

1. **`sub-metadata-generator`** — Generate Dublin Core/PREMIS metadata for any digitized object
2. **`sub-format-migration-planner`** — Plan format migrations for any preservation scenario
3. **`sub-oais-packager`** — Package files in OAIS-compliant structure (METS/BagIt)

These would originate from the skill that first needs them, then be shared across cluster.

---

*This integration document is part of Phase 5 (Integration) of PROJECT-DEVELOPMENT-PHASE-TRACKING.md*
