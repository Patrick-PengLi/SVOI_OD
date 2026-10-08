

## Update 2026-10-02

# 04_prior_predictive_observed

- `gravity_stations_pre1975_full_surveys.csv`: every station of BMR helicopter gravity surveys 196953 and 196955 (1969), 1,912 stations over 132-138 E, 28-31 S, extracted 2026-10-02 from the GA 2019 National Gravity Grids point-located data (`geophysics/ga_national/gravity_national_points/133023_11_0.zip`, same columns as the ASEG-GDF2 .dfn). The notebook clips it by the study window exactly as it clips the P234 lines; 398 stations fall on the Andamooka sheet.
- `P234-line-magnetic-AWAGS_MAG_2010.nc` and its `.npz` cache: the complete 1962 P234 aeromagnetic survey (305,634 valid readings, 136.4-138.1 E, 30-32 S).
