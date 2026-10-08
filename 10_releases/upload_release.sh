#!/usr/bin/env bash
# Create the GitHub release and upload the ensembles (run once, from the SVOI_OD folder, after the commit is pushed).
set -euo pipefail
TAG="ensembles-2026-10-07"; R="10_releases/$TAG"; P="08_prior_models"
git tag -f "$TAG" && git push -f origin "$TAG"
gh release create "$TAG" --title "WP4 10,000-member ensembles, three branches (2026-10-07)" --notes-file "$R/RELEASE_NOTES.md"
gh release upload "$TAG" \
  "$P/gen_n10000/pred_all.npz#A_sh_v0.10_pred_all.npz"             "$P/gen_n10000/draws_all.csv#A_sh_v0.10_draws_all.csv" \
  "$P/middleback/gen_n10000/pred_all.npz#B_fe_v0.2_pred_all.npz"   "$P/middleback/gen_n10000/draws_all.csv#B_fe_v0.2_draws_all.csv" \
  "$P/mountgunson/gen_n10000/pred_all.npz#C_mg_v0.1_pred_all.npz"  "$P/mountgunson/gen_n10000/draws_all.csv#C_mg_v0.1_draws_all.csv" \
  "$P/gen_n10000/observed.npz#observed.npz" "$R/SHA256SUMS.txt#SHA256SUMS.txt"
gh release view "$TAG"
