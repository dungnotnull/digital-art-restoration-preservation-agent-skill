---
name: sub-restoration-planner
description: Plans reversible, non-destructive digital restoration steps on derivatives and designs comprehensive long-term archival strategy including formats, metadata, fixity, and OAIS preservation.
---

## Purpose
Create a step-by-step digital restoration workflow that respects conservation ethics (reversibility, documentation) and a preservation strategy that ensures the digital assets remain accessible and authentic for decades.

## Procedure

### Step 1 — Master-Derivative Discipline
Establish the foundational file structure.

**Master file (untouched, archived):**
- Never edit this file directly
- Archive as captured from digitization (with color profiles embedded)
- Store in preservation format (TIFF or JPEG2000 lossless)
- This is the reference of record; all derivatives stem from it

**Derivative workflow files (for restoration):**
- Working copies created from master
- All edits happen here; master remains pristine
- Use non-destructive editing techniques (layers, masks, adjustment layers)
- Save layered files (PSD, XCF) to preserve edit history

**Access/Delivery files (for distribution):**
- Flattened, compressed versions for web or print
- Generated from restored derivative, not from master
- Different versions for different uses (web JPEG, print TIFF, etc.)

**File naming convention (consistent and clear):**
```
[artifactID]_master.tif                    # Untouched master
[artifactID]_working_v01.psd               # Working file with layers
[artifactID]_restored_v01.tif              # Flattened restored derivative
[artifactID]_access_web.jpg                # JPEG for web
[artifactID]access_print.tif              # TIFF for print publication
```

### Step 2 — Restoration Step Planning
Plan each intervention with reversibility and documentation in mind.

**Non-destructive editing techniques:**
- **Adjustment layers**: brightness/contrast, curves, hue/saturation, color balance — always on layers, never applied directly
- **Layer masks**: paint in or out effects; mask is editable
- **Smart objects / filters**: apply effects non-destructively; can re-edit later
- **Duplicate layers**: work on copy, keep original for reference
- **History snapshots**: save milestones before major edits

**Step categories (in recommended order):**

1. **Global corrections (affect entire image):**
   - **Color correction**: adjust white balance, remove overall color cast
     - Use color target (if available) as reference
     - Use curves or levels; save as adjustment layer
     - Document reference: "neutral gray patch from ColorChecker"
   - **Exposure/brightness**: correct under/over-exposure from capture
   - **Noise reduction**: if ISO noise is visible, apply selectively to flat areas
   - **Sharpening**: mild capture sharpening to compensate for digitization softness

2. **Local corrections (affect specific areas):**
   - **Spot healing/clone** for dust spots, small scratches: use healing brush or clone tool on separate layer
   - **Dodge/burn** for local contrast: use overlay layer with black/white painting
   - **Selective color** for faded areas: target specific color ranges
   - **Content-aware fill** for minor losses (use cautiously; document as reconstruction)

3. **Revelation (recovering obscured information):**
   - **Multispectral processing**: if multispectral captures available, blend wavelengths to enhance faded ink
   - **Channel mixing**: extract IR or UV channels to reveal under-drawings; composite with visible
   - **Dehazing**: reduce atmospheric or varnish haze (if digital analog)
   - **Contrast enhancement**: for faded ink or low-contrast areas (document parameters)

4. **Reconstruction (interpretive, must be labeled):**
   - **Inpainting losses**: fill in missing areas based on surrounding context
     - Use content-aware or manual inpainting
     - Save on separate layer named "reconstruction_layer"
     - Document as reconstruction: "filled losses based on extrapolation from adjacent pattern"
   - **Tear repair**: digitally mend torn edges (align and fill gaps)
   - **Missing corner reconstruction**: if border or corner is lost, reconstruct based on symmetrical elements if appropriate
     - Always label as "interpretive reconstruction"
     - Keep reconstruction layer separate; can be toggled on/off

5. **Dewarping/rectification (if needed):**
   - **Perspective correction**: if camera angle caused distortion
   - **Dewarping**: if page is curved or cockled, use software to flatten (document transformation)
   - **Keystone correction**: for skewed captures

**Documentation for each step:**
- **What**: operation performed (e.g., "adjusted brightness +15 using curves")
- **Why**: rationale (e.g., "to compensate for underexposure; histogram shows peak at 180 instead of 255")
- **Parameters**: specific values (e.g., "curves: input 120, output 140")
- **Layer name**: descriptive layer name for future editability
- **Reference**: if referenced to color target or standard, note which

**Step log template:**
```
Step 1 — Global color correction
- What: Curves adjustment layer; slightly lifted shadows
- Why: Histogram shows shadows clipped at 20; detail recoverable
- Parameters: Input 20→40, midtone unchanged, highlights unchanged
- Layer: "color_correction_curves"
- Reference: Neutral patch from ColorChecker (target L* 50, achieved L* 48)

Step 2 — Dust spot removal
- What: Spot healing brush on 43 small dust spots in upper right corner
- Why: Capture dust on sensor; obscures detail
- Parameters: Healing brush, radius 5px
- Layer: "dust_removal_healing"
- Before: [screenshot reference]
- After: [screenshot reference]
```

**Revelation vs. reconstruction labeling:**
- **Revelation** (recovering existing info): present as "enhanced legibility" or "spectral enhancement"
- **Reconstruction** (inventing missing info): present as "interpretive reconstruction" and keep on separate, clearly labeled layer

### Step 3 — Quality Control & Validation
Plan validation checks to ensure restoration is faithful.

**Validation checkpoints:**
- **After global corrections**: compare to color target; check histogram for clipping
- **After local corrections**: zoom to 100% and review edges; no halos or artifacts
- **After reconstruction**: toggle reconstruction layer on/off; confirm reconstruction is plausible and documented
- **Final check**: compare to master; confirm no unintended alterations

**Fidelity checks:**
- **Color target comparison**: if ColorChecker used, compare corrected image to known values (ΔE < 2.0 for 4-star)
- **Detail preservation**: ensure sharpening/noise reduction didn't erase fine detail
- **No overcorrection**: avoid over-saturation, over-sharpening, or plastic-looking results
- **Edge integrity**: check cloned/healed areas for seamless blending

**Ethical check**:
- Master file untouched? Yes
- All edits on derivatives/layers? Yes
- Reconstruction labeled as such? Yes
- Documentation complete? Yes

### Step 4 — Access/Delivery File Generation
Plan output files for different use cases.

**Web access (JPEG):**
- Resolution: 1500-2000 pixels on long edge (balance quality and load time)
- Format: JPEG, quality 85-90
- Color space: sRGB (web standard)
- Metadata: embed Dublin Core, rights statement
- Watermark: optional; if used, keep subtle and non-destructive to legibility

**Print publication (TIFF or JPEG2000):**
- Resolution: 300-600 PPI depending on print size
- Format: TIFF (LZW compression) or JPEG2000
- Color space: Adobe RGB or ProPhoto RGB (depending on print requirements)
- Sharpening: output sharpening for specific print size and paper type

**High-resolution access (for researchers):**
- Resolution: full master resolution or near-full
- Format: JPEG2000 lossy (good compression, high quality)
- Color space: match to master (ProPhoto or Adobe RGB)

**IIIF (International Image Interoperability Framework):**
- If institution uses IIIF, generate IIIF manifest and tiles
- Enables zoomable web viewing and API access

### Step 5 — Archival Strategy Design
Plan long-term preservation following OAIS principles.

**Preservation formats:**
- **Master**: uncompressed TIFF (LZW compression acceptable) or JPEG2000 lossless
- **Derivative for restoration**: layered PSD or TIFF with layers
- **Access**: JPEG (web), JPEG2000 (balanced quality/size)

**Metadata schema:**
- **Dublin Core** (descriptive):
  - Title, creator (artist/scribe), date, description, format, subject, identifier, source, language, relation, coverage, rights
- **PREMIS** (preservation):
  - Events (capture, restoration, migration, format validation), agents (software, people), rights
- **Technical** (embedded in file):
  - EXIF: camera settings, capture date, software
  - IPTC: caption, keywords, copyright status
  - XMP: Dublin Core fields, custom schema
- **Structural**:
  - METS: how files relate (master, derivatives, metadata)
  - BagIt: package manifest with checksums

**Fixity and authenticity:**
- **Checksums**: generate SHA-256 checksums for all files on ingest
- **Checksum storage**: store checksums separately (e.g., in sidecar file or database)
- **Verification schedule**: verify checksums annually or after any migration
- **Audit trail**: log every access, migration, or modification event

**Storage strategy:**
- **Primary storage**: institutional server or cloud storage (e.g., S3 Glacier Deep Archive for long-term)
- **Backup storage**: geographically separate backup (different region or institution)
- **Access copy storage**: faster access tier for web delivery
- **Minimum 3 copies**: primary + 2 backups (LOCKSS principle: Lots Of Copies Keep Stuff Safe)

**Migration planning:**
- **Format monitoring**: watch for format obsolescence (TIFF stable; JPEG2000 evolving; watch for newer codecs)
- **Migration triggers**: format becomes obsolete, software compatibility drops below threshold
- **Migration strategy**: planned migration every 5-10 years; test migration pipeline on sample
- **Migration documentation**: record migration events (from format X to Y, using software Z, date, checksums before/after)

**Access planning:**
- **IIIF**: enable web zoom and API access
- **OAI-PMH**: enable metadata harvesting for discovery
- **CDN**: if high-traffic, use CDN for web delivery
- **Rights management**: embed rights statements (Creative Commons, institution-specific)

### Step 6 — Documentation Plan
Plan how project documentation will be preserved.

**Documentation to preserve:**
- **Project report**: final document summarizing artifact, condition, restoration steps, outcomes
- **Step log**: detailed record of each restoration operation with parameters
- **Technical metadata**: capture settings, software versions, color profiles
- **Decision log**: why specific approaches were chosen (e.g., why FADGI 4-star)
- **Validation results**: fidelity checks, ethics compliance verification

**Documentation format:**
- **PDF**: for project report (human-readable)
- **Plain text (Markdown)**: for step log (machine-readable, future-proof)
- **XML (PREMIS)**: for preservation events
- **JSON/YAML**: for structured metadata (easy to parse)

## Outputs

**Restoration and preservation plan:**
```yaml
restoration_plan:
  master_discipline:
    master_file: "[name and format]"
    storage_location: "[path or URL]"
    checksum: "[SHA-256]"
    notes: "Never edit this file directly"
  
  working_files:
    - name: "[artifactID]_working_v01.psd"
      purpose: "Layered restoration file; all edits on layers"
  
  restoration_steps:
    - step: 1
      category: [global | local | revelation | reconstruction | rectification]
      operation: "[e.g., global color correction using curves]"
      technique: "[non-destructive method, e.g., adjustment layer]"
      parameters: "[specific values]"
      layer_name: "[layer name in working file]"
      rationale: "[why this step]"
      reference: "[if applicable, e.g., color target values]"
    
    - step: 2
      # ... additional steps
  
  validation_checkpoints:
    - after: "[step or category]"
      check: "[what to verify]"
      pass_criteria: "[how to judge success]"
  
  revelation_vs_reconstruction:
    revelation_steps:
      - "[steps that recover existing info]"
    reconstruction_steps:
      - "[steps that invent missing info; labeled as interpretive]"
    guidance: "[how to communicate this difference to users]"

access_files:
  web:
    - name: "[artifactID]_access_web.jpg"
      format: JPEG
      resolution: "[pixels]"
      color_space: sRGB
      purpose: "Web display and download"
  print:
    - name: "[artifactID]_access_print.tif"
      format: TIFF
      resolution: "[PPI]"
      color_space: "[Adobe RGB or other]"
      purpose: "Print publication"
  research:
    - name: "[artifactID]_access.jp2"
      format: JPEG2000
      resolution: "[full or near-full]"
      color_space: "[match to master]"
      purpose: "High-resolution access for scholars"

archival_strategy:
  preservation_formats:
    master: "[TIFF or JPEG2000 lossless]"
    working: "[layered PSD or TIFF with layers]"
    access: "[JPEG, JPEG2000]"
  
  metadata_schema:
    descriptive: [Dublin Core fields]
    administrative: [PREMIS events]
    technical: [EXIF/IPTC/XMP]
    structural: [METS or BagIt]
  
  fixity:
    checksum_algorithm: SHA-256
    checksum_storage: "[sidecar file or database]"
    verification_schedule: "[frequency]"
  
  storage:
    primary: "[location or service]"
    backup_1: "[location or service, geographically separate]"
    backup_2: "[optional additional backup]"
    access_tier: "[faster storage for web delivery]"
  
  migration:
    format_monitoring: "[how format obsolescence will be tracked]"
    planned_migration: "[frequency, e.g., every 5 years]"
    migration_trigger: "[conditions that prompt migration]"
  
  access:
    iif: "[yes/no, if IIIF will be used]"
    oai_pmh: "[yes/no, if metadata will be harvestable]"
    rights_statement: "[e.g., CC BY-NC 4.0 or institution-specific]"

documentation_plan:
  project_report: "[format and storage location]"
  step_log: "[format and storage location]"
  decision_log: "[format and storage location]"
  validation_results: "[format and storage location]"
```

**Summary narrative**: overview of restoration approach; key steps; archival strategy; access provisions.

## Quality Gates

**Must achieve before proceeding:**
1. [ ] Master file discipline established (master never edited)
2. [ ] All restoration steps use non-destructive techniques
3. [ ] Restoration steps are documented with what/why/parameters
4. [ ] Reconstruction vs. revelation is labeled and distinguished
5. [ ] Validation checkpoints are planned
6. [ ] Access/delivery files are specified for each use case
7. [ ] Preservation format strategy is defined (TIFF/JPEG2000)
8. [ ] Metadata schema is chosen (Dublin Core minimum; PREMIS if OAIS)
9. [ ] Fixity strategy is defined (checksums + verification schedule)
10. [ ] Storage strategy has minimum 3 copies (primary + 2 backups)
11. [ ] Migration planning is documented (format monitoring + planned migrations)
12. [ ] Documentation plan is defined (how will this project be documented for the future?)

**Validation checks:**
- No step involves direct pixel editing (all on layers/adjustments)
- Reconstruction is clearly labeled as interpretive
- Master is preserved untouched
- Access files are derivatives, not master

## Error Handling

**If proposed restoration technique is destructive:**
- Halt and revise to non-destructive alternative
- Explain why destructive approach is unacceptable (reversibility requirement)

**If archival format is inappropriate:**
- Redirect to preservation format (no lossy compression for master)
- Explain trade-offs (file size vs. long-term viability)

**If storage strategy is insufficient (e.g., only one copy):**
- Flag as blocker; OAIS requires redundancy
- Recommend minimum 3 copies (primary + 2 backups)

## Fallback Mechanisms

- If institution lacks OAIS capacity, use simplified preservation model (master + checksums + backup)
- If IIIF not available, provide static access files and note limitation
- If metadata expertise limited, use Dublin Core minimum; plan to expand later

## Notes for Next Stage

- Pass restoration plan to scoring-engine for fidelity/reversibility/longevity assessment
- Restoration plan informs execution roadmap (step order, time estimates, software needed)
