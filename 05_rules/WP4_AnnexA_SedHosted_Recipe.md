**WP4 Annex A: Generative Recipe for the Sediment-Hosted Branch**

Olympic Dam Sequential-VOI Program, Fleet Space Technologies and
Stanford Mineral-X

*Annex to Work Package 4, Period Prior Construction. For the
postdoctoral researcher. Draft, September 2026.*

**1. Purpose**

WP4 requires that each concept in the period prior be a sampler that
produces full 3D realizations, and the sediment-hosted branch is the
dominant branch: it carried most of WMC's prior weight and it is the
concept under which every pre-RD1 action was chosen. This annex
specifies that sampler. It defines five generative levels, the
parameters of each level, and the documentary basis for every parameter.
The WP4 rules apply throughout: a parameter enters with a citation to a
document that predates the first action, qualitative statements are
translated by a fixed rule, and the leakage audit checks the result. The
same five-level architecture serves the other branches (Ni-Cu on
intrusions, iron body, VMS) and the modern IOCG prior with different
objects and rules, so nothing in this annex is specific to one branch
except the geology.

The concept being encoded, as Haynes stated it: copper leached from
basalt piles moves through the red-bed aquifer and precipitates where
the fluids meet reduced sedimentary rocks, so ore forms as stratabound
blankets near basalt margins, preferentially at lineament intersections.
The recipe reproduces this belief structure, including its two
consequential properties. The ore body itself is geophysically nearly
invisible at the grades and thicknesses of the analog deposits, so
gravity and magnetics detect the basalt and only drilling resolves the
ore variable. And the ore sits beside the anomaly source, at the
basement-cover contact, so hole placement under this concept tests
contacts and margins.

**2. Rules of Construction**

- **Weighting, never conditioning.** Realizations are generated
  unconditionally from the recipe and then weighted by their likelihood
  against the t0 regional gravity and magnetics through the WP3 forward
  models. Geology builds the prior; geophysics selects within it. The
  basalt-object frequency therefore comes from geological reasoning and
  the Roopena analog. Tuning it to match the observed anomaly count
  would use the gravity map twice, once in the prior and once in the
  weighting, and is prohibited.

- **Translation rule for qualitative statements.** Where an era document
  gives a number, the parameter takes a distribution centered on it.
  Where the document is qualitative (adjacent to, thick basalt,
  favourable structure), the parameter takes the widest range consistent
  with the wording, and the translation is recorded next to the citation
  so the audit can check the reading, and the sensitivity of downstream
  results to the translation is reported.

- **One parameter, one row.** Every parameter appears as one row of the
  citation table (Section 5): parameter, distribution, source document
  with date, translation note, status. The table is the object the
  leakage audit works through. A parameter without a row does not exist.

**3. The Five Levels**

**Level 1: Stratigraphic frame**

Every deeper object hangs off the cover stack, and cover thickness
controls both drilling cost and geophysical response, so the frame comes
first. Build implicit surfaces for the flat-lying Stuart Shelf
succession, Andamooka Limestone, Arcoona Quartzite, Tregolana Shale, the
Pandurra red beds, and the basement unconformity, interpolated from the
t0 stratigraphic and water bores with a gentle regional trend. The bores
sit tens of kilometers apart, so the between-bore variance is wide by
construction, about 150 to 600 m total cover \[CHECK\], and the
unconformity carries its own relief field. Basis: the SA Geological
Survey 1:250,000 sheets and explanatory notes for the Andamooka and
Torrens areas and the logged t0 bores.

**Level 2: Basalt objects**

The basalt pile is the concept's anomaly source and copper donor, so its
geometry statistics drive everything the geophysics can detect. Generate
flow piles as a marked point process on the basement surface: lateral
extents of order 2 to 20 km, stacked-flow thicknesses of 50 to 300 m
\[CHECK both\], elongation along structure. Intensity is elevated along
the O'Driscoll lineament network and in inferred structural lows, with
the multiplier elicited from the lineament reports. The one place the
object was observable in 1972 is the Roopena Basalt outcrop on the
southeastern shelf; its mapped dimensions anchor the size distributions.
Basis: Roopena mapping, the WMC targeting memoranda, O'Driscoll's
interpretation.

**Level 3: Redox architecture**

The concept places ore only where reduced rocks exist, and the published
maps of the era did not show reduced facies in the target position, so
this level carries the concept's largest honest uncertainty. Generate a
binary reduced-facies field at and near the basement-cover contact:
modest marginal probability of presence, about 0.1 to 0.3 \[CHECK\],
with spatial structure taken from how reduced facies belts behave in the
analog basins, belts of tens of kilometers containing patches of one to
ten kilometers \[CHECK\]. Basis: the facies descriptions in the few t0
bore logs, and the pre-1975 analog literature for the correlation
structure.

**Level 4: Ore rule**

Ore placement is the concept's core claim, and it is a rule, so it is
encoded as one. An ore blanket forms where three conditions coincide:
distance to a basalt margin below d, about 0 to 10 km \[CHECK from the
targeting memoranda\]; reduced facies present; and the
lineament-intersection factor applied as a multiplier on occurrence
probability. Where the rule fires, place a stratabound lens: thickness 2
to 30 m, grade 1 to 4 percent Cu, tonnage lognormal with median of order
tens of millions of tonnes \[CHECK all three\]. Basis: Haynes's
memoranda for the rule and its reach, and the analog deposits as known
by 1975, the Zambian Copperbelt, White Pine, and the Kupferschiefer, for
the blanket statistics.

**Level 5: Petrophysical attachment**

The forward models consume property volumes, so each realization ends by
mapping lithology and ore to density, susceptibility, and resistivity
with era values and era uncertainty: basalt 2.80 to 3.00 and magnetic,
cover units 2.4 to 2.6 and non-magnetic, conductive where saturated, and
the ore blanket at analog grades close to invisible to gravity and
magnetics. Use the density contrasts the WMC interpreters themselves
assumed when modeling the anomalies, with the era textbooks (Dobrin;
Grant and West; Parasnis) as backup \[CHECK values\]. Shear velocity
receives no era value, because none existed; under the period prior the
seismic channel is undefined, which is itself the historically correct
state.

**4. Prior Predictive Check**

A recipe can be wrong in a way no single parameter reveals, so the
assembled sampler is checked as a whole before use. Draw districts from
the recipe, forward-model them, and compare the statistics of the
generated anomaly populations, count per unit area, amplitude
distribution, wavelength, against the actual t0 gravity and magnetic
maps of the Stuart Shelf. The comparison is a QC gate. A gross mismatch
sends the recipe back to the geological levels, and the revision is
documented as a numbered change to the citation table. The check is
diagnostic only; it never becomes a fitting loop, per the double-use
rule of Section 2.

**5. Parameter-Citation Table (stub)**

The working ranges below are placeholders for elicitation from the
envelopes. The table is complete when every status reads cited.

| **Level** | **Parameter**                                  | **Working range \[CHECK\]**                         | **Expected source**                                           | **Status** |
|-----------|------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------|------------|
| **1**     | Cover unit thicknesses (per unit)              | Total 150 to 600 m                                  | SA 1:250k notes; t0 bore logs                                 | to elicit  |
| **1**     | Between-bore thickness variance and trend      | Wide; set by bore spacing                           | t0 bore logs                                                  | to elicit  |
| **1**     | Basement unconformity relief                   | Tens of m over km                                   | t0 bores; 1:250k notes                                        | to elicit  |
| **2**     | Basalt object intensity (count per 10,000 km²) | 2 to 10                                             | Roopena mapping; targeting memoranda                          | to elicit  |
| **2**     | Basalt lateral extent; thickness               | 2 to 20 km; 50 to 300 m                             | Roopena mapping                                               | to elicit  |
| **2**     | Lineament intensity multiplier                 | 2 to 5                                              | O'Driscoll reports                                            | to elicit  |
| **3**     | P(reduced facies present at contact)           | 0.1 to 0.3                                          | t0 bore facies logs; analog basins                            | to elicit  |
| **3**     | Reduced-facies belt and patch lengths          | Tens of km; 1 to 10 km                              | Mendelsohn 1961; Kupferschiefer literature                    | to elicit  |
| **4**     | Ore distance to basalt margin, d               | 0 to 10 km                                          | Haynes targeting memoranda                                    | to elicit  |
| **4**     | P(ore \| margin, reduced facies)               | 0.05 to 0.3                                         | Haynes memoranda; analog frequency                            | to elicit  |
| **4**     | Lineament-intersection ore multiplier          | 2 to 5                                              | O'Driscoll reports                                            | to elicit  |
| **4**     | Blanket thickness; grade; tonnage              | 2 to 30 m; 1 to 4% Cu; lognormal, median tens of Mt | Mendelsohn 1961; White Pine papers; Kupferschiefer literature | to elicit  |
| **5**     | Basalt density; susceptibility                 | 2.80 to 3.00; magnetic                              | WMC assumed contrasts; Dobrin; Parasnis                       | to elicit  |
| **5**     | Cover density; resistivity                     | 2.4 to 2.6; conductive where saturated              | WMC reports; era tables                                       | to elicit  |
| **5**     | Ore blanket property contrast                  | Near zero (gravity, magnetics)                      | Computed from grade and thickness                             | derived    |

**6. Documentary Basis**

Four tiers, to be assembled in this order through the WP1 Task 4
extraction.

- **Regional frame:** SA Geological Survey 1:250,000 map sheets and
  explanatory notes (Andamooka, Torrens areas); the BMR gravity and
  aeromagnetic map series and record reports; the logged t0
  stratigraphic and water bores.

- **The concept:** The WMC open-file reports of 1972 to 1975 in the
  SARIG envelopes: Haynes's targeting memoranda, the anomaly
  interpretations with their assumed density contrasts, the anomaly
  rankings, and O'Driscoll's lineament interpretation. These are the
  primary sources for Levels 2, 4, and 5 and for the class weights of
  WP4 Task 3.

- **Object analog:** Roopena Basalt outcrop mapping for the basalt
  object statistics.

- **Ore analogs:** Mendelsohn (1961) for the Copperbelt; the White Pine
  literature; the Kupferschiefer literature \[CHECK editions\]. Only
  editions published before t0 qualify.

Retrospective accounts (Woodall's and Haynes's later papers) serve as
finding aids to locate the era documents. They are never themselves
sources for a parameter, because they were written with knowledge of the
outcome.

**7. Outputs and Interfaces**

- **Deliverable ensemble:** Order 1,000 to 10,000 realizations on the
  coarse regional grid, each carrying lithology, ore, and the Level 5
  property volumes, with likelihood weights against the t0 surveys.
  Local refinement around ranked anomalies is generated on demand from
  the same recipe.

- **Class-agnostic API:** The sampler takes a branch definition as data:
  geometry family, property distributions, mineralization rule. The
  Ni-Cu, iron-body, and VMS branches, the modern IOCG prior, and any
  class created by the model-expansion rule at replay time plug into the
  same interface.

- **Documentation:** The filled citation table, the prior predictive
  check report, and the sampler code and seed conventions, versioned so
  that every downstream VOI figure can name the prior version it was
  computed under.
