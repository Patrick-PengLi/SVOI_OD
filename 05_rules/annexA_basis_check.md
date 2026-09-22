# WP4 Annex A: basis check, level by level

Annex A (`04_reports/papers/WP4_AnnexA_SedHosted_Recipe.md`, copied to
`wp4_prior_state/00_inventory/`) ends each of its five levels with a
"Basis:" sentence. This file takes those sentences one at a time and records,
for every source named, whether it is on disk, where, its date, whether it
is in the t0 state (before 2 May 1975), and what remains to fetch. Filled
levels are dated; open levels carry the basis sentence only. All paths are
inside `01_data/wp1_data/database/wp4_prior_state/` unless marked otherwise.

## Level 1: Stratigraphic frame (checked 2026-09-18, closed 2026-09-21)

Basis (Annex A): "the SA Geological Survey 1:250,000 sheets and explanatory
notes for the Andamooka and Torrens areas and the logged t0 bores."

1:250,000 sheets. ON DISK. `03_geology_sheets_1_250000/`: TORRENS SH 53-16
first edition (1964, 2018d055885) and ANDAMOOKA SH 53-12 first edition
(1966, 2018d055884), both in state, with 150 dpi renders in `renders/`. The
second and digital editions are in the same folder but are truth side only.

Explanatory notes. DO NOT EXIST as a notes booklet. SARIG's ExpNotes series
(2018d040088 to 2018d040138) was walked in order on 2026-09-18 and has no
ANDAMOOKA and no TORRENS entry. The companion text of the first editions is
Johns, R.K., "Geology and mineral resources of the Andamooka-Torrens area":
as RB 61/00102 (19 Oct 1965) ON DISK at
`03_geology_sheets_1_250000/supporting_reports/rb6100102/` (24.2 MB), in
state; as Geological Survey Bulletin 41 (1968, SARIG 2018d037811, 143
scanned pages with an OCR text layer, 16.2 MB) ON DISK since 2026-09-21
(fetched by `fetch_250k_sheets.py`, verified at the catalogue size) at
`annexA_levels/level1_stratigraphic_frame/notes/`, with the extracted text
`Bull_041_Johns_1968_text.txt` beside it. Transmittal dated 16 Aug 1967,
printed 1968; mapping 1959-64; in state. Also in
`supporting_reports/`: SP 029 Handbook of South Australian Geology (1969), RB
74/00144 helicopter geological survey of the Gawler Block (1973), the
Director of Mines annual reports 1955 to 1974-75, mesac10786.

Logged t0 bores. ON DISK. `04_bores_through_cover_regional_window/`: the SA
Geodata details and stratigraphy exports (statewide, snapshot fetched
2026-09-10), the regional and companion window clips with per-interval
stratigraphy, and, from 2026-09-18, the 2 degree buffer search
(`bores_buffer2deg_pre_t0_basement.csv`, its `_strat_intervals.csv`,
`bores_buffer2deg_pre_t0_strat_petroleum.csv`) with the findings note
`bores_buffer2deg_findings.md`. Membership is by drill date before
1975-05-02. Findings: 101 t0 holes in the regional window, deepest 117 m,
none to basement; in the buffer no t0 hole within 82 km logged anything
older than Adelaidean (WOOMERA 1, 1958, Pandurra from 454 m under
Cretaceous and Adelaidean, 82.5 km SW, is the nearest), none within 160 km
reached crystalline basement; the Mount Gunson / Pernatty holes 110 to
170 km SSE give Pandurra tops at 8 to 192 m.

Cross-check. mesac17946 (Trevena 1979, SADME Stuart Shelf drillhole
stratigraphy compilation to 31 Dec 1978) ON DISK in the same folder, with
OCR text (`mesac17946_ENV09395_ocr.txt`, uncorrected) and a plain copy of
the PDF. It is dated 1979 and uses closed-file data, so it is a cross-check,
not a t0 source. Its Andamooka appendix lists only WMC 1976-78 holes with
depths to Pandurra or basement; its Torrens appendix agrees with SA Geodata
to the metre on LD 2-4, MF 1-5 and LY 2. Its text calls the Pandurra
Formation basal Adelaidean cover; SA Geodata codes it Mesoproterozoic. The
buffer CSV carries both readings as flags (`reached_pre_adelaidean`,
`reached_crystalline_basement`); which one is "basement" is a Task 2 ruling.

Consequence for the level. The annex's "interpolated from the t0
stratigraphic and water bores" has no bore inside the window to interpolate
from; the frame rests on the sheets, section A-B on the ANDAMOOKA sheet,
Bulletin 41 and WOOMERA 1, and the 150 to 600 m band is a translation to be
recorded as such in the citation table.

What Bulletin 41 says that the frame can cite (page numbers are the
printed ones; find them in the text file):
- Tent Hill Formation (Woomera Shale Member, unnamed siltstones, Arcoona
  Quartzite Member) "varies from 400 ft. to over 1,200 ft. in thickness"
  (120 to 370 m), the thickest section in Woomera No. 1 bore (p. 28-29).
- Woomera No. 1 bore, Phillip Ponds (Clarence River Basin Oil, BMR PSSA
  Pub. 2, 1960): unnamed siltstones 0-236 ft, Woomera Shale 236-784.5 ft
  (548.5 ft), "Pernatty Grit" 784.5-2,005 ft, 1,220 ft penetrated without
  reaching its base (pp. 25, 29). So the PERIOD reading puts the top of the
  Pandurra equivalent at 784.5 ft = 239 m; the modern SA Geodata log of the
  same hole puts Whyalla Sandstone 239-341 m, Tapley Hill 341-454 m and
  Pandurra from 454 m. The 1968 "Pernatty Grit" interval includes 1,122 to
  1,490 ft of dark-grey laminated siltstone that is now Tapley Hill
  Formation. The frame at t0 must use the 239 m reading (or carry both,
  labelled); the 454 m figure in `bores_buffer2deg_findings.md` is the
  modern one.
- Woomera Shale thins to under 50 ft over the Pernatty Grit "high" at
  Oakden Hills - Mount Gunson - Emu Bluff; "elsewhere the thickness is
  unknown" (p. 29): the period statement of unconformity relief.
- Basement: nearest crystalline outcrop is feldspar porphyry on Lake
  Gairdner, 15 miles west of the map edge; Beda bore's "porphyry" from 439
  to 1,099.5 ft is read by Johns as Callanna (Willouran) lavas, not basement
  (p. 22-23). No hole in the two map areas is described as reaching
  basement.
- Depth to magnetic basement from the 1962 BMR aeromagnetics (Young 1964),
  quoted in the Structure chapter (p. 46): in the central northern part of
  the region (the Andamooka side) anomalies exceed 500 gammas, are rarely
  more than 10 miles long, and "relate to magnetic basement within 2,000 ft.
  of the surface" (610 m), on trends N 40 W, N-S and N 40 E; in the
  southwest, basement within 1,000 ft. This is the one pre-t0 published
  depth-to-basement statement for the deposit's side of the shelf and it
  bounds the 150 to 600 m band from above.

Nothing left to fetch for Level 1. Open work, not data: transcribe the
mesac17946 data-source list (pp. 16-37) for open-file status per hole; the
Pandurra ruling for the basement unconformity (Task 2); decide whether the
frame carries the 1968 or the modern reading of Woomera No. 1.

## Level 2: Basalt objects (checked 2026-09-21; all fetchable sources on disk)

Basis (Annex A): "Roopena mapping, the WMC targeting memoranda,
O'Driscoll's interpretation." Three pieces; folder
`annexA_levels/level2_basalt_objects/<piece>/`.

Piece 1, Roopena mapping. ON DISK since 2026-09-21 (fetched by
`02_code/scripts/fetch_annexA_sources.py`, manifest
`01_data/wp1_data/annexA_sources_manifest.csv`), in `roopena_mapping/`:
- 2019d011394 Roopena 1 Mile geological map, Miles, Johns and Solomon
  (1952), 5.0 MB, catalogue size matched. In state.
- rb6700081 RB 67/00081, Risely, "Geophysical report no. 1 on a gravity and
  magnetic survey of the Roopena Volcanics", dated 1 Nov 1968 on its title
  page, 28 pp., text layer. In state. Content already useful: the survey
  could not resolve the volcanics' thickness because of the regional
  gradient; the two SADM holes put the base of the volcanics at 431 ft
  (131 m, hole 1, over Corunna Conglomerate with chalcopyrite 460-490 ft)
  and beyond 337 ft (103 m, hole 2, over Moonabie Formation); the
  unconformity dips about 30 W near outcrop flattening to 10 W; surface
  specific gravities 2.61 to 3.35 g/cc (means 2.68 north and 2.82 south,
  weathered 2.42), yet the volcanics sit in a gravity trough; magnetic
  pattern irregular. These are Level 2 geometry and Level 5 property
  values with a period citation.
- mesac3667 Jones, "Summary report on the Roopena area, S.M.L. 204" (BHP),
  dated July 1970 on its title page (Env 01174, PDF pp. 229-284 inside the
  331-page envelope for SML 204 1968-70). In state by its writing date.
  Size: the blob serves 32.1 MB against the catalogue's 42.8 MB; the PDF is
  complete by content (start and end markers, 331 pages, the report's
  title, contents, text and plans present), and the fetch script now
  expects the served size. CAUTION: the envelope cover is dated 8/11/1977,
  which reads as its open-file release, i.e. after t0; under the "whose
  information state" ruling (WMC's own vs an idealised explorer with all
  open-file data) this report may be out for an idealised open-file
  explorer at t0 even though it was written in 1970.
- 2018d048833 PORT AUGUSTA SI 53-04 1:250,000 sheet (1968), 8.3 MB,
  catalogue size matched. In state.
Also here, derived from the Level 1 buffer intervals:
`roopena_beda_drillholes_pre_t0_intervals.csv`, 20 pre-t0 holes logging
Roopena, Beda, Backy Point or Wooltana units (Roopena DDH 1-4 1967-68, BHP
RP 1-2 1969, Pacminex EX series 1973-74), 234 to 262 km from the deposit.
Out of state and not fetched: RB 80/00147 (1980), mesac14260 (1993-94).

Piece 2, the WMC targeting memoranda. NOT FOUND in any public archive
(SARIG catalogue and the acquisition index searched; nothing WMC-authored
before t0). This is the S22 gap. `wmc_targeting_memoranda/NOT_FOUND.md`
records the search. Kept beside it, labelled: the EL 190 first quarterly
section 1.2 (nearest admissible, QUALIFIED, and it states the stratiform
Cattle Grid model, not the basalt-donor concept) and Haynes (2006) as a
finding aid only. DECISION NEEDED: request from BHP's archive, or cite the
level to O'Driscoll + EL 190 + Roopena and carry the basalt-donor rule as
testimony.

Piece 3, O'Driscoll's interpretation. ON DISK: GA eCat 79287 (Claoue-Long
2014, CC-BY), the 34 Andamooka / Torrens / Stuart Shelf window sheets with
world files in `odriscoll_interpretation/window_sheets/`, the GA index and
metadata, the SA sheet index, and the two OD4 iv page crops. In state:
OD4 iv only so far (1974 on its face); the other 33 must be dated from
their faces, and OD4 iii and xiv are 1980 redrawings (out). Gap against
the annex: its table expects "O'Driscoll reports"; the package is maps
only, with no written report, so the lineament multiplier has to be
elicited from the maps (for example target density on versus off
lineaments) and recorded under the translation rule.
Findings from the Level 2 notebook (2026-09-21,
`02_code/notebooks/wp4_level2_basalt_objects.ipynb`):
- Piece 1: the 1952 Roopena 1-mile sheet's legend has NO volcanic unit (the
  ground at Roopena H.S. is Qra alluvium); the object is mapped on the 1968
  PORT AUGUSTA sheet as Pcr ROOPENA VOLCANICS: 7.5 km2 main patch (4.7 km
  N-S x 3.6 km E-W, long axis 157) + two slivers = 8.6 km2, 257 km from the
  deposit; thickness 75-141 m in Roopena DDH 1-4 and BHP RP 1-2 (Risely:
  131 m and >103 m); SG median 2.80, 7 of 15 inside 2.80-3.00. Risely p. 19
  proposes copper "immediately beneath the volcanics".
- Piece 2: memoranda text not found; BUT two WMC 1974 targeting plans survive
  among O'Driscoll's sheets: OD6 iv (Sept 1974 plan for the target-selection
  meeting 30/9/74-5/10/74; BLUE T.O'D 1974 targets in state, RED D.McP.D
  targets are 1976 and out) and OD7 i (Sept 1974 exploration plan with a WMC
  proposed drill hole). NOT_FOUND.md updated.
- Piece 3: all 34 window sheets dated from their faces
  (`odriscoll_window_sheet_dates.csv`): in 6 (OD4 ix 1971; OD4 iv, OD4 xxxii,
  OD5 iii, OD7 v 1974; OD7 i Sept 1974), partly 6 (incl. OD6 iv), out 15,
  undated 7. Correction to the September memory: OD7 i is Sept 1974, not
  2004; OD4 xxx is the 1976 D.McP.D assessment. 20 blue 1974 targets on OD6
  iv transcribed (`odriscoll_OD6iv_1974_blue_targets.csv`, 16 matched on the
  scan, 4 by eye), union 1,728 km2 = 5.4% of the two sheets, so a map-based
  multiplier is bounded above by 1/f = 18; the deposit lies in TOD74-14.
  O'Driscoll's 1983 lineament-control statistic (OD6 v/vi) is out of state.

## Level 3: Redox architecture (checked 2026-09-21; folder built)

Basis (Annex A): "the facies descriptions in the few t0 bore logs, and the
pre-1975 analog literature for the correlation structure."

Two pieces. What the level has to set: a binary reduced-facies field at and
near the basement-cover contact, marginal presence about 0.1 to 0.3, belts
of tens of km holding patches of 1 to 10 km.

Piece 1, facies descriptions in the t0 bore logs. On disk.
- SA Geodata LITHO export (fetched 2026-09-21), screened by
  level3_facies_screen.py: 9,766 intervals in 732 pre-t0 buffer holes, of
  which 9,364 intervals in 708 holes carry a logging date before t0. These
  are the t0 bore logs. Redox classes (pre-t0 logged): 3,839 oxidised,
  1,320 mixed, 1,168 reduced, 3,037 no redox word; 273 holes have at least
  one reduced interval. Only 4 of the 708 holes lie in the regional window
  ("the few t0 bore logs"). Of the 221 holes whose strat log reaches
  crystalline basement, 69 have a pre-t0 litho log.
- SA Geodata STRAT export: 3,656 intervals in 1,670 holes, but only 30 carry
  a logging date before t0; the rest are 1990+ Mines and Energy SA
  compilations, a later translation. Used for the contact position only.
  Some logging dates precede the drill date (Mount Woods 3, 4, 7).
- Contact intervals (lowest strat cover interval above pre-Adelaidean rock):
  Pandurra as basement, 347 holes: 64 reduced, 10 mixed, 19 oxidised, 211
  none, 43 no cover logged. Pandurra as cover, 221 holes: 16 reduced, 2
  mixed, 14 oxidised, 147 none, 42 no cover.
- Bulletin 41 (Johns 1968): period facies statements (Woomera Shale;
  Woomera 1 dark-grey pyritic siltstone; Mount Gunson "Origin of Ore").
- Mount Gunson sub-reports: SARIG catalogue queried (1,314 records;
  annexA_catalogue_level3.csv). 28 sub-reports in the envelopes dated
  (catalogue or OCR of their pages; level3_mount_gunson_subreport_dates.csv):
  18 before t0, 3 after, 7 unresolved. The 18 are cut to their page ranges
  by level3_extract_pages.py (38 MB), including Woocalla facies variations
  (May 1974), Genesis of Mount Gunson deposits (Oct 1974), Pernatty Lagoon
  1973 hole table, Curtis petrography 1971-75, Warne bore analyses 1972,
  and RB 74/00135 (Knight 1974, Stuart Shelf geology). Unresolved and after
  items are left out.
- Round 2 fetched 2026-09-21: RB 65/00068 Pandurra prospect (1969), RB
  60/00004 heavy metals in Cambrian and Marinoan shelf sediments (1965), RB
  18/00119 (1941); Env 00674 (1965-66 annual report with Geology of the
  Pernatty Lagoon area; the envelope has 86 pages, the catalogue range runs
  to p. 94, so the extract is pp. 35-86); drill-log envelopes 06669, 06624,
  06626 (Pacminex / Mount Gunson Mines logs 1970-72, dated from contents
  pages; the p. 2 index sheet of 06669 is Jan 1976). All before t0; the
  sub-report table now has 22 before, 3 after, 7 unresolved.

Piece 2, pre-1975 analog literature. Mostly on disk.
- Liege 1974 volume (Bartholome ed.), 10 papers fetched and OCR'd: Rentzsch
  (Kupferschiefer), Binda and Mulgrew, Annels (Copperbelt), Cahen, Cailteux,
  Lefebvre (Shaba), Brown (northern Michigan, White Pine), Johnson (Permian
  copper shales), Kirkham (Canada), Rowlands (Adelaidean, Stuart Shelf).
  Article 800 is 1989 (out). Article 3498 failed (SSL).
- 11 dimension statements transcribed (level3_analog_dimensions_pre_t0.csv):
  reduced horizons continuous for ~100 km (Copperbelt Ore Shale) to ~200 km
  (Keweenaw, Permian shales); ore patches 3 to 10 km by 1 to 4 km (Texas),
  ~5 km with a 400 m gap over a basement high (Mufulira), some thousand m2
  to some km2 (Mansfeld); Kupferschiefer ore ~0.2% of the reduced shale's
  coverage. This supports the annex's "tens of km; 1 to 10 km".
- Still to supply by hand (library): Mendelsohn 1961; White and Wright 1954;
  Brown 1971; Ensign et al. 1968 (NOT_FOUND.md in the level folder).

Mount Gunson analog dossier (2026-09-21). WMC's EL 190 concept named Mount
Gunson; its pre-t0 open file was read and transcribed:
- mount_gunson_t0_dossier.csv: 37 statements from 13 documents, 1941 to
  9 Oct 1974 (36 before t0; the Pacminex genesis text signed 3/3/1975 but
  filed under a July 1976 title page is unresolved, cross-check only).
  Key sources: Maiden PMR 58/74 (May 1974, Woocalla facies), Maiden PMR 97/73
  (Sep 1973), Johns RB 72/00189 (Oct 1972), Johns RB 74/00197 (Oct 1974),
  Thomson et al. RB 74/00135 (Jun 1974), Tonkin PMR 149/71 (Aug 1971),
  Mathias East Lagoon evaluation (Apr 1970), Mason RB 65/00068 (1967),
  Bulletin 41 (1968), RB 18/00119 (1941), Thomson RB 60/00004 (1965).
- mount_gunson_LD_holes_1971.csv: 6 of 7 widely spaced 1971 holes cut
  Woocalla black/dolomitic shale, 12 to 129 m (median 47 m); Woomera 1
  (82 km from the deposit) has 113 m of dark-grey shale on the Pandurra.
- Lengths: reduced unit / disconformity 15 to 145 km; patches (ore, Pb-Zn
  troughs, facies fringe) 0.5 to 3 km.
- Grade-tonnage (for Level 4): 0.03-0.4 Mt at 3-3.5% Cu and 0.2-3 Mt at
  1-1.4% Cu; tabular bodies to about 5 m thick.
- Round 3 fetched: RB 72/00189, Env 06604 (East Lagoon), RB 63/00075
  (1966 geophysics, not transcribed), Env 02292 (1973 Cattlegrid pit plans,
  not transcribed).
Notebook: 02_code/notebooks/wp4_level3_redox_architecture.ipynb, Part C.

## Level 4: Ore rule (checked 2026-09-21; PP 820 fetched, folder built)

Basis (Annex A): "Haynes's memoranda for the rule and its reach, and the
analog deposits as known by 1975, the Zambian Copperbelt, White Pine, and
the Kupferschiefer, for the blanket statistics."

Rows: reach d to a basalt margin (0-10 km); P(ore | margin, reduced) (0.05-0.3);
lineament-intersection multiplier (2-5); blanket thickness 2-30 m, grade
1-4% Cu, tonnage lognormal with median tens of Mt.

Piece 1, Haynes's memoranda. NOT on disk, not in open file (Level 2 finding;
decision pending: request from BHP or carry as testimony). Stand-ins on disk:
EL 190 first quarterly concept statement (a quarter after t0); O'Driscoll
1974 target sheets and the 1/f = 18 bound (Level 2); Mount Gunson dossier
(Level 3): basic dyke swarm and Katunga dolerite ~500 ppm Cu (Johns 1972),
basalt >200 m under the Pandurra (Johns 1974), Cu fall-off over 1-15 km from
the basin edge (Maiden 1974), MG14 dyke ~1 km from the Cattle Grid (genesis
text, date unresolved); Risely 1968 (Level 2). Analog ore fractions for
P(ore | ...): Kupferschiefer 0.002 of area, Permian shales 0.3 of belt (Level 3).

Piece 2, analog blanket statistics. Partly on disk.
- Mount Gunson (Level 3 dossier): seven pre-t0 tonnage/grade figures,
  0.03-3 Mt at 1-3.5% Cu; tabular bodies to ~5 m.
- White Pine: White and Wright 1954 (grades, "multimillion-ton" body under
  several square miles), Brown 1971 (no tonnage).
- Permian copper shales (Johnson 1974): 1-2% Cu, 15-45 cm, ~30 km2 bodies.
- Copperbelt and Kupferschiefer: thickness and area fraction only; no
  tonnage or grade in the Liege OCR text. Mendelsohn 1961 and Ensign 1968
  print only.
Fetched: USGS PP 820 (1973), copper chapter (Cox, Schmidt, Vine, Kirkemo et
al.), transcribed in level4_blanket_statistics_pre_t0.csv (26 rows, quotes and
pages). Copperbelt: seven deposits averaging 4 Mt Cu each at 3.5% Cu (fig. 22
envelope about 55-330 Mt ore at 2-4.5% Cu), district reserve well over 1,000 Mt
ore, ore zoned parallel to the shoreline (Garlick 1961). Kupferschiefer: bed
about 0.5 m, economic only in some areas of Lower Silesia; no tonnage.
White Pine: ore bed 1-8 m, anomalous Cu over at least 250 km, 7-8 Mt Cu
production plus reserves, 11 Mt Cu subeconomic. Rule: favourable environment 10,
porous strata updip and marginal to buried basalt (Portage Lake, perhaps
Nonesuch), and "a coincidence of several may greatly increase the probability".
Table 39 read from the page image (text layer scrambled): Africa 53 Mt Cu
identified, Europe excl. USSR 25.
Against the Annex A rows: grade 1-4% supported (Copperbelt 2-4.5, White Pine and
Gunson 1-3.5); thickness 2-30 m: White Pine 1-8 m and Kupferschiefer 0.5 m sit
below it, Copperbelt ore-body thickness still to supply; tonnage median tens of
Mt: Copperbelt deposits are about 100 Mt ore, Gunson 0.03-3 Mt, so the spread is
wide. Reach d: no number in PP 820; the basalt-to-ore gap at White Pine is
vertical (110-1,850 m), not a lateral distance.
Placed by hand 2026-09-21 (rows 27-46): White 1942 (Mansfeld: ore bed 0.13-0.51 m,
2.5-2.8% Cu, ore 0.0086 of the host shale area, red cap barren, ore near faults),
Douglas 1955 (Roan Antelope discussion letter only), Love 1962 (Kupferschiefer),
Gillson 1963 (Copperbelt review quoting Mendelsohn 1961: ore layer under 15 m in
most cases, gabbro near each major deposit, lineament over 320 km); White and
Wright 1954 grades 1-5% (laminated) and 1-2% (massive).
NOT FOUND: USBM Minerals Yearbook 1971-72 (not downloadable), main Roan Antelope
paper (Econ. Geol. 49, 1954), Mendelsohn 1961, Ensign et al. 1968.
Notebook verdicts (wp4_level4_ore_rule.ipynb): grade 1-4% supported; thickness
0.13-15 m for ore beds, annex 2-30 m too thick at the floor; tonnage bimodal
(Gunson 0.15-3.2 Mt, world analogs 57-198 Mt, one lognormal median 3.2 Mt,
log10 sd 1.24); P(ore) 0.002-0.009 over a basin, 0.09-0.35 along a belt; reach d
and the lineament multiplier have no pre-t0 number (Johns 1972 is the only pre-t0
source stating all three rule conditions).
Folder: wp4_prior_state/annexA_levels/level4_ore_rule/ (haynes_memoranda with
NOT_FOUND.md and stand-ins; analog_blanket_statistics).

## Level 5: Petrophysical attachment (checked 2026-09-22; folder built)

Basis (Annex A): "the density contrasts the WMC interpreters themselves
assumed when modeling the anomalies, with the era textbooks (Dobrin; Grant
and West; Parasnis) as backup."

Rows: density (basalt 2.80-3.00, cover 2.4-2.6), susceptibility (basalt
magnetic, cover non-magnetic), resistivity (cover conductive where saturated),
ore blanket close to invisible to gravity and magnetics, shear velocity
undefined.

Piece 1, the density contrasts WMC assumed. The model sheets and sample
measurements are NOT FOUND: the work pre-dates the licence, so it is in WMC's
own files (now BHP's) or the EL 190 application papers, the same gap as
Haynes's memoranda (S22). One decision covers both.
- Rutter and Esdale 1985 (Expl. Geophys. 16, 273-276), by the two WMC
  geophysicists, is the only record: Roopena Volcanics sampled at Roopena
  Station and Depot Creek against five Marinoan units; the susceptibility
  contrast "variable" with alteration and never given as a number; the density
  contrast 0.3 g/cc "established with a greater degree of credibility"; block
  models at that contrast put Olympic Dam at 1,150 m, or 850 m if reshaped, and
  the magnetic source at about 2,000 m. DATED 1985, after t0. RULING NEEDED,
  same class as Haynes 2006.
- Pre-t0 stand-ins on disk: Risely 1968 measured the same Roopena outcrops
  (Roopena Volcanic 2.61-3.35, means 2.68-2.87; weathered 2.42; Pandurra
  quartzite 2.44; Moonabie quartzite 2.62-2.66; reduction density 2.67), which
  gives a Roopena-against-Pandurra contrast of about 0.35 and against Moonabie
  about 0.18. Milton et al. 1966 at Mount Gunson (RB 63/75): reduction density
  2.59, residual contrast over the ore only 0.3 mGal, and seven methods with
  "no diagnostic relationships to the ore occurrence" - era support for the
  annex line that the blanket is close to invisible.
- After t0, cross-checks only: AMDEL bulk densities of six RDD1 (and one RDD2)
  core samples, 3 October 1975, 2.58-3.05 g/cc with 3.05 inside the mineralised
  interval, so the measured contrast is 0.35-0.45 against cover, but against
  hematite-rich rock rather than the basalt the 0.3 was assumed for; the
  December 1975 gravity plans (2307-09/10/11) with reduction density 2.20 g/cc
  printed beside an E.C.F. of 0.2081 mGal/m, which implies about 2.40, so the
  plan is internally inconsistent [CHECK]; and the RD-hole core S.G. and
  susceptibility sheets in mesac25009.

Piece 2, the era textbooks. All three scanned by Peng and transcribed
(replay_ready/prior/level5_era_properties.csv, 202 rows with page and table):
- Dobrin 1960, 2nd ed. (90 rows): Table 12-1 densities pp. 250-251, Fig. 12-5
  averages (sandstone 2.32, shale 2.42, limestone 2.54, dolomite 2.70, basic
  igneous 2.79), Tables 13-1 and 13-2 and Fig. 13-5 susceptibilities pp.
  268-270 (basalt measured 680, calculated average 14,300 x 1e-6 cgs),
  Table 17-1 resistivities p. 341. Sedimentary contrasts "seldom exceeding
  0.25 g/cm3".
- Parasnis 1973, Mining Geophysics 2nd ed. (51 rows; printing 1973 confirmed by
  Peng, this copy's title page reads 1975): Table V densities p. 251 (basalt
  2.70-3.30, diabase 2.50-3.20, gabbro 2.70-3.50, limestone and quartzite
  2.60-2.70), Table I susceptibilities pp. 28-29 (basalt 250-105,000 x 1e-6 for
  0-2.5% magnetite), Fig. 56 resistivity ranges p. 166 (graphical only).
- Grant and West 1965 (36 rows): Fig. 7-6 80 per cent fiducial limits pp.
  198-199 (igneous 2.55-2.95, limestone 2.20-2.70, shale 2.10-2.60, sandstone
  2.05-2.50), Tables 12-2 and 12-3 susceptibilities p. 366 (basalt mean
  2.95e-3 emu), k = 2.89e-3 V^1.01 p. 367, Fig. 13-4 and the formation-factor
  relations pp. 394-395, Table 13-1 mineral conductivities p. 398. Two
  statements matter: a density contrast is "impossible to predict with
  confidence" from lithology alone (p. 199), and hematite is "not normally a
  conductor", 1-100 mhos/m in specular form with impurities (p. 399), which is
  era support for a near-blind resistivity and IP channel over this ore.

Against the Annex A rows: cover 2.4-2.6 supported (Dobrin averages 2.32-2.70,
Grant and West limits 2.05-2.70); basalt 2.80-3.00 supported (Parasnis
2.70-3.30, Dobrin diabase 2.804-3.110, basic igneous average 2.79); the 0.3
contrast is consistent with all three books but the books themselves say a
contrast cannot be pinned from lithology, so it should be carried as a
distribution, not a number; susceptibility has no WMC number and the era books
disagree by a factor of 20 between measured and magnetite-derived values;
resistivity for saturated cover rests on textbook tables and the formation
factor, not on any era measurement at the deposit; the ore being close to
invisible is supported directly by Milton 1966 and by Grant and West on
hematite. Shear velocity: nothing to fetch, the annex already says no era value
existed.

Folder: wp4_prior_state/annexA_levels/level5_petrophysical_attachment/
(wmc_assumed_contrasts with NOT_FOUND.md and the pre-t0 stand-ins,
era_textbooks, cross_checks_after_t0).
Notebook: 02_code/notebooks/wp4_level5_petrophysical_attachment.ipynb
(9 figures; Parts A, B per basis piece, C rows). Verdicts: directions all
supported; three numbers should become distributions (contrast 0.15-0.5 rather
than 0.3; basalt susceptibility 250-105,000 x 1e-6 cgs; cover resistivity
attached through porosity and pore water, not by rock name). Depth is far more
sensitive to body shape than to the contrast (factor 1.8 over the whole era
contrast range). Ore invisibility confirmed twice: a 30 m blanket at 4% Cu as
chalcopyrite gives 0.14 mGal against Milton's 0.3 mGal yardstick, and hematite
conducts 0.1 mhos/m.
