# Annex A prior model: citation table, sampler inputs, prior predictive data

Built by 02_code/scripts/build_wp4_prior_state_folder.py. The period prior for the
sediment-hosted branch is built from this folder: Section 3 of the Annex is the
structure, the citation table here is the only source of parameters (Rule 3, one
parameter one row), and Section 2's rules govern both. t0 = 2 May 1975.

01_citation_table/wp4_annexA_citation_table_draft.csv
    The 15 parameters of Annex A Section 5, one row each, same wording. Columns:
    annex working range, PROPOSED distribution, annex expected source, in-state
    source with date, evidence and translation, status. DRAFT for review.
    wp4_annexA_documentary_basis.csv: the Section 6 register, one row per source
    the Annex names (four tiers plus the Level 5 textbooks, retrospective and
    after-t0 items), with status, dates, folder and the rows that use it.
    Fixed settings (held constant, not sampled; recorded here for the audit):
    basement density 2.60 g/cm3 and susceptibility 500 x 1e-6 cgs (Risely 1968
    Gawler Range granophyre and porphyry 2.57-2.62; Dobrin 1960 granite);
    magnetization induced only, in the April 1962 field; ore blanket at the
    base of the reduced unit; Pandurra Formation treated as cover pending the
    Task 2 ruling; shear velocity undefined. Added with the sampler
    (wp4_period_prior_sediment_hosted.ipynb, 2026-09-22): basalt resistivity
    3,100 and basement 5,000 ohm-m (Dobrin 1960); basalt outline aspect 4.7/3.6
    = 1.3 at azimuth 157 degrees (Roopena outcrop, PORT AUGUSTA 1968); reduced
    belt aspect 32/10 = 3.2 at azimuth 10 degrees (Mount Gunson corridor, Johns
    1972); chalcopyrite 34.6% Cu and 4.2 g/cm3 (Parasnis 1973 Table V).
    Sampler choices without a source: trend amplitude equal to the 20% residual
    sd, trend azimuth uniform, cover floored at 50 m, reach d below 0.5 km
    rounded up to half a cell. Section 4 check: induced magnetization in the
    April 1962 field at the deposit (DGRF: F 57,776 nT, I -62.44, D 6.00),
    P234 clearance 150 m; anomaly rule (plane removed, 1 km grid, 3 or more
    cells above 2 mGal or 20 nT; noise 1.0 mGal from the station accuracy
    columns and a declared 5 nT) fixed before the observed statistics.
02_level_parameter_rows/
    The per-level verdict tables from the five level notebooks (L1-L5) and the
    five parameter figures. Evidence behind every citation-table row.
03_sampler_inputs/
    study_windows.csv (regional window 136.3-137.45 E, 30.98-29.92 S); O'Driscoll
    1974 blue targets and the window-sheet dating; the Mount Gunson t0 dossier;
    the Level 4 blanket statistics and the Level 5 property table. Larger inputs
    stay in ../annexA_levels/<level>/ and are read from there.
    Lineaments (Peng, 2026-09-22): the network is represented by O'Driscoll's 20
    blue 1974 targets (wp4_prior_lineament_targets_1974.csv, AMG66 converted to
    lon/lat; 11 in the regional window, 6.8% of its area; 6.6% on the sampler's
    1 km MGA zone 53 grid, which rounds the window out to 13,560 km2). Both lineament
    multipliers (L2-3 basalt intensity, L4-3 ore) act inside these circles. No
    lineament network is digitised or needed.
04_prior_predictive_observed/  (Section 4 only; never used to set a parameter)
    gravity_stations_pre1975_regional.csv: 342 BMR 1969 stations in the window.
    P234-line-magnetic-AWAGS_MAG_2010.nc: inventory item S02, BMR P234
    aeromagnetics flown 1962-04-01 to 1962-04-30, gate PASS, in state at t0.
    305,634 points on 214 line segments. Use the channel mag_awagsLevelled
    (AWAGS 2010 levelling of the 1962 readings), as wp4_02_bmr_aeromagnetics.ipynb
    does; mag_microLevelled and mag_tieLevelled are the other two channels. The
    older cache npz in replay_ready/magnetics holds mag_microLevelled only
    (checked 2026-09-22, max difference 0.0 nT) and is not used here.
05_rules/
    The Annex, the WP4 guideline and the level-by-level basis check.
06_sources/level1_stratigraphic_frame ... level5_petrophysical_attachment/
    Every source document behind the citation table, as checked level by level
    (sheets, Bulletin 41, bore exports, Roopena mapping, O'Driscoll sheets, Mount
    Gunson reports, analog papers, PP 820 chapter, the three textbooks, with
    transcriptions and NOT_FOUND notes). Each level has its own README. The
    column source_files in the citation table points into this folder.
07_notebooks/
    The five executed level notebooks and their 49 figures, read-only records of
    the checks. They read from the project tree (../../01_data/...), so they do
    not re-run from inside this folder; open them to read outputs and captions.
wp4_period_prior_sediment_hosted.ipynb  (in this folder; RUN THIS ONE)
    The prior notebook with its paths set to run from this folder: open it with
    SVOI_OD/ as the working directory. Reads 01_citation_table,
    03_sampler_inputs and 04_prior_predictive_observed; writes to
    08_prior_models/. Needs numpy, scipy, pandas, matplotlib, discretize,
    pyproj, netCDF4 and simpeg. Steps 0-14 run in about 1.5 min; Section 7
    (Steps 15-18, 1,000 realizations) about 5 min more. Generated from
    02_code/notebooks/wp4_period_prior_sediment_hosted.ipynb by the builder.
08_prior_models/
    Outputs of the notebook above: figures wp4_PP_00 to wp4_PP_13, and
    wp4_prior_draws_n50.csv, the parameter draws and summaries of the 50-member
    check ensemble (seeds 1000-1049). Seeds 11, 23 and 37 are the three models
    shown in 3D. Re-running a seed reproduces the same realization. The same
    notebook carries the Section 4 prior predictive check (Steps 8-13, figures
    wp4_PP_08 to wp4_PP_10): wp4_prior_predictive_stats_n200.csv (seeds
    1000-1199) and wp4_prior_predictive_gate.csv (PASS/WARN/FAIL per
    statistic). Step 14 audits the Section 6 register. Steps 15-18 (Section 7,
    run locally): the branch interface checked against
    wp4_prior_draws_n50_reference_v1.csv, the deliverable ensemble with
    likelihood weights (wp4_prior_ensemble_n1000.csv), local refinement, and
    wp4_prior_version.json. wp4_sh_prior_sampler.py is the sampler as a
    module, generated from the notebook, for reuse.

To share: this folder is self-contained (about 550 MB) and is the git repository
SVOI_OD (github.com/Patrick-PengLi/SVOI_OD). Paths in the tables are relative to
this folder. File and folder names are shortened so that no path inside the repo
exceeds 140 characters (Windows' 260-character limit); 06_sources/LONG_NAMES.csv
maps each shortened path to its original name. No file is over 50 MB.

Open before sampling (see open_issue in the table):
1. DOUBLE USE: the 610 m cover upper bound is Young 1964 reading the same 1962
   aeromagnetics the WP3 weighting uses; basalt azimuths must come from
   O'Driscoll's photolineaments, not from aeromagnetic trends.
2. Spatial definition of "margin" for P(ore); tonnage derived, not sampled.
3. Declared assumptions for basalt-object intensity and between-bore
   correlation length (no in-state source can fix either).
4. The fixed settings above replace extra rows; change any of them to a row
   only if the Section 4 check shows the prior is sensitive to it.
5. Rulings: standing of Haynes 2006 and Rutter and Esdale 1985; memoranda
   request to BHP; Pandurra as cover or basement; colour words as redox evidence.
