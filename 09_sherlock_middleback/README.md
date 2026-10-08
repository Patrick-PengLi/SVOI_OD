# Middleback-branch prior-model generation on Sherlock (Annex B)

Self-contained, the twin of `../09_sherlock` for the Middleback-type branch. Copy this whole folder to
`/home/users/pli6/svoi_od/09_sherlock_middleback` (pscp -r, or WinSCP in binary mode). The inputs are inside it
(01_citation_table with the Annex A and B tables, 03_sampler_inputs, 04_prior_predictive_observed).

    cd $HOME/svoi_od/09_sherlock_middleback
    dos2unix *.sh *.sbatch               # if sbatch complains about line breaks
    bash test_one_chunk.sh               # 5 seeds into $SCRATCH/svoi_od/test_fe, about 20 s on a login node
    mkdir -p logs && sbatch gen_array.sbatch
    squeue -u $USER
    ls $SCRATCH/svoi_od/gen_n10000_fe/pred_*_*.npz | wc -l   # 100 when done
    source env.sh && source $HOME/svoi_env/bin/activate
    python merge_gen.py $SCRATCH/svoi_od/gen_n10000_fe          # -> pred_all.npz, draws_all.csv

The environment is the one built by `../09_sherlock/setup_env.sh` (`$HOME/svoi_env`); nothing more is needed. If it is
missing, `bash setup_env.sh` here builds the same one.

Then copy `pred_all.npz`, `draws_all.csv` and `observed.npz` back to `08_prior_models/middleback/gen_n10000/` on the PC.
The analysis of the Middleback ensemble (gate on 10,000, falsification, and the district comparison with the basalt
ensemble in `08_prior_models/gen_n10000/`) is the next notebook to write; the same seeds 3000-12999 are used in both
runs, so Level 1 and the barren piles match seed for seed and the two ensembles differ only in the branch.

## What runs

`svoi_core.py` is the shared setting (grid, rule, operator, surveys, Level 1 with the horsts, barren piles, Level 5),
copied from `../09_sherlock` (generated there by `build_core.py` from the basalt notebook; Annex A v0.10, Change 9).
`svoi_fe.py` is the branch (belt, ranges, ore bodies, properties, `synthetic_fe`), generated here by `build_fe.py` from
`../wp4_period_prior_middleback.ipynb`. `run_gen.py` is the basalt run's script with `synthetic_fe` in place of
`synthetic`; chunks, resume, noise-free output and `merge_gen.py` are identical.

Built 2026-10-07 for WP4-B-FE v0.2 (Level 2 object is the BIF range, ore bodies counted objects of Middleback plan area).
Checked in the same session: a 3-seed chunk through `run_gen.py` reproduces the notebook's `synthetic_fe` for seed 3000 to float32 precision,
and the draws carry the Annex B rows (B2-1, B2-3, B2-4, B3-1, B3-2, B4-1). Rows B are 'to elicit' or 'declared';
confirm them before the ensemble is used in the replay.

After changing the branch cell in the notebook: `python build_fe.py` here and copy `svoi_fe.py`. After changing the
basalt notebook's setting: `python build_core.py` in `../09_sherlock`, then copy `svoi_core.py` here too, so both
branches share one setting.

Output per chunk: `pred_<c0>_<c1>.npz` (seeds, grav at 398 stations, mag at 37,095 readings, float32),
`draws_<c0>_<c1>.csv` (shared rows, Annex B rows, per-realization summaries), and one `observed.npz`.
