# Prior-model generation on Sherlock

Self-contained: copy this whole folder to `/home/users/pli6/svoi_od/09_sherlock` (WinSCP, binary mode).
The inputs the sampler reads are inside it (01_citation_table, 03_sampler_inputs, 04_prior_predictive_observed).

    cd $HOME/svoi_od/09_sherlock
    bash setup_env.sh                 # once; builds $HOME/svoi_env
    bash test_one_chunk.sh            # 5 seeds into $SCRATCH/svoi_od/test, about 10 s
    mkdir -p logs && sbatch gen_array.sbatch
    squeue -u $USER
    # interactive use (merge etc.): source env.sh && source $HOME/svoi_env/bin/activate
    ls $SCRATCH/svoi_od/gen_n10000_c9/pred_*_*.npz | wc -l   # 100 when done
    python merge_gen.py $SCRATCH/svoi_od/gen_n10000_c9         # -> pred_all.npz, draws_all.csv

Then copy `pred_all.npz`, `draws_all.csv` and `observed.npz` back to `08_prior_models/gen_n10000/` (the folder the analysis
notebooks read) and rerun `wp4_prior_ensemble_n10000_analysis.ipynb`; its Step 4 is the 10,000-member version of the
notebook's Step 15 falsification.

The production run is noise-free (`--noise 0`, set in gen_array.sbatch); tests add their own noise realizations from
`observed.npz` (`grav_sd`, `mag_sd`). Seeds 3000-12999 are disjoint from every seed the notebook uses.

If sbatch reports "DOS line breaks", run `dos2unix *.sh *.sbatch`.

## Version of the sampler in this folder

`svoi_core.py` is generated from the notebook by `build_core.py` (data cell, Part 0 setup, the sampler of Part A, Steps 8
and 9), so a seed gives the same realization here as in the notebook.

Rebuilt 2026-10-06 for prior **WP4-A-SH v0.10** (Change 9: under each O'Driscoll 1974 target circle the basement is a horst
raised by the L1-3 relief draw, 0 to 150 m, cut off at the base of the Pandurra; no new row, no new draw). Checked 2026-10-06
against the notebook in the same session: the 50 draws of seeds 1000-1049 match `wp4_prior_draws_n50_reference_v4.csv`
to 1e-12 and the notebook to 0; the noisy prediction of seed 1000 matches the notebook's Step 11 to 0; seed 99 raises the
basement under the circles by 70 m in both. Grid 147 x 115 (Andamooka sheet, Change 7), 6 km basement texture (Change 8),
398 gravity stations, 37,095 magnetic readings. Output folder `gen_n10000_c9`; the earlier `gen_n10000_sheet` (v0.9, no
horsts) and `gen_n10000` (provisional window, 342 stations) are superseded and should not be merged with it.

After changing the sampler or Steps 8-9 in the notebook, run `python build_core.py` locally and copy `svoi_core.py` again.
If the citation table or a sampler input changes, copy it into the matching subfolder here as well (all six input files
were identical to `SVOI_OD/` on 2026-10-06).

## Files

| File | Role |
|---|---|
| `svoi_core.py` | generated sampler + forward operator + observed surveys (do not edit by hand) |
| `build_core.py` | regenerates `svoi_core.py` from `../wp4_period_prior_sediment_hosted.ipynb` |
| `run_gen.py` | one chunk: realize, forward-model, sample at the survey points; skips finished chunks |
| `gen_array.sbatch` | SLURM array, 100 chunks of 100 seeds |
| `merge_gen.py` | merges the chunks into `pred_all.npz`, `draws_all.csv` |
| `test_one_chunk.sh`, `setup_env.sh`, `env.sh` | login-node test, environment build, module load |

Output per chunk: `pred_<c0>_<c1>.npz` (seeds, grav at 398 stations, mag at 37,095 readings, float32), `draws_<c0>_<c1>.csv`,
and one `observed.npz`.
