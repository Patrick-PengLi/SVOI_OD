"""Annex A sediment-hosted period prior sampler (generated from wp4_period_prior_sediment_hosted.ipynb; do not edit by hand).

Run from 02_code/notebooks/. Defines PM, CT, TG, WIN, cited(), the mesh (MESH, NX, NY, XC, YC, GX, GY, HZ, ZC),
FIX, LITH, draw(), grf(), realize(seed, keep_volume). Seed convention: one integer seed per realization, numpy default_rng.
"""
from pathlib import Path
import re
import numpy as np
import pandas as pd
from scipy import ndimage, stats
from pyproj import Transformer
import discretize

PM = Path("../../01_data/wp1_data/database/wp4_prior_state/annexA_prior_model/SVOI_OD")
FIG = Path("../../03_results/wp4_prior/figures")
TAB = Path("../../03_results/wp4_prior")
assert PM.is_dir(), "run from 02_code/notebooks/"
FIG.mkdir(parents=True, exist_ok=True)

CT = pd.read_csv(PM / "01_citation_table/wp4_annexA_citation_table_draft.csv").set_index("row_id")
TG = pd.read_csv(PM / "03_sampler_inputs/wp4_prior_lineament_targets_1974.csv")
WIN = pd.read_csv(PM / "03_sampler_inputs/study_windows.csv").set_index("window").loc["regional"]
ANNEX_GREY = "#e3e3e3"                                  # shading for a confirmed or stated range
OD_LON, OD_LAT = 136.887, -30.441                      # Olympic Dam, for orientation only; never used by the sampler

def cited(row, *numbers):
    """assert that every number the code uses for a row is written in that row's confirmed distribution"""
    txt = CT.loc[row, "proposed_distribution"].replace(",", "")
    written = {float(x) for x in re.findall(r"\d+\.?\d*", txt)}
    for v in numbers:
        assert float(v) in written, (row, v, txt)
    assert str(CT.loc[row, "confirmed"]).startswith("confirmed") or "confirmed" in str(CT.loc[row, "confirmed"]), row
    return True


# ---- mesh: regional window in GDA94 / MGA zone 53, 1 km cells, 25 m layers to 2 km then padding -----------------
to_mga = Transformer.from_crs("EPSG:4326", "EPSG:28353", always_xy=True)
xs, ys = to_mga.transform([WIN.lon_min, WIN.lon_max, WIN.lon_min, WIN.lon_max], [WIN.lat_min, WIN.lat_min, WIN.lat_max, WIN.lat_max])
X0, X1, Y0, Y1 = np.floor(min(xs) / 1e3) * 1e3, np.ceil(max(xs) / 1e3) * 1e3, np.floor(min(ys) / 1e3) * 1e3, np.ceil(max(ys) / 1e3) * 1e3
DX = 1000.0
NX, NY = int((X1 - X0) / DX), int((Y1 - Y0) / DX)
HZ = [25.0] * 80 + [25.0 * 1.5 ** k for k in range(1, 11)]          # 80 x 25 m to 2 km, then 10 padding layers to about 6.3 km
MESH = discretize.TensorMesh([[DX] * NX, [DX] * NY, HZ[::-1]], origin=[X0, Y0, -sum(HZ)])
ZC = -MESH.cell_centers_z[::-1]                        # cell-centre depths below surface (m), top layer first
XC = X0 + DX * (np.arange(NX) + 0.5); YC = Y0 + DX * (np.arange(NY) + 0.5)
GX, GY = np.meshgrid(XC, YC)                           # (NY, NX) map grid
AREA_KM2 = NX * NY * (DX / 1e3) ** 2
TX, TYY = to_mga.transform(TG.lon.values, TG.lat.values)
IN_CIRCLE = np.zeros((NY, NX), bool)
for x, y, r in zip(TX, TYY, TG.radius_km.values):
    IN_CIRCLE |= (GX - x) ** 2 + (GY - y) ** 2 <= (r * 1e3) ** 2
ODX, ODY = to_mga.transform(OD_LON, OD_LAT)

# ---- fixed settings (held constant, not sampled; README of annexA_prior_model) --------------------------------------
FIX = dict(rho_basement=2.60, k_basement=500.0, res_basalt=3100.0, res_basement=5000.0,
           basalt_aspect=4.7 / 3.6, basalt_az=157.0,          # Roopena outcrop, PORT AUGUSTA 1968
           belt_aspect=32.0 / 10.0, belt_az=10.0,              # Mount Gunson corridor, Johns 1972 (RB 72/00189)
           cu_in_ccp=0.346, rho_ccp=4.2,                       # chalcopyrite, Parasnis 1973 Table V
           iron_ratio=0.15 / 0.40, iron_aspect=3.0, iron_az=0.0, iron_thick_m=200.0, k_iron=5000.0,   # Change 1: iron-oxide bodies (Task 3 weights; Middleback reports)
           rho_b_mean=2.65, rho_b_min=2.50, rho_b_max=3.12,                                          # Change 1: basement density field
           k_b_median=1120.0, k_b_min=10.0, k_b_max=20000.0,                                          # Change 2: basement susceptibility field (L5-6); Change 4: median 1,120 (Grant and West Table 12-3, rhyolite)
           domain_km=30.0, texture_km=4.0, domain_share=0.8)                                          # Change 5: two-scale basement fields (both), share of variance at the domain scale; replaces the 20 km and 16 km single scales
LITH = {1: "Andamooka Limestone", 2: "Arcoona Quartzite", 3: "unnamed siltstones", 4: "Woomera Shale",
        5: "Pandurra Formation", 6: "basalt", 7: "basement", 8: "iron-oxide body"}

# ---- the draws, each tied to its citation row -------------------------------------------------------------------------
cited("L1-1", 320, 670, 0.46, 0.54, 0.075, 0.24, 0.23, 0.53)                               # Change 6 (2026-09-23): one draw, total cover to basement
cited("L1-2", 20, 10, 50); cited("L1-3", 0, 150); cited("L2-1", 2, 10); cited("L2-2", 2, 20, 75, 300)
cited("L2-3", 1, 18); cited("L3-1", 0.05, 0.30); cited("L3-2", 30, 150, 0.5, 5); cited("L4-1", 0, 15)
cited("L4-2", 0.09, 0.35); cited("L4-3", 1, 5); cited("L4-4", 1, 15, 1.0, 4.5)
cited("L5-1", 2.80, 0.12, 2.60, 3.35, 20, 26000); cited("L5-2", 2.60, 2.70, 2.10, 2.20, 2.44, 0.05, 10, 100, 1, 1000)
cited("L2-4", 0.3, 3, 3.0, 4.5); cited("L5-4", 0.03, 0.10, 0.5, 1.0)                        # Change 1 and 2 rows (2026-09-23), bundled in Change 6: iron-body size; density, basement density; susceptibility variation
U = lambda r, a, b: r.uniform(a, b)
LU = lambda r, a, b: float(np.exp(r.uniform(np.log(a), np.log(b))))

def draw(r):
    """one set of realization-level parameters; row ids in the keys"""
    return {"L1-1 cover_total_m": U(r, 320, 670),                       # Change 6: total cover to basement, one draw; units are fixed fractions of it
            "L1-2 corr_length_km": LU(r, 10, 50), "L1-3 relief_m": U(r, 0, 150),
            "L2-1 intensity_per_1e4km2": U(r, 2, 10), "L2-3 basalt_multiplier": U(r, 1, 18),
            "L3-1 p_reduced": U(r, 0.05, 0.30), "L3-2 belt_length_km": LU(r, 30, 150),
            "L4-1 reach_d_km": U(r, 0, 15), "L4-2 p_ore": U(r, 0.09, 0.35), "L4-3 ore_multiplier": U(r, 1, 5),
            "L5-2 rho_quartzite": U(r, 2.60, 2.70), "L5-2 rho_shale": U(r, 2.10, 2.60), "L5-2 rho_limestone": U(r, 2.20, 2.70),
            "L5-2 rho_pandurra": r.normal(2.44, 0.05), "L5-2 k_cover": LU(r, 10, 100), "L5-2 res_cover": LU(r, 1, 1000)}

def grf(r, lx_km, ly_km=None, az=0.0, pad=2):
    """zero-mean unit-variance Gaussian random field on the map grid; correlation lengths along az and across it"""
    ly_km = lx_km if ly_km is None else ly_km
    ny, nx = NY * pad, NX * pad
    kx = np.fft.fftfreq(nx, d=DX / 1e3) * 2 * np.pi; ky = np.fft.fftfreq(ny, d=DX / 1e3) * 2 * np.pi
    KX, KY = np.meshgrid(kx, ky); a = np.radians(az)
    kpar = KX * np.sin(a) + KY * np.cos(a); kper = KX * np.cos(a) - KY * np.sin(a)
    amp = np.exp(-((kpar * lx_km) ** 2 + (kper * ly_km) ** 2) / 8.0)
    f = np.real(np.fft.ifft2(np.fft.fft2(r.standard_normal((ny, nx))) * amp))[:NY, :NX]
    return (f - f.mean()) / f.std()

def ellipse(x0, y0, length_km, aspect, az):
    a = np.radians(az); dx, dy = (GX - x0) / 1e3, (GY - y0) / 1e3
    u = dx * np.sin(a) + dy * np.cos(a); v = dx * np.cos(a) - dy * np.sin(a)
    return (u / (length_km / 2)) ** 2 + (v / (length_km / 2 / aspect)) ** 2 <= 1.0

def weighted_points(r, n, weight, mask=None):
    """n random map points with probability proportional to weight (optionally inside mask); jittered inside cells"""
    w = weight.astype(float) * (1 if mask is None else mask)
    if n == 0 or w.sum() == 0: return np.empty(0), np.empty(0)
    idx = r.choice(w.size, size=n, p=(w / w.sum()).ravel())
    iy, ix = np.unravel_index(idx, w.shape)
    return XC[ix] + r.uniform(-DX / 2, DX / 2, n), YC[iy] + r.uniform(-DX / 2, DX / 2, n)

# ---- the five levels as stages; a branch is data that names its draw, stages, properties and summary (Section 7) ----------
def level1_frame(r, p, F):
    T0, lc = p["L1-1 cover_total_m"], p["L1-2 corr_length_km"]
    g = np.radians(r.uniform(0, 360))
    trend = ((GX - GX.mean()) * np.sin(g) + (GY - GY.mean()) * np.cos(g)) / (NX * DX / 2)
    total = np.clip(T0 * (1 + 0.20 * grf(r, lc) + 0.20 * trend), 50, None)          # total cover to basement (L1-1), one draw
    cover = total * 0.46                                                            # Stuart Shelf succession 0.46, Pandurra 0.54 (fixed shares, row L1-1)
    fl = 0.075                                                                      # Andamooka Limestone share of the succession (fixed, row L1-1)
    s1 = cover * fl; s2 = s1 + cover * (1 - fl) * 0.24; s3 = s2 + cover * (1 - fl) * 0.23; s4 = cover
    rel = grf(r, lc); rel = p["L1-3 relief_m"] * ((rel - rel.min()) / (rel.max() - rel.min()) - 0.5)
    return dict(cover=cover, s1=s1, s2=s2, s3=s3, s4=s4, base=total + rel)         # base = top of basement

def level2_basalt(r, p, F):
    lam, M2, fin = p["L2-1 intensity_per_1e4km2"], p["L2-3 basalt_multiplier"], IN_CIRCLE.mean()
    n_obj = r.poisson(lam * AREA_KM2 / 1e4)
    bx, by = weighted_points(r, n_obj, np.where(IN_CIRCLE, M2, 1.0) / (fin * M2 + (1 - fin)))
    btop = np.full((NY, NX), np.nan); bid = np.zeros((NY, NX), int); objs = []
    for j, (x, y) in enumerate(zip(bx, by), 1):
        L = LU(r, 2, 20); t = LU(r, 75, 300)
        rho = stats.truncnorm.rvs((2.60 - 2.80) / 0.12, (3.35 - 2.80) / 0.12, loc=2.80, scale=0.12, random_state=r)
        k = LU(r, 20, 26000)                                              # L5-1, corrected 2026-09-23 (Parasnis Table I is in rationalised units)
        m = ellipse(x, y, L, FIX["basalt_aspect"], FIX["basalt_az"])
        btop = np.where(m, np.maximum(F["base"] - t, F["s4"]), btop); bid[m] = j
        objs.append(dict(obj=j, x=x, y=y, length_km=L, thickness_m=t, rho=rho, k=k,
                         in_circle=bool(IN_CIRCLE[np.argmin(abs(YC - y)), np.argmin(abs(XC - x))])))
    basalt = bid > 0
    return dict(btop=btop, bid=bid, basalt=basalt, objs=objs, contact=np.where(basalt, btop, F["base"]))

def level3_redox(r, p, F):
    Lb = p["L3-2 belt_length_km"]
    red = grf(r, Lb / 3.0, Lb / 3.0 / FIX["belt_aspect"], FIX["belt_az"])
    return dict(reduced=red >= np.quantile(red, 1 - p["L3-1 p_reduced"]))

def level4_ore(r, p, F):
    d, basalt = p["L4-1 reach_d_km"], F["basalt"]
    if basalt.any():
        dist = np.where(basalt, ndimage.distance_transform_edt(basalt), ndimage.distance_transform_edt(~basalt)) * DX / 1e3
        zone = (dist <= max(d, 0.5)) & F["reduced"]
    else:
        zone = np.zeros_like(F["reduced"])
    M4, P = p["L4-3 ore_multiplier"], p["L4-2 p_ore"]
    Dg = np.exp(np.linspace(np.log(0.5), np.log(5), 2001)); mean_area = np.mean(np.pi * Dg ** 2 / 4)
    n_ore = r.poisson(P * zone.sum() * (DX / 1e3) ** 2 / mean_area) if zone.any() else 0
    fz = (zone & IN_CIRCLE).sum() / max(zone.sum(), 1)
    ox, oy = weighted_points(r, n_ore, np.where(IN_CIRCLE, M4, 1.0) / (fz * M4 + (1 - fz)), zone)
    ores = []
    for x, y in zip(ox, oy):
        Dk = LU(r, 0.5, 5); th = LU(r, 1, 15); gr = U(r, 1.0, 4.5)
        host = p["L5-2 rho_pandurra"]
        vf = gr / 100 / FIX["cu_in_ccp"] * host / FIX["rho_ccp"]; drho = vf * (FIX["rho_ccp"] - host)
        ix, iy = np.argmin(abs(XC - x)), np.argmin(abs(YC - y))
        ores.append(dict(x=x, y=y, diam_km=Dk, thick_m=th, grade=gr, drho=drho, depth_m=F["contact"][iy, ix],
                         Mt=np.pi * Dk ** 2 / 4 * 1e6 * th * (host + drho) / 1e6, in_circle=bool(IN_CIRCLE[iy, ix])))
    return dict(zone=zone, ores=ores)

def level2_iron(r, p, F):
    """Change 1: iron-oxide bodies (Middleback type) in the basement, top at the unconformity; second object population"""
    n_iron = r.poisson(FIX["iron_ratio"] * p["L2-1 intensity_per_1e4km2"] * AREA_KM2 / 1e4)
    ix_, iy_ = weighted_points(r, n_iron, np.ones((NY, NX)))
    iid = np.zeros((NY, NX), int); irons = []
    for j, (x, y) in enumerate(zip(ix_, iy_), 1):
        L = LU(r, 0.3, 3); rho = U(r, 3.0, 4.5)
        m = ellipse(x, y, L, FIX["iron_aspect"], FIX["iron_az"])
        if not m.any():                                                    # smaller than a cell: keep the nearest cell
            m[np.argmin(abs(YC - y)), np.argmin(abs(XC - x))] = True
        area = np.pi * L ** 2 / 4 / FIX["iron_aspect"]
        fill = min(1.0, area / (m.sum() * (DX / 1e3) ** 2))               # fraction of the marked cells the body fills (mass kept)
        iid[m] = j
        irons.append(dict(obj=j, x=x, y=y, length_km=L, rho=rho, fill=fill, area_km2=area, depth_m=F["base"][np.argmin(abs(YC - y)), np.argmin(abs(XC - x))]))
    return dict(iid=iid, irons=irons)

def level5_basement(r, p, F):
    """Change 1: a lateral basement density field; Change 2: an independent log-normal susceptibility field (both row L5-4 since Change 6)"""
    W = FIX["domain_share"]
    two_scale = lambda: np.sqrt(W) * grf(r, FIX["domain_km"]) + np.sqrt(1 - W) * grf(r, FIX["texture_km"])   # Change 5: domains plus texture, unit variance
    sd = U(r, 0.03, 0.10)                                                 # row L5-4, drawn here so that the earlier stages keep their seeds
    rb = np.clip(FIX["rho_b_mean"] + sd * two_scale(), FIX["rho_b_min"], FIX["rho_b_max"])
    sdk = U(r, 0.5, 1.0)                                                  # row L5-4, decades
    logk = np.clip(np.log10(FIX["k_b_median"]) + sdk * two_scale(), np.log10(FIX["k_b_min"]), np.log10(FIX["k_b_max"]))
    return dict(rho_base=rb, k_base=10.0 ** logk, basement_sd=sd, basement_logk_sd=sdk)

def level5_properties(p, F):
    z = ZC[None, None, :]
    lith = np.full((NY, NX, len(ZC)), 7, np.int8)
    for code, surf in [(1, F["s1"]), (2, F["s2"]), (3, F["s3"]), (4, F["s4"]), (5, F["base"])]:
        lith[(lith == 7) & (z < surf[:, :, None])] = code
    lith[(z >= F["btop"][:, :, None]) & (z < F["base"][:, :, None]) & F["basalt"][:, :, None]] = 6
    rho_u = {1: p["L5-2 rho_limestone"], 2: p["L5-2 rho_quartzite"], 3: p["L5-2 rho_shale"], 4: p["L5-2 rho_shale"],
             5: p["L5-2 rho_pandurra"]}
    rho3 = np.vectorize(lambda c: rho_u.get(c, np.nan))(lith).astype(np.float32)
    k3 = np.where(lith <= 5, p["L5-2 k_cover"], np.nan).astype(np.float32)
    res3 = np.where(lith <= 5, p["L5-2 res_cover"], FIX["res_basement"]).astype(np.float32)
    base3 = lith == 7                                                     # basement takes the Change 1 field, column by column
    rho3 = np.where(base3, F["rho_base"][:, :, None].astype(np.float32), rho3); k3 = np.where(base3, F["k_base"][:, :, None].astype(np.float32), k3)
    for o in F["objs"]:
        m3 = (lith == 6) & (F["bid"][:, :, None] == o["obj"])
        rho3[m3], k3[m3] = o["rho"], o["k"]
    res3[lith == 6] = FIX["res_basalt"]
    for o in F["irons"]:                                                  # iron-oxide bodies: basement cells from the unconformity down 200 m
        m3 = base3 & (F["iid"][:, :, None] == o["obj"]) & (z >= F["base"][:, :, None]) & (z < F["base"][:, :, None] + FIX["iron_thick_m"])
        lith[m3] = 8
        rho3[m3] = rho3[m3] + o["fill"] * (o["rho"] - rho3[m3]); k3[m3] = k3[m3] + o["fill"] * (FIX["k_iron"] - k3[m3])
    return dict(lith=lith, rho=rho3, k=k3, res=res3)

def sh_summary(p, F):
    objs, ores = F["objs"], F["ores"]
    return {"L5-4 basement_sd": F["basement_sd"], "L5-4 basement_logk_sd": F["basement_logk_sd"], **dict(n_basalt=len(objs), basalt_frac=F["basalt"].mean(), reduced_frac=F["reduced"].mean(),
                n_iron=len(F["irons"]), basement_sd_realized=F["rho_base"].std(), basement_logk_sd_realized=np.log10(F["k_base"]).std(),
                zone_km2=F["zone"].sum() * (DX / 1e3) ** 2, n_ore=len(ores), Mt_total=sum(o["Mt"] for o in ores),
                contrast=np.mean([o["rho"] for o in objs]) - p["L5-2 rho_pandurra"] if objs else np.nan)}

BRANCH_SH = dict(name="sediment-hosted Cu, Annex A", citation_table="01_citation_table/wp4_annexA_citation_table_draft.csv",
                 geometry_family="flat-lying cover stack; flow-pile ellipses on the basement surface",
                 mineralization_rule="ore disks in the margin zone: within d of a basalt edge and on a reduced belt",
                 draw=draw, stages=[level1_frame, level2_basalt, level3_redox, level4_ore, level2_iron, level5_basement],   # Change 1 stages last: earlier draws unchanged
                 properties=level5_properties, summary=sh_summary)

def realize_branch(branch, seed, keep_volume=False):
    """one realization of any branch: draw, run the stages in order, attach properties; seed -> numpy default_rng(seed)"""
    r = np.random.default_rng(seed); p = branch["draw"](r); F = {}
    for stage in branch["stages"]:
        F.update(stage(r, p, F))
    out = {"seed": seed, **p, **branch["summary"](p, F)}
    if keep_volume:
        F.update(branch["properties"](p, F))
    maps = {k: v for k, v in F.items() if k not in ("objs", "ores", "basalt", "s4", "basement_sd", "basement_logk_sd")}    # irons (list) stays for plotting
    return out, maps, pd.DataFrame(F["objs"]), pd.DataFrame(F["ores"])

def realize(seed, keep_volume=False):
    return realize_branch(BRANCH_SH, seed, keep_volume)

