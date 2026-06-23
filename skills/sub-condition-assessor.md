---
name: sub-condition-assessor
description: Diagnoses degradation types, assesses information loss vs. recoverability, and recommends imaging techniques (multispectral, IR, UV, RTI) matched to degradation characteristics and material constraints.
---

## Purpose
Translate condition observations into technical imaging recommendations that maximize information recovery while respecting artifact fragility. The right imaging technique can reveal under-drawings, faded ink, retouching, or surface details that inform restoration decisions.

## Procedure

### Step 1 — Degradation Classification
Organize observed condition issues into diagnostic categories.

**Surface degradation (external to image-bearing layer):**
- **Accretions**: surface dirt, soot, grime, candle wax, adhesives, insect debris, mold residues
- **Abrasions**: surface scratches, scuffing, rubbing
- **Planar deformation**: cockling, creases, warping, buckling
- **Tears/losses**: mechanical damage to support
- **Biological**: active/inactive mold, insect damage (bore holes, frass)
- **Previous interventions**: tape residues, old repairs, overpaint, varnish

**Image layer degradation (affects content):**
- **Fading**: light-induced pigment/ink fading (often recoverable via spectral imaging)
- **Discoloration**: overall yellowing, acid burn, foxing (brown spots), silver mirroring (photographs)
- **Flaking/lifting**: pigment or ink layer detaching from support
- **Media loss**: missing ink/pigment (information loss, not obscuration)
- **Bleeding/offset**: water-soluble inks migrated; offset from opposite page
- **Ink corrosion**: iron gall ink burn-through (active deterioration)

**Chemical/structural instability:**
- **Acid migration**: discoloration spreading from acidic materials
- **Oxidation**: silver oxidation in photographs, metal thread corrosion
- **Glass deterioration**: daguerreotype glass corrosion, ambrotype deterioration
- **Acetate decay**: vinegar syndrome in film (vinegar smell, shrinkage, brittleness)

### Step 2 — Information Loss vs. Recoverability Assessment
Distinguish what is gone from what is obscured.

**Irreversible information loss (cannot be recovered digitally):**
- Complete physical loss of media (e.g., ink scraped away, pigment flaked off and lost)
- Burned or abraded areas where media was destroyed
- Torn sections where content is missing
- Severe ink corrosion that has eaten through paper
- Silver mirroring that has obliterated image detail

**Recoverable information (obscured but present):**
- Faded ink/pigment (still present, just low contrast) → multispectral/IR
- Under-drawings or pentimenti (covered by paint layers) → IR, multispectral
- Retouching or overpaint obscuring original → IR/UV, multispectral to differentiate
- Varnish discoloration → UV to reveal surface details beneath
- Surface dirt or grime → not an imaging problem; cleaning is physical (defer to conservator)
- Foxing or mold stains (obscuring but not destroying media) → color correction may help

**Partially recoverable:**
- Water damage with tide lines (some areas lost, some recoverable)
- Insect damage along edges (loss plus adjacent distortion)

### Step 3 — Imaging Technique Mapping
Match degradation to appropriate imaging modalities.

**High-resolution RGB (baseline for all projects):**
- **Purpose**: overall documentation, color reference, visual record
- **Specs**: follow FADGI/Metamorfoze from framework-selector
- **Use case**: all projects, always capture first

**Multispectral/Hyperspectral Imaging:**
- **Purpose**: reveal faded ink, under-drawings, differentiate materials
- **How it works**: captures reflected light at specific wavelengths; different inks/pigments reflect/absorb differently
- **Best for**:
  - Faded iron gall ink (often visible in IR)
  - Carbon ink under-drawings (IR penetrates upper layers)
  - Palimpsests (text written over erased text)
  - Differentiating ink types (iron gall vs. carbon vs. modern)
  - Recovering water-damaged or faded text
- **Wavelengths**:
  - Visible (400-700nm): standard RGB
  - Near-IR (700-1000nm): penetrates upper layers, reveals under-drawing
  - UV-reflectance (365nm): reveals fluorescence differences, retouching
- **Output**: image stack at each wavelength; false-color composites to highlight differences

**Infrared (IR) Photography:**
- **Purpose**: see beneath paint layers; reveal under-drawings, pentimenti
- **Best for**: paintings (oil, tempera), manuscripts with faded ink, palimpsests
- **Limitations**: does not penetrate very thick or opaque pigments (lead white, vermilion)
- **Equipment**: IR-sensitive camera, IR filter, IR lighting
- **Caution**: some materials may be heat-sensitive; use IR LED or filtered visible light to avoid heating

**Ultraviolet (UV) Imaging:**
- **Purpose**: reveal surface details, retouching, varnish, mold
- **How it works**: UV fluorescence and reflectance; materials fluoresce differently
- **Best for**:
  - Revealing retouching or overpaint (modern paints often fluoresce differently)
  - Visualizing varnish layers and surface texture
  - Detecting mold (certain fungi fluoresce)
  - Identifying repairs (adhesive residues fluoresce)
- **Output**: UV-induced fluorescence image, UV-reflected image
- **Safety**: wear UV-protective eyewear; limit exposure to avoid UV damage to artifact

**RTI (Reflectance Transformation Imaging):**
- **Purpose**: document surface texture and subtle topography
- **How it works**: capture from multiple light directions; software renders surface with interactive lighting
- **Best for**:
  - Impasto (raised paint) in paintings
  - Tool marks, brushwork, surface texture
  - Subtle surface details (impressed seals, drypoint lines in prints)
  - Inscriptions or tooling on covers/boards
- **Equipment**: camera on fixed stand, movable light source (or dome with multiple LEDs), RTI software
- **Output**: interactive RTI file (.ptm or .rti) + static visualizations

**Spectral Reflectance/Colorimetry:**
- **Purpose**: measure color objectively for color correction reference
- **Best for**: color restoration, monitoring fade over time, scientific documentation
- **Equipment**: spectrophotometer or colorimeter with calibrated target
- **Output**: spectral reflectance curves, CIE Lab values

**Macro Photography:**
- **Purpose**: capture fine details (brushwork, pigment particles, paper texture)
- **Best for**: technical study, documentation of media and technique
- **Specs**: high magnification (1:1 or greater), focus stacking if depth-of-field limited

**Transmitted Light (for translucent supports):**
- **Purpose**: see watermarks, structural details in paper/parchment
- **Best for**: watermark documentation, paper structure analysis
- **Setup**: light source behind artifact; artifact on light table or held with clamp

### Step 4 — Equipment Availability Check
Verify recommended techniques are available; flag limitations.

**If recommended imaging is available:**
- Confirm specifications (wavelength range, resolution)
- Note any calibration needs (spectral targets, wavelength calibration)
- Flag capture time considerations (multispectral can be slow)

**If recommended imaging is NOT available:**
- State limitation explicitly
- Note what information may not be recoverable
- Suggest alternatives (e.g., if no multispectral, note that faded ink may not be fully recovered)

### Step 5 — Evidence-to-Preserve Identification
List what must NOT be altered during restoration.

**Historical evidence to preserve:**
- Artist's hand (brushwork, pen strokes, tool marks)
- Under-drawings or pentimenti (reveal process)
- Original color choices (even if faded)
- Period inscriptions, annotations, marginalia
- Signs of use or wear that tell object's story (e.g., wax seals, folds)
- Original binding or mounting (if historically significant)

**Distinguish from damage that obscures evidence:**
- Surface dirt is damage; removing it (digitally) reveals evidence
- Varnish discoloration obscures; digital color correction reveals
- Foxing stains obscure; digital inpainting may restore appearance (but label as reconstruction)

**Reconstruction vs. revelation guidelines:**
- **Revelation**: recovering information that exists but is obscured (e.g., faded ink made legible via multispectral) — present as recovery, not interpretation
- **Reconstruction**: inventing appearance of missing or destroyed areas (e.g., inpainting losses) — label clearly as interpretive, keep separate from revelation

### Step 6 — Fragility & Handling Precautions
Flag any condition that requires special handling during imaging.

**Handle-with-care flags:**
- **Flaking media**: avoid vibration; use gentle support; do not place face-down
- **Fragile support**: tears, brittle paper; use rigid support; avoid flexing
- **Light sensitivity**: fugitive watercolors, photographs (daguerreotypes, tintypes); minimize exposure; use LED instead of strobe if heat is concern
- **Moisture sensitivity**: water-soluble inks; avoid humidity changes; do not use water-based cleaning (defer to conservator anyway)
- **Planar distortion**: cockled or warped pages; use gentle flattening (physical treatment by conservator) or capture as-is with multiple focal planes

**Imaging constraints due to fragility:**
- May need to limit capture angles (no backside imaging if fragile)
- May need to minimize light exposure (low light sensitivity)
- May need to avoid certain lighting (no transmitted light if brittle paper)

## Outputs

**Condition assessment summary:**
```yaml
condition:
  degradation_catalog:
    - category: [surface | image_layer | chemical_structural]
      issue: "[standard conservation term]"
      severity: [minimal | moderate | severe | critical]
      stability: [stable | deteriorating | actively_degrading]
      extent: "[localized/generalized extent]"
  
  information_assessment:
    irreversible_loss:
      - "[areas or content that cannot be recovered]"
    recoverable:
      - "[content that is obscured but present]"
    partially_recoverable:
      - "[areas with mixed loss/recoverability]"
  
  imaging_recommendations:
    required:
      - technique: [high_res_rgb | multispectral | ir | uv | rti | macro | transmitted_light]
        purpose: "[what this reveals]"
        justification: "[why this technique for this degradation]"
        alternatives: "[if this is unavailable]"
    optional:
      - "[techniques that would be helpful but not essential]"
    unavailable_flagged:
      - technique: "[recommended but unavailable]"
        impact: "[what information may be lost]"
        workaround: "[if any]"
  
  evidence_to_preserve:
    - "[list of features that must not be altered during restoration]"
  
  fragility_flags:
    - "[handling precautions needed during imaging]"
  
  reconstruction_boundaries:
    revelation_vs_reconstruction:
      guidance: "[how to distinguish recovery from invention in this specific case]"
```

**Summary narrative**: key degradation issues; which imaging techniques are most critical and why; what evidence must be preserved; any handling precautions.

## Quality Gates

**Must achieve before proceeding:**
1. [ ] All observed degradation is classified into categories
2. [ ] Information loss is distinguished from recoverable obscuration
3. [ ] At least one imaging technique is recommended (baseline RGB is minimum)
4. [ ] Recommended techniques are matched to specific degradation types with justification
5. [ ] Equipment limitations are flagged explicitly (no silent downgrades)
6. [ ] Evidence-to-preserve is identified
7. [ ] Fragility/handling precautions are noted
8. [ ] Reconstruction vs. revelation guidance is articulated

**Validation checks:**
- Recommended imaging is appropriate to degradation type (e.g., IR for faded ink)
- Recommended imaging is feasible given equipment (or limitation is flagged)
- Master preservation is not compromised by imaging choices (e.g., no harmful lighting)

## Error Handling

**If degradation type is unknown or ambiguous:**
- Request additional description or reference images
- Make conservative assumption (assume worst case: recommend comprehensive imaging)

**If imaging technique is not available:**
- State limitation explicitly
- Document what may not be recoverable
- Do not silently downgrade

**If artifact is too fragile for recommended imaging:**
- Prioritize safety over information
- Recommend less invasive alternatives
- Flag that some information may be sacrificed for artifact safety

## Fallback Mechanisms

- If multispectral unavailable, note that faded ink may not be fully recoverable; proceed with high-res RGB and color correction
- If RTI unavailable, document surface texture with raking-light RGB capture
- If degradation is unknown, recommend comprehensive baseline RGB + IR (if available) as conservative approach

## Notes for Next Stage

- Pass imaging recommendations to restoration-planner
- Evidence-to-preserve list constrains allowable restoration edits
- Fragility flags affect execution plan (handling procedures)

---

# Degradation → Imaging Mapping Table

| Degradation Type | Primary Imaging Technique | Secondary/Complementary | What It Reveals |
|------------------|---------------------------|--------------------------|-----------------|
| Faded ink/pigment | Multispectral, IR | High-res RGB | Legibility of faded content; under-drawings |
| Under-drawings/pentimenti | IR | Multispectral | Preliminary sketch beneath paint layers |
| Varnish discoloration | UV, multispectral | High-res RGB | Surface details beneath yellowed varnish |
| Retouching/overpaint | UV, IR | Multispectral | Differentiation of original from later additions |
| Surface dirt/grime | High-res RGB | — | Visual record for digital cleaning (color correction) |
| Mold/foxing stains | Multispectral, UV | High-res RGB | Distinguish stains from underlying content |
| Tears/losses | High-res RGB, macro | RTI (for texture at edges) | Extent and nature of losses; edge detail |
| Flaking/lifting media | Macro, high-res RGB | — | Documentation for monitoring; treatment planning |
| Impasto/surface texture | RTI | Raking-light RGB | 3D surface characteristics; brushwork |
| Watermarks | Transmitted light | High-res RGB | Paper structure, watermark design |
| Inscriptions/tooling | RTI, raking-light RGB | Macro | Incised or impressed marks |
| Insect damage | High-res RGB, macro | — | Documentation of extent and pattern |
| Silver mirroring | High-res RGB, spectral | — | Documentation; may not be recoverable |
| Foxing | Multispectral | High-res RGB | Distinguish stain from content |
| Acid burn/ink corrosion | Transmitted light, high-res RGB | IR (if ink remains) | Transparency of damage; any remaining ink |
| Wax/adhesive residues | UV | High-res RGB | Location and extent of residues |
| Cracks/craquelure | High-res RGB, RTI | Macro | Pattern and depth of cracking |
