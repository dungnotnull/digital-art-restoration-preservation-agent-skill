---
name: sub-evaluation-framework-selector
description: Selects appropriate digitization standards (FADGI/Metamorfoze), conservation ethics frameworks, and archival models based on artifact profile and institutional requirements. Shared across science-industry cluster.
---

## Purpose
Select the right digitization standard, conservation ethics framework, and preservation model to guide the entire workflow. These choices are the guardrails that ensure ethical, technically sound, and sustainable outcomes.

## Procedure

### Step 1 — Digitization Standard Selection
Choose between FADGI (Federal Agencies Digitization Guidelines Initiative) and Metamorfoze based on artifact profile, institutional context, and goal.

**FADGI (US Federal Agencies) — Star Rating System:**

| Star Level | PPI (min) | Bit Depth | Color Target | Quality | Use Case |
|-----------|-----------|-----------|--------------|---------|----------|
| 1 Star | 300 | 8-bit | sRGB | Basic | Access copies, web display |
| 2 Star | 300 | 8-bit | sRGB + color chart | Good | General reference |
| 3 Star | 400 | 8-bit | sRGB + IT8.7/4 chart | High | High-quality reference |
| 4 Star | 400-600 | 16-bit | Adobe RGB or ProPhoto + charts | Very High | Archival master, research |
| **For exceptional items** | 600+ | 16-bit | ProPhoto RGB + full charts | Museum | Highest fidelity, publication |

**Capture specifications by star level:**
- **Resolution**: minimum PPI; aim for higher if detail is critical
- **Color space**: sRGB (web), Adobe RGB (print), ProPhoto RGB (wide gamut)
- **Bit depth**: 8-bit (gradients may band), 16-bit (smooth gradients, better editing headroom)
- **Color targets**: IT8.7/2, IT8.7/4, or ColorChecker; include grayscale and color patches
- **Delta E target**: CIEDE2000; 4-star aims for ΔE < 2.0 (imperceptible difference)
- **Noise/SNR**: signal-to-noise ratio requirements increase with star level
- **Sharpness/MTF**: modulation transfer function thresholds

**Metamorfoze (Netherlands National Archive) — Preservation Imaging Guidelines:**

| Tier | PPI (min) | Bit Depth | Color Target | Quality | Use Case |
|------|-----------|-----------|--------------|---------|----------|
| Access | 300 | 8-bit | sRGB | Basic | Access copies |
| Preservation | 400 | 16-bit | ProPhoto RGB + charts | Archival | Preservation masters |
| **Special** | 600+ | 16-bit | ProPhoto RGB + full charts | Museum | Exceptional items |

**Metamorfoze-specific requirements:**
- **Uniform lighting**: measured with light meter; aim for <5% variation across target
- **Color charts**: use ColorChecker SG or similar; include in every capture
- **Neutral gray patches**: for white balance and neutrality verification
- **Sharpness**: MTF curves to demonstrate edge detail
- **Noise**: measured in midtone patches; keep below threshold

**Selection Criteria Matrix:**

| Factor | Choose FADGI if... | Choose Metamorfoze if... |
|--------|-------------------|--------------------------|
| Institution | US-based or following US standards | European or following Dutch/NL standards |
| Goal | Broad applicability, US repository requirements | Preservation-focused, strict archival requirements |
| Color gamut | Standard to wide gamut needed | Wide gamut emphasis |
| Documentation preference | Detailed quality metrics | Emphasis on uniform lighting + neutrality |

**Default recommendation:**
- If artifact is high-value or destined for preservation → choose 4-star FADGI or Metamorfoze Preservation
- If artifact is for access only → 2-star FADGI or Metamorfoze Access
- If artifact has exceptional detail or wide color gamut → 4-star or higher with 600+ PPI
- If photograph (daguerreotype, tintype, etc.) → highest feasible PPI (600-1000) to capture plate detail

### Step 2 — Conservation Ethics Framework
Confirm the ethical principles that will guide all decisions.

**Core Conservation Ethics (AIC Code of Ethics; ICOM-CC):**
- **Minimal intervention**: do only what is necessary; respect original material and historical evidence
- **Reversibility**: all digital interventions must be reversible (non-destructive editing)
- **Retreatability**: future conservators/digital specialists should be able to undo or redo work
- **Documentation**: document every decision, technique, and parameter; keep the audit trail
- **Respect for original**: the master is sacred; derivative edits are clearly labeled as such
- **Distinguish revelation from reconstruction**: recovering existing information (faded ink) is fundamentally different from inventing missing information (inpainting losses)

**Ethical constraints checklist:**
- [ ] Master file will never be overwritten or altered
- [ ] All restoration work happens on copies (derivatives)
- [ ] Every edit is logged (what, why, parameters)
- [ ] Reconstruction (interpretive) is clearly labeled as such
- [ ] Original is preserved as the reference of record
- [ ] Decisions are documented with rationale
- [ ] Physical conservation deferred to qualified professionals

**Red lines (never cross):**
- Never overwrite the master
- Never destroy original pixels (always use layers, masks, non-destructive edits)
- Never present reconstruction as if it were original
- Never apply physical treatments (chemicals, cleaning, repair)

### Step 3 — Archival Model Selection
Choose OAIS (Open Archival Information System) or simplified preservation model.

**OAIS Reference Model (ISO 14721) — Core Concepts:**
- **Ingest**: submission of digital content into preservation system
- **Archival Storage**: long-term storage with fixity and migration planning
- **Access**: dissemination to users without compromising preservation
- **Preservation Planning**: format monitoring, migration, emulation planning
- **Data Management**: metadata, fixity, audit trails

**Key OAIS packages for this project:**
- **Content Information**: digital object (master + derivatives) + Representation Information (how to interpret)
- **Preservation Description Information (PDI)**:
  - **Reference**: identifies the object (Dublin Core, etc.)
  - **Provenance**: ownership/custody history
  - **Context**: why it exists, what it relates to
  - **Fixity**: checksums to verify authenticity over time
- **Packaging**: how files are organized and described (METS, BagIt)

**Archival Format Strategy:**
- **Master**: uncompressed TIFF (LZW compression acceptable) or JPEG2000 (lossless)
- **Derivatives**: JPEG (access), JPEG2000 (balanced quality/size)
- **Metadata**: embedded (IPTC/XMP) + sidecar (XML for complex metadata)
- **Fixity**: checksums (SHA-256) stored separately; verify regularly

**Metadata Standards:**
- **Descriptive**: Dublin Core (title, creator, date, format, etc.)
- **Administrative**: PREMIS (rights, format, preservation events)
- **Technical**: EXIF/IPTC/XMP embedded in files
- **Structural**: METS (how files relate) or simple manifest

**Storage Strategy:**
- **Primary**: stable storage (institutional server, cloud storage)
- **Backup**: geographically separate backup
- **Fixity checking**: regular verification (annually or after migrations)
- **Migration planning**: format migration schedule (e.g., review formats every 5 years)

**Simplified preservation model (if OAIS is overkill):**
- Master + derivatives stored with clear naming
- Checksums recorded and verified periodically
- Migration plan documented but less formal

### Step 4 — Justification & Documentation
Document the chosen framework with rationale.

**Framework selection rationale:**
- Why this standard? (institutional requirement, artifact value, goal alignment)
- Why this ethics framework? (minimal intervention is non-negotiable; reversibility ensures future flexibility)
- Why this archival model? (long-term preservation, institutional commitment to sustainability)

**Capture specifications to execute:**
- Target PPI and resolution (pixels per inch; total pixel dimensions)
- Bit depth and color space
- Color target type and placement
- Lighting requirements (uniformity, directionality if relevant)
- Delta E target (if applicable)
- File formats (master, derivatives)
- Metadata schema and required fields
- Checksum algorithm (SHA-256 recommended)

## Outputs

**Framework selection summary:**
```yaml
framework:
  digitization_standard:
    name: [FADGI 4-Star | Metamorfoze Preservation | etc.]
    rationale: "[why this standard]"
    capture_specs:
      ppi: [number]
      bit_depth: [8|16]
      color_space: [sRGB | Adobe RGB | ProPhoto RGB]
      color_target: [type and placement]
      delta_e_target: [number if applicable]
      lighting_requirements: "[specifications]"
      file_formats:
        master: [TIFF | JPEG2000 | etc.]
        derivatives: [list]
      metadata_standards: [Dublin Core | PREMIS | etc.]
      checksum_algorithm: [SHA-256]
  
  ethics_framework:
    principles:
      - minimal_intervention
      - reversibility
      - retreatability
      - documentation
      - respect_for_original
      - distinguish_revelation_from_reconstruction
    red_lines:
      - never_overwrite_master
      - never_destroy_original_pixels
      - never_present_reconstruction_as_original
      - never_apply_physical_treatments
  
  archival_model:
    type: [OAIS | simplified]
    preservation_strategy:
      master_format: "[specification]"
      derivative_formats: "[list]"
      storage_strategy: "[primary + backup locations]"
      fixity_schedule: "[how often to verify checksums]"
      migration_schedule: "[format review interval]"
    metadata_schema:
      descriptive: [Dublin Core fields]
      administrative: [PREMIS events]
      technical: [EXIF/IPTC/XMP]
      structural: [METS or simple manifest]
```

**Justification narrative** (2-3 paragraphs): why these choices are appropriate for this artifact and institution.

## Quality Gates

**Must achieve before proceeding:**
1. [ ] A named digitization standard is selected (FADGI or Metamorfoze tier)
2. [ ] Capture specifications are defined (resolution, bit depth, color space, targets)
3. [ ] Conservation ethics are explicitly acknowledged (minimal intervention, reversibility, documentation)
4. [ ] Archival model is chosen (OAIS or simplified)
5. [ ] Format strategy is defined (master format, derivatives, metadata)
6. [ ] Rationale is documented (why these choices, not just what)
7. [ ] Red lines are stated explicitly (never cross these)

**Validation checks:**
- Standard is appropriate for artifact value and goal
- Specs are achievable with available equipment (if not, note limitation)
- Ethics framework is comprehensive (not just "be ethical")
- Archival strategy is realistic (not over-promising)

## Error Handling

**If standards documents are unavailable:**
- Use cached specifications from SECOND-KNOWLEDGE-BRAIN
- Flag that standards may be outdated
- Proceed with last-known specs; note limitation in output

**If artifact profile suggests higher standard than equipment can achieve:**
- Note the limitation explicitly
- Recommend highest feasible level
- Flag that output may not meet repository requirements

**If institutional policy conflicts with ethics:**
- Flag as blocker; ethics are non-negotiable
- Recommend policy review before proceeding

## Fallback Mechanisms

- Use SECOND-KNOWLEDGE-BRAIN for cached FADGI/Metamorfoze specs if web unavailable
- Default to 4-star FADGI or Metamorfoze Preservation for high-value items if uncertain
- Default to OAIS if institution has preservation mandate; simplified for access-only projects

## Notes for Next Stage

- Pass framework to condition-assessor
- Capture specs inform imaging recommendations (e.g., if no multispectral, flag limitation)
- Ethics framework gates all future decisions (restoration steps must be reversible)
