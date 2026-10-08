#!/usr/bin/env bash
# Download the 10,000-member ensembles from the GitHub release and place them where the notebooks read them.
# Needs the GitHub CLI (gh) logged in, or set GH_TOKEN. Run from the SVOI_OD folder:  bash 10_releases/fetch_ensembles.sh
set -euo pipefail
TAG="${1:-ensembles-2026-10-07}"
REPO="Patrick-PengLi/SVOI_OD"
declare -A DEST=( [A_sh_v0.10]=08_prior_models/gen_n10000 [B_fe_v0.2]=08_prior_models/middleback/gen_n10000 [C_mg_v0.1]=08_prior_models/mountgunson/gen_n10000 )
tmp=$(mktemp -d)
gh release download "$TAG" --repo "$REPO" --dir "$tmp"
(cd "$tmp" && sha256sum -c SHA256SUMS.txt)
for pre in "${!DEST[@]}"; do
  d="${DEST[$pre]}"; mkdir -p "$d"
  mv "$tmp/${pre}_pred_all.npz" "$d/pred_all.npz"; mv "$tmp/${pre}_draws_all.csv" "$d/draws_all.csv"; cp "$tmp/observed.npz" "$d/observed.npz"
  echo "placed $pre -> $d"
done
rm -rf "$tmp"
