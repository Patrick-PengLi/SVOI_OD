# Level 1 check, 2026-09-18: sheets, notes and the wider bore search

Basis for Level 1 of the prior: the SA 1:250,000 sheets and their notes for
ANDAMOOKA and TORRENS, and the bores logged at t0 (2 May 1975). This note
records what was checked on 2026-09-18, what was found, and what is still
to fetch. Data files are beside it; the script is
`02_code/scripts/bores_buffer_search.py`.

## 1. Explanatory notes for the two sheets

`wp4_prior_state/03_geology_sheets_1_250000/` holds six map faces (1st, 2nd
and digital editions of both sheets) and no notes booklet. SARIG's
"ExpNotes" series (records 2018d040088 to 2018d040138) was walked in
catalogue order: it runs ABMINGA, BARTON, BILLA KALINA, CALLABONNA,
CHILDARA ... TALLARINGA, WARRINA, WHYALLA, WINTINNA, WOODROFFE, YARDEA.
There is no ANDAMOOKA and no TORRENS entry, so no notes booklet was ever
issued for the first editions. Their companion text is Johns, R.K.,
"Geology and mineral resources of the Andamooka-Torrens area", written as
RB 61/00102 (19 Oct 1965) and published as Geological Survey of South
Australia Bulletin 41 (1968, 103 pp.). The report-book form is on disk
(`03_.../supporting_reports/rb6100102/`, 24.2 MB); the published Bulletin
is SARIG record 2018d037811 (16.2 MB, CC-BY) and is NOT on disk. Both the
catalogue host and the blob host refuse the cloud and VM proxies, so it
needs one local run:

    python 02_code/scripts/fetch_250k_sheets.py

(the record was added to that script; files already present are skipped).
Both texts are in state (1965 and 1968, before t0). The reference panels on
the map faces themselves were already read for the wp4_03 notebook.

## 2. Pre-1975 holes to basement outside the window (2 degree buffer)

Buffer: the regional window widened by 2 degrees on each side (lon 134.30
to 139.45, lat -32.98 to -27.92). Source: the SA Geodata details and
stratigraphy exports already on disk (`drillholes/sa_geodata/`). Screen:
MAX_DRILLED_DEPTH_DATE before 2 May 1975 (undated holes are not admitted;
1 petroleum and 41 stratigraphic-class holes in the buffer are undated,
27 undated holes exceed 300 m, most of them WMC RD series). Age from the
GIS_CODE prefix: A Archaean, Y/L Palaeoproterozoic, M Mesoproterozoic
(pre-Adelaidean), N Adelaidean, E Cambrian, all else younger cover.

Counts: 69,753 holes in the buffer, 10,167 drilled before t0, 1,670 of
those with a stratigraphic log. 347 logged pre-Adelaidean rock; of these
221 reached crystalline basement (Pandurra Formation excluded) and 126
bottomed in the Pandurra Formation only.

Distance from Olympic Dam (136.887 E, 30.441 S):
- nearest pre-t0 hole with pre-Adelaidean rock: WOOMERA 1 (Clarence River
  Basin Oil Co, May 1958, 611 m, 82.5 km SW): Pandurra Formation from
  454 m to end of hole, under 42 m of Cretaceous (Bulldog Shale) and 412 m
  of Adelaidean (Corraberra, Tregolana, Whyalla Sandstone, Tapley Hill; no
  Cambrian). This is the only pre-t0 statement of a thick cover over
  Pandurra within 100 km of the deposit.
- the Mount Gunson / Pernatty group, 110 to 170 km SSE on the TORRENS
  sheet: LY 2 and LY 3 (CSR, March 1974; Pandurra from 29 m, LY 2 to
  667 m), LD 1 to 6 (1971; Pandurra at 66 to 192 m), MF 1 to 12 (1973-74;
  Pandurra at 38 to 92 m), WP 5 to 26 (1968; Pandurra at 8 to 59 m), and
  water bores on KINGOONYA (1959-62; Pandurra at 17 to 53 m). All end in
  Pandurra; none reached the rocks beneath it.
- nearest pre-t0 hole into crystalline (pre-Pandurra) basement: G 1
  (Gairdner Range Volcanics area, 1904, 160 km W, Yardea Dacite at 4 m)
  and the Delhi Mount Woods 1 to 7 holes (Oct-Nov 1964, 163 to 169 km NW,
  Palaeoproterozoic rocks at 49 to 92 m). Everything else is 180 km or
  more away (Gawler Craton outcrop on GAIRDNER, TARCOOLA, STREAKY BAY;
  Middleback and Port Augusta district on PORT AUGUSTA).
- petroleum wells before t0 in the buffer: 28. Wilkatana 1 to 19 (1956-57,
  205 km SE, deepest 670 m, three logged into "Proterozoic rocks"), Motpena
  1 and 2 (1957, Parachilna), AW 2 and 4 (1969, Copley), Weedina 1 (Pexa
  1970, 249 km NW, 1,624 m, Archaean-Devonian rocks from 1,609 m). None
  bears on the Stuart Shelf cover near the deposit.
- stratigraphic-class holes before t0 in the buffer: 82, but the class is
  dominated by shallow engineering bores (Works and Housing DD series at
  Woomera 1947, Lake Hart launcher bores 1957-60, Dept of Works 1960) and
  the MPE series on MARREE (1971-72). The SADME stratigraphic holes that
  matter are TR 1, 1A, 2 (1964, 193 km), Lake Torrens 3 to 5 and 3A
  (1960-64, 141 to 146 km), BEDA BORE (1889, 335 m, 178 km) and Roopena
  DDH 1 to 4 (1967-68, 258 km, in Roopena Basalt from surface). 51 of the
  82 carry no stratigraphic log in SA Geodata.
- inside the regional window: 0 (consistent with the 2026-09-10 finding of
  101 pre-t0 holes, deepest 117 m).

Files: `bores_buffer2deg_pre_t0_basement.csv` (347 holes; columns include
depth to the first pre-Adelaidean unit, depth to the first crystalline
basement unit, the two flags, the unit and GIS-code sequences, hole class,
operator, sheet, distance from OD), `..._strat_intervals.csv` (their
intervals with the age class per interval), and
`bores_buffer2deg_pre_t0_strat_petroleum.csv` (all 110 stratigraphic- and
petroleum-class holes before t0, reached basement or not).

## 3. Cross-check against mesac17946 (Trevena 1979, SADME compilation)

Envelope 9395, "Stuart Shelf Project, drillhole stratigraphy compilation
using data acquired until 31/12/1978", H. Trevena, 1979, draft. On disk in
`reports/era_1975_1982/mesac17946/` (a 76-page scan; OCR text of the
typed pages now beside it as `mesac17946_ENV09395_ocr.txt`, uncorrected;
the appendix tables are handwritten and were read from the page images).
Contents: text pp. 3-15, list of drill holes with data source pp. 16-37,
Appendix I TORRENS pp. 38-47, II PORT AUGUSTA pp. 48-55, III
WHYALLA/BURRA pp. 56-59, IV ANDAMOOKA, GAIRDNER, KINGOONYA, BILLA KALINA,
WARRINA, CURDIMURKA pp. 60-62; contour plans of the base of Sturtian
sedimentation and of post-Pandurra cover. Column semantics: RL in feet and
metres; "BASE STURTIAN" and "TOP PANDURRA" are elevations (m, relative to
sea level) of the contoured surfaces with the overlying unit in brackets;
"BASEMENT" is in most rows the end-of-hole elevation (a minimum), not a
crystalline basement contact; red figures are minima; only inked RLs are
levelled.

Andamooka sheet (Appendix IV, p. 61): the holes with a depth to Pandurra or
basement are RD-1 and RD-3 to RD-10 (Olympic Dam; "the unit named Pandurra
is rarely more than a few metres thick"; RD-1 RL 306 ft / 93 m, basement
-234 m), RD-7, BD-1, TOD-1, PD1-A, AD-1, CD-1, WWD-1, TD-3 and FHD-1. In
SA Geodata every one of these families on the Andamooka sheet is dated
1976 to 1978 (WMC). So at 31 Dec 1978 the SADME files held NO pre-1975
hole on the Andamooka sheet with a depth to Pandurra or basement, which
confirms the SA Geodata result from a period source.

Torrens sheet (Appendix I, pp. 39-47): the pre-t0 holes in the compilation
are WOOMERA BORE (RL 460 ft / 140 m, top Pandurra -332 m under Sturtian,
end of hole -471 m; SA Geodata: Pandurra from 454 m, EOH 611 m; the 18 m
difference is probably the RL used), BEDA BORE (1889; RL 101 m, Beda Volcanics and
"Pandurra" at -234 m = 335 m = end of hole; SA Geodata has no log for it),
LY 2 and LY 3 (1974), LD 1 to 29 (1971 onward), MF 1 to 13 (1973-74), WP
5 to 74 (1968 onward) and LW 19 to 55 (1966 onward). Everything else in
that appendix (OK, PL, BK, PEB, PRL/SAR, EX, PSC/SASC, PIL/SAI, AD-2,
WHD-1, BDH 1-4, SLT 101-104, Pacminex LH-1) is dated August 1975 to 1979
in SA Geodata. Hole-by-hole check where both sources carry a number
(depth to top of Pandurra, m): LD 2 183 vs 183.5; LD 3 192 vs 191.7; LD 4
136 vs 135.3; MF 1 38 vs 38.0; MF 2 71 vs 71.0; MF 4 89 vs 89.0; MF 5 92
vs 92.0; LY 2 29 vs 29.4. The modern export reproduces the 1978
compilation to the metre.

Period usage of the unit names (compilation pp. 5-6): "Basal Adelaidean
cover of the Stuart Shelf is represented by the Pandurra Formation. This
unit rests unconformably on pre-Adelaidean cover rocks and older basement
rocks of the Gawler Craton; it is equated with the Callanna Beds". SADME
in 1979 therefore counted the Pandurra Formation as COVER (its contoured
"post-Pandurra cover" surface is the top of the Pandurra), while SA
Geodata today codes it Mesoproterozoic (M----p). For the Task 2 ruling
this means the period explorer's "basement" is the pre-Pandurra
crystalline rock, i.e. the `reached_crystalline_basement` flag, not
`reached_pre_adelaidean`. Note also the compilation is dated 1979 and
draws on closed-file company data to end-1978: it is a cross-check on the
modern export, not itself a t0 source.

## 4. What this settles for the prior

At t0 no hole within 82 km of the deposit had logged anything older than
Adelaidean; no hole within 160 km had reached crystalline basement; the
only deep cover figure near the window was WOOMERA 1 (454 m of Cretaceous
and Adelaidean over Pandurra, 82 km SW). Cover thickness at the deposit at
t0 therefore rests on the sheets, Bulletin 41 and section A-B, then on
the May 1975 reflection event (291 +/- 34 m), and gets its first
drilled number from RDD1 (335 m). The WP4 Task 2 placeholder band of
150-600 m has no bore support inside 80 km; WOOMERA 1 sits inside that
band.

Still to fetch: Bulletin 41 (2018d037811, one local run of
fetch_250k_sheets.py). Still open: the drill-hole data-source list of the
compilation (pp. 16-37, handwritten) has not been transcribed; it would
give the open-file / closed-file status of each pre-1975 hole, which
matters for the "whose information state" ruling.
