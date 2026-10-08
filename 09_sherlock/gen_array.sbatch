#!/bin/bash
# 10,000 prior models = 100 chunks of 100 seeds (3000-12999), at most 64 running at once. Noise-free (--noise 0); the tests add their own
# noise from observed.npz. Use a fresh --out folder: finished chunks are skipped. gen_n10000_c9 = prior v0.10 (Change 9 horsts, 2026-10-06);
# the earlier gen_n10000_sheet (v0.9) and gen_n10000 (342 stations) are superseded.
# For 2,000 models use --array=0-19. Change --partition after checking sh_part.
#SBATCH --job-name=svoi_gen
#SBATCH --partition=normal
#SBATCH --array=0-99%64
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/gen_%A_%a.out

export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
source $HOME/svoi_od/09_sherlock/env.sh
source $HOME/svoi_env/bin/activate

python $HOME/svoi_od/09_sherlock/run_gen.py \
    --out $SCRATCH/svoi_od/gen_n10000_c9 \
    --start 3000 --chunk 100 --noise 0
