# WP4 period prior: 10,000-member ensembles, three branches (2026-10-07)

Prior realizations of the Stuart Shelf window (Andamooka SH53-12 sheet, 147 x 115 km, 1 km cells) forward-modelled and
sampled at the t0 survey points: the 398 BMR helicopter gravity stations (1969, surveys 196953/196955) and the 37,095
P234 aeromagnetic readings (1962). Noise-free; the analysis notebooks add the survey noise where a test needs it.

Seeds 3000 to 12999 in every branch (`numpy.random.default_rng(seed)`), so Level 1 (cover, basement relief, horsts)
and the barren basalt piles are the same realizations across the three branches, member for member.

| Asset | Branch | Generator | Shape |
|---|---|---|---|
| `A_sh_v0.10_pred_all.npz`, `A_sh_v0.10_draws_all.csv` | A, sediment-hosted Cu on basalt margins (Annex A, WP4-A-SH v0.10, Changes 1 to 9) | `09_sherlock/svoi_core.py` | grav (10000, 398) float32, mag (10000, 37095) float32 |
| `B_fe_v0.2_pred_all.npz`, `B_fe_v0.2_draws_all.csv` | B, Middleback-type iron (Annex B, WP4-B-FE v0.2) | `09_sherlock_middleback/svoi_fe.py` on `svoi_core` | same |
| `C_mg_v0.1_pred_all.npz`, `C_mg_v0.1_draws_all.csv` | C, Mount Gunson-type stratiform Cu (Annex C, WP4-C-MG v0.1) | `09_sherlock_mountgunson/svoi_mg.py` on `svoi_core` | same |
| `observed.npz` | the t0 surveys at the same points (identical in all three runs) | `svoi_core` | grav_x, grav_y, grav, grav_sd, mag_x, mag_y, mag |
| `SHA256SUMS.txt` | checksums of the above | | |

`pred_all.npz` holds `seeds`, `grav`, `mag`. `draws_all.csv` holds one row per seed: the Level 1 to 5 draws of the
shared setting, the branch's own rows (L3/L4, B2 to B4, or C3/C4), and the realization summaries (`n_basalt`, `n_ore`,
`Mt_total` or `Fe_Mt_total`, etc.).

Produced on Sherlock (SLURM arrays of 100 chunks x 100 seeds) with the folders `09_sherlock*/` of this repository at the
commit tagged `ensembles-2026-10-07`; each chunk was checked against the notebook's own realization of the same seed to
float32 precision. Where the files go and what reads them: `A_*` -> `08_prior_models/gen_n10000/`, `B_*` ->
`08_prior_models/middleback/gen_n10000/`, `C_*` -> `08_prior_models/mountgunson/gen_n10000/` (drop the prefix);
`observed.npz` into each. Readers: `wp4_prior_ensemble_n10000_analysis*.ipynb` (one per branch) and
`wp4_bayes_factor_branches.ipynb`. `10_releases/fetch_ensembles.sh` does the download and placement.
