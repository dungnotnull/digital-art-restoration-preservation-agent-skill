---
name: sub-requirements-gatherer
description: Captures comprehensive artifact metadata, condition assessment, restoration goals, equipment capabilities, and institutional constraints for digital restoration and preservation workflows.
---

## Purpose
Systematically capture all critical inputs needed to plan an ethical digital restoration and preservation workflow. This is the foundation that guides all subsequent stages — framework selection, condition assessment, restoration planning, and scoring.

## Procedure

### Step 1 — Artifact Identification
Gather the following artifact characteristics:

**Essential fields (must collect):**
- **Artifact Type**: Choose from: painting (oil, acrylic, watercolor, tempera, fresco, other), manuscript/illuminated manuscript, book/bound volume, photograph (daguerreotype, tintype, albumen, silver gelatin, chromogenic, inkjet, other), print (engraving, etching, woodcut, lithograph, screen print, other), drawing (pencil, ink, charcoal, pastel, other), document (parchment, vellum, paper, other), textile/embroidery, 3D object (sculpture, artifact, other)
- **Primary Material**: support (canvas, wood panel, paper, vellum, parchment, fabric, metal, glass, ceramic, other), medium/mediums (pigments, inks, dyes — specify if known), any notable material characteristics (e.g., cotton rag paper, silk thread, gold leaf)
- **Dimensions**: height x width x depth (cm), consider if oversize requires special handling
- **Date/Period**: approximate creation date, century, or period; if unknown, note that
- **Cultural/Provenance Context**: origin, culture, creator (if known), provenance highlights if relevant to treatment decisions

**Helpful context if available:**
- Previous documentation (catalog entries, conservation reports)
- Significance or rarity (affects standard selection)

### Step 2 — Condition Documentation
Document current condition thoroughly:

**Visual degradation observed** (use standard conservation terminology):
- **Surface issues**: scratches, abrasions, accretions/dirt, soot, grime, mold residues, insect damage, candle wax, adhesives, pressure-sensitive tape, other
- **Structural issues**: tears, losses (missing areas), cracks, craquelure, flaking/lifting, planar deformation (cockling, creases, warping), other
- **Chemical degradation**: foxing (brown spots), acid migration, fading/light damage, discoloration/yellowing, oxidation, silver mirroring (photographs), other
- **Previous interventions**: restorations, inpainting, lining, repairs (note if visible/known)
- **Active deterioration**: mold (active/inactive), insect activity, flaking, glass corrosion (daguerreotypes), acetate decay (film), other

**Condition severity assessment**:
- Rate each issue: minimal, moderate, severe, critical
- Note stability: stable, deteriorating, actively degrading
- Identify any fragile areas requiring special imaging precautions

**Handle with care flags**:
- Fragile media (flaking, friable pigments, powdery surface)
- Structural weakness (tears along fold lines, brittle paper)
- Light sensitivity (fugitive pigments, photographs)
- Moisture sensitivity (water-soluble inks, cockled paper)

### Step 3 — Goal Clarification
Understand what success looks like:

**Primary goal(s)** (may select multiple):
- **Digital preservation**: create archival master for long-term preservation
- **Digital restoration**: recover degraded or obscured content
- **Access**: enable web access, exhibition, publication
- **Research**: enable scholarship, analysis, comparison
- **Documentation**: record current condition for monitoring
- **Reconstruction**: visually interpret missing areas (clearly labeled as such)

**Specific questions to answer**:
- What content needs to be revealed or recovered?
- Who are the intended users/audience?
- Is this for publication or internal use?
- Are there copyright or reproduction restrictions?
- Does the output need to meet specific repository requirements?

**What success means for this project**:
- Capture the user's definition of "done"
- Note any specific deliverables requested

### Step 4 — Equipment & Capabilities
Document available imaging and processing resources:

**Capture equipment**:
- **Camera/scanner**: make, model, sensor specifications (megapixels, sensor size), bit depth capability
- **Lens**: make, model, focal length, macro capability
- **Lighting**: type (LED, fluorescent, strobe, natural, other), diffusors, polarization capability
- **Copy stand/rig**: stability, camera mounting, ability to position artwork safely
- **Maximum capture size**: dimensions that can be accommodated

**Special imaging capability** (critical for certain degradation types):
- **Multispectral/hyperspectral**: wavelengths available (UV, IR, visible filters), resolution
- **Infrared (IR)**: ability to capture under-drawing, faded ink
- **Ultraviolet (UV)**: ability to reveal retouching, varnish, mold
- **RTI (Reflectance Transformation Imaging)**: capability for surface texture documentation
- **Spectrophotometer/colorimeter**: for color measurement
- **Microscopy**: for detail documentation

**Processing capabilities**:
- Software available (Adobe Photoshop, GIMP, specialized image processing)
- File format support (TIFF, JPEG2000, DNG, RAW)
- Color management capability (monitor calibration, printer profiling)
- Storage capacity and backup systems

**Limitations**:
- Budget constraints affecting approach
- Time constraints for digitization or processing
- Access to specialized equipment or facilities

### Step 5 — Institutional & Ethical Constraints
Document boundaries and requirements:

**Institutional policies**:
- Digitization standards the institution follows (if any)
- Approval requirements for treatment decisions
- Accession or deaccession policies relevant to treatment
- Rights and reproductions policies

**Legal/ethical considerations**:
- Copyright status and reproduction rights
- Cultural sensitivity or repatriation considerations
- Sacred or ceremonial use restrictions
- Indigenous community consultation requirements
- Data sovereignty or Traditional Knowledge Labeling (TK Labels)

**Conservation ethics alignment**:
- Confirm understanding: digital restoration is complementary to, not a replacement for, physical conservation
- Physical treatment requires qualified conservator
- Digital interventions must be reversible and documented

**Privacy/sensitivity**:
- Any content that should be restricted from public access
- Culturally sensitive materials requiring restricted access

## Outputs

**Structured artifact profile:**
```yaml
artifact:
  type: [string]
  material: [string]
  dimensions: "[H x W x D, cm]"
  date_period: "[string]"
  cultural_context: "[string]"

condition:
  degradation_observed:
    - type: [string]
      severity: [minimal|moderate|severe|critical]
      stability: [stable|deteriorating|actively_degrading]
  fragility_flags:
    - [string]
  handle_with_care:
    - [specific_precautions]

goal:
  primary:
    - [digital_preservation|digital_restoration|access|research|documentation|reconstruction]
  success_definition: "[string]"
  intended_use: "[string]"
  intended_audience: "[string]"
  deliverables_requested: "[list]"

equipment:
  capture:
    camera: "[make/model/specs]"
    lens: "[make/model]"
    lighting: "[type/capability]"
    max_capture_size: "[dimensions]"
  special_imaging:
    multispectral: "[yes/no + details]"
    infrared: "[yes/no + details]"
    ultraviolet: "[yes/no + details]"
    rti: "[yes/no + details]"
    other: "[details]"
  processing:
    software: "[list]"
    formats_supported: "[list]"
    color_management: "[yes/no]"
  limitations:
    budget: "[constraints]"
    time: "[constraints]"
    access: "[constraints]"

constraints:
  institutional_policies: "[string]"
  copyright_status: "[string]"
  cultural_considerations: "[string]"
  ethics_understood: true
  physical_conservator_required: "[if yes, describe]"
  access_restrictions: "[if any]"
```

**Summary narrative** (2-3 sentences): artifact overview, key condition issues, primary goal, equipment context.

## Quality Gates

**Must achieve before proceeding:**
1. [ ] Artifact type and material identified
2. [ ] Condition documented with at least major degradation types and severity
3. [ ] Primary goal(s) clearly defined (not just "fix it")
4. [ ] Equipment capabilities cataloged (including what's NOT available)
5. [ ] Institutional constraints noted
6. [ ] Physical conservation boundary acknowledged (digital scope confirmed)
7. [ ] Culturally sensitive content flagged if present

**Red flags that require clarification before proceeding:**
- Goal is ambiguous or unrealistic (e.g., "make it look new" without ethical bounds)
- Equipment insufficient for stated goal (e.g., multispectral needed but unavailable)
- Physical treatment requested (defer to conservator)
- Cultural sensitivity or repatriation issues not addressed
- Copyright or reproduction restrictions unaddressed

## Error Handling

**Missing information:**
- If artifact type unknown → ask clarifying questions or request photo
- If condition not documented → explain why this matters (affects imaging decisions)
- If goal unclear → present options and ask user to prioritize

**Conflicting inputs:**
- Equipment insufficient for goal → propose alternatives or note limitation explicitly
- Goal conflicts with ethics (e.g., overwriting original) → halt and explain ethical boundary

**Scope creep:**
- If user requests physical treatment → redirect to qualified conservator, keep scope digital
- If user requests unethical digital intervention → cite conservation ethics and refuse

## Fallback Mechanisms

If user cannot provide complete information:
- Make reasonable assumptions based on artifact type
- Note assumptions explicitly in outputs
- Flag for verification in later stages

## Notes for Next Stage

- Pass all captured data to framework-selector
- Highlight any equipment limitations that will affect standard selection
- Note any degradation types that require specialized imaging (for condition-assessor)
