#!/bin/bash
# Run once on a Sherlock login node:  bash setup_env.sh
set -e
cd "$(dirname "$0")"
source env.sh
python3 --version
rm -rf $HOME/svoi_env
python3 -m venv $HOME/svoi_env
source $HOME/svoi_env/bin/activate
pip install --upgrade pip
pip install --only-binary=:all: numpy scipy pandas pyproj
pip install --prefer-binary discretize
python -c "import numpy, scipy, pandas, pyproj, discretize; print('environment ready, numpy', numpy.__version__)"
