"""Merge the chunk files into one npz and one csv:  python merge_gen.py <folder>"""
import sys
from pathlib import Path
import numpy as np, pandas as pd

d = Path(sys.argv[1])
files = sorted([p for p in d.glob("pred_*_*.npz")], key=lambda p: int(p.stem.split("_")[1]))
seeds = np.concatenate([np.load(f)["seeds"] for f in files])
grav = np.concatenate([np.load(f)["grav"] for f in files]); mag = np.concatenate([np.load(f)["mag"] for f in files])
draws = pd.concat([pd.read_csv(d / f.name.replace("pred_", "draws_").replace(".npz", ".csv")) for f in files], ignore_index=True)
assert (draws.seed.values == seeds).all() and len(np.unique(seeds)) == len(seeds)
gaps = sorted(set(range(seeds.min(), seeds.max() + 1)) - set(seeds.tolist()))
np.savez_compressed(d / "pred_all.npz", seeds=seeds, grav=grav, mag=mag); draws.to_csv(d / "draws_all.csv", index=False)
print(f"{len(files)} chunks, {len(seeds)} realizations (seeds {seeds.min()}-{seeds.max()}), missing seeds: {len(gaps)}")
print(f"grav {grav.shape}, mag {mag.shape} -> pred_all.npz, draws_all.csv")
