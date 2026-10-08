#!/bin/bash
# 10,000 prior models = 100 chunks of 100 seeds (3000-12999), at most 64 running at once. Noise-free (--noise 0); the tests add their own
# noise from observed.npz. Use a fresh --out folder: finished chunks are skipped. gen_n10000_mg = Mount Gunson branch WP4-C-MG v0.1 (2026-10-07) on the shared setting of Annex A v0.10;
# seeds 3000-12999 as the basalt run, so Level 1 and the piles match seed for seed.
# For 2,000 models use --array=0-19. Change --partition after checking sh_part.
#SBATCH --job-name=svoi_gen_mg
#SBATCH --partition=normal
#SBATCH --array=0-99%64
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/gen_%A_%a.out

export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
source $HOME/svoi_od/09_sherlock_mountgunson/env.sh
source $HOME/svoi_env/bin/activate

python $HOME/svoi_od/09_sherlock_mountgunson/run_gen.py \
    --out $SCRATCH/svoi_od/gen_n10000_mg \
    --start 3000 --chunk 100 --noise 0
