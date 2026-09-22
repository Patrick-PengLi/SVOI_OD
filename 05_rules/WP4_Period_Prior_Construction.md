**Work Package 4: Period Prior Construction**

Olympic Dam Sequential-VOI Program, Fleet Space Technologies and
Stanford Mineral-X

*Scope of work for the postdoctoral researcher. Draft for discussion,
August 2026.*

**1. Purpose**

The replay of WP7 is a counterfactual only if the policy chooses under
the information state of its time. A prior that contains knowledge
derived from Olympic Dam after 1975 makes every policy look good, and
the replay then proves nothing. The difficulty is specific: the deposit
belongs to a class, IOCG, that did not exist as a concept in 1975, and
the exploration team held a different and, as it turned out, incorrect
genetic model. WP4 builds the starting prior from documents that predate
the first action, so that the truth has non-zero probability under the
prior without the prior containing the concept.

Two objects are kept separate throughout. The prior is the belief the
policy uses to choose actions. The truth (WP2) is what outcomes are
scored against, and it is built with everything known today. The policy
computes its expected value under the prior; its realized
cost-to-decision is scored against the truth. Scoring a misspecified
policy against the true geology is the experiment.

**2. Three Rules**

- **Citation gate.** Every scenario class, property range, and class
  weight in the period prior carries a citation to a document that
  predates the first action. A class without a citation does not enter
  the prior. A dense iron-oxide body is admissible because
  Middleback-type ores at Iron Knob had been mined since 1900. An IOCG
  breccia complex with copper, uranium, gold, and rare earths in a
  hematite matrix is inadmissible because no one had written it down.

- **Pre-registered residual.** The prior includes a generic residual
  class so that the truth does not sit at zero probability. Its geometry
  and grade-tonnage ranges come from a rule and a source written and
  dated before any realization is scored against Olympic Dam. A residual
  adjusted afterward is leakage under another name.

- **Data-driven expansion.** When an intersection has low likelihood
  under every existing class, the sequential policy adds a class
  parameterized only from observations made up to that stage. The new
  class knows what RD1 intersected. It does not know what RD10 will
  intersect. This rule reproduces the reinterpretation WMC made in late
  1975 and makes the cost of recognizing what was found a measured
  quantity.

**3. Tasks**

**Task 1: Fix t0 and inventory the information state**

The survey that led to the discovery must be a priced action, so the
clock starts before WMC's infill gravity. Set t0 at the take-up of the
Stuart Shelf ground, about 1972 to 1973 \[CHECK\], from the WP1
historical reconstruction. Inventory what existed at t0: the BMR
regional gravity and its station spacing, the BMR aeromagnetics and line
spacing, the 1:250,000 geology sheets, every stratigraphic and water
bore through the cover in the regional window with its logged cover
thickness, Haynes's sediment-hosted copper concept as stated in the WMC
reports, and O'Driscoll's lineament maps. Record the document and date
for each item. Nothing dated after t0 enters the prior except through
the expansion rule.

**Task 2: Physical-setting layer**

The survey likelihoods respond to physical properties, so the prior is
expressed in the space the instruments measure. Build cover thickness as
a spatial field across the regional window: a trend from the t0 bores
and wide uncertainty between them, about 150 to 600 m \[CHECK\]. Assign
cover properties as known in 1975: density 2.4 to 2.6, non-magnetic,
conductive where saturated. Represent basement as undifferentiated
Gawler Craton crystalline rock and overlay the lineament framework as a
structural field. This layer carries no genetic content.

**Task 3: Source-class layer under the citation gate**

Each geophysical anomaly in the regional window receives a discrete
source class. Extract from the pre-t0 and pre-drilling WMC reports the
candidate sources listed for a coincident gravity and magnetic high
under cover. The classes the record is expected to support, with the
properties each carries:

| **Class**                                          | **Properties and geometry**                                                                                         | **Placeholder weight \[CHECK\]** | **Basis**                            |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------------------|
| **Basalt or mafic volcanic pile**                  | Density 2.8 to 3.0; moderately to strongly magnetic; tabular flows, hundreds of meters thick                        | 0.40                             | Haynes's source rock                 |
| **Mafic to ultramafic intrusion**                  | Density 2.9 to 3.1; magnetic; plug or sill                                                                          | 0.20                             | Standard anomaly source              |
| **Iron formation or iron-oxide body**              | Density 3.0 to 4.5 by iron content; susceptibility from near zero (hematite) to very high (magnetite); lens or body | 0.15                             | Middleback type, Iron Knob           |
| **Magnetite-bearing granitoid or felsic volcanic** | Density 2.65 to 2.75; magnetic; no gravity high                                                                     | 0.10                             | Explains magnetic-only anomalies     |
| **Barren basement density contrast**               | Lithology change or block uplift; density step 0.1 to 0.3                                                           | 0.10                             | Structural alternative               |
| **Residual (Task 5)**                              | Generic geometry; ranges by pre-registered rule                                                                     | 0.05                             | Rule and source dated before scoring |

Property ranges come from petrophysical tables available in 1975
\[CHECK\]. Class weights come from the WMC anomaly-ranking reports,
which are the team's prior written down; the placeholders above stand
until extraction. Record the citation for every class, range, and
weight. Any class the record does not support is dropped, and its
placeholder weight moves to the residual.

**Task 4: Mineralization layer**

The value function needs grade and tonnage, and under the 1975 concept
these are decoupled from the anomaly source: copper sits in reduced
sediments adjacent to the basalt, which acts as donor. Encode this as
Haynes stated it. Add a variable for the presence of reduced host
sediments at the basement-cover contact, with a modest prior, since the
published maps did not show them. Set the probability of economic copper
given class and host presence. Take grade and tonnage under the
sediment-hosted class from what the deposit type looked like in 1975:
the Copperbelt, White Pine, the Kupferschiefer, at 1 to 4 percent Cu and
tens to a few hundred million tonnes \[CHECK\]. Give the iron-body and
intrusion classes small copper expectations from the same era's
knowledge. Apply a multiplicative factor at lineament intersections with
a strength elicited from O'Driscoll's reports rather than assigned.

**Task 5: Residual class by pre-registered rule**

Write the rule first. Generic body geometry; grade and tonnage ranges
from a pre-1975 global compilation of base-metal deposits \[CHECK
source\]. Date the rule and its source, file them with the program
leads, and only then compute how Olympic Dam scores under the residual.
Report that score in the leakage audit.

**Task 6: Model-expansion rule**

Specify the procedure the sequential policy follows when an intersection
has low likelihood under every class. Define the likelihood threshold
that triggers expansion. Define the parameterization of the new class
from the observations to date: intersected lithology, measured density
and susceptibility, assays, and the geometry implied by the hole. Define
how the new class receives prior weight and how it enters the forward
models. Document that the procedure references no knowledge later than
the stage at which it fires.

**Task 7: Assemble the t0 prior ensemble**

Sample class, geometry, and properties for every anomaly in the regional
window, together with the physical-setting fields. Forward-model each
realization against the t0 surveys with the WP3 operators and weight the
realizations by likelihood. The weighted ensemble is the t0 prior. The
prior before RD1 follows when the infill gravity is added as the first
priced action in WP6; this work package delivers the t0 state and the
recipe.

**Task 8: Leakage audit**

A reviewer who did not build the prior checks every class, range,
weight, and rule against its citation and checks the residual score
against the dated rule. Any element without a pre-t0 citation is removed
or moved to the residual. The audit report lists each element, its
citation, and the reviewer's finding.

**Task 9: Labeled modern prior**

Build the IOCG-based prior from current knowledge as a separate object,
labeled as such, for the upper-bound replay of WP7. Keep the same
physical-setting layer and the same forward models so that the
difference between the two replays is attributable to the concept alone.
The difference in cost-to-decision between the period-prior and
modern-prior runs is the value of the geological concept.

**4. Deliverables**

| **Deliverable**                    | **Contents**                                                                                       | **Feeds**     |
|------------------------------------|----------------------------------------------------------------------------------------------------|---------------|
| **t0 information-state inventory** | Every dataset and document available at t0 with dates and citations                                | WP5, WP7      |
| **Prior specification**            | Layers, classes, ranges, weights, mineralization model, each with its citation                     | WP5, WP6, WP7 |
| **t0 prior ensemble**              | Weighted realizations conditioned on the t0 surveys                                                | WP5, WP6, WP7 |
| **Model-expansion rule**           | Threshold, parameterization, and weighting procedure, with documentation of its information cutoff | WP6, WP7      |
| **Leakage audit report**           | Independent check of every element against its citation; residual score                            | Program       |
| **Labeled modern prior**           | IOCG-based prior on the same setting and forward models                                            | WP7           |

**5. Dependencies and Sequencing**

Task 1 draws on the WP1 historical reconstruction and can start as soon
as the pre-drilling WMC reports are indexed. Tasks 2 to 6 run in
parallel after Task 1. Task 7 needs the WP3 forward operators for
gravity and magnetics. Task 8 follows Task 7. Task 9 can run at any time
after Task 2, since it shares the physical-setting layer. The leakage
audit gates the use of the prior in WP5 and WP7.
