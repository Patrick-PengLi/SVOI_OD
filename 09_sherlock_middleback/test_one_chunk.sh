#!/bin/bash
# Quick check on a login node (about 10 s):  bash test_one_chunk.sh
set -e
cd "$(dirname "$0")"
source env.sh
source $HOME/svoi_env/bin/activate
export OMP_NUM_THREADS=1
python run_gen.py --out $SCRATCH/svoi_od/test_fe --chunk 5 --chunk-id 0 --noise 0
python merge_gen.py $SCRATCH/svoi_od/test_fe
