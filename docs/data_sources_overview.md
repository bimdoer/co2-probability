# Data Sources Overview

Overview of the dataset used for probabilistic prediction of building GHG intensity (`GHG_sum_em_m2a`) from early-stage building parameters.

| Dataset / Source | Region | Project Type | Main Variables | Target Directly Available | Data Format / Accessibility | Advantage | Disadvantage |
|------------------|--------|--------------|----------------|---------------------------|-----------------------------|-----------|--------------|
| **CarbEnMats GBDB** ([GitHub](https://github.com/mroeck/carbenmats-buildings)) | Global | Buildings (mixed use) | Structure, roof, GFA, volume, floors AG/BG, use type/subtype, WLC/GHG, energy, materials | ✔️ Yes (`GHG_sum_em_m2a`) | XLSX / CSV via GitHub & Zenodo (GPL-3.0) | Large open WLC database (>1'200 cases); rich attribute dictionary | Heterogeneous LCA scopes and reporting quality across sources |

## Selected predictors (this project)

| Attribute | Description |
|-----------|-------------|
| `bldg_struct_type` | Structure type and main material |
| `bldg_roof_type` | Roof type in terms of geometry |
| `bldg_area_gfa` | Gross Floor Area (m²) |
| `bldg_volume_gbv` | Gross building volume (m³) |
| `bldg_floors_ag` | Floors above ground |
| `bldg_floors_bg` | Floors below ground |
| `bldg_use_type` | Building type |
| `bldg_use_subtype` | Building sub typology |

## Target

| Attribute | Description |
|-----------|-------------|
| `GHG_sum_em_m2a` | Summed GHG emissions intensity per m² and year |

## Key files

- Attributes: [gbdb_attributes.xlsx](https://github.com/mroeck/carbenmats-buildings/blob/main/gbdb_attributes.xlsx)
- Data: [gbdb_data.xlsx](https://github.com/mroeck/carbenmats-buildings/blob/main/gbdb_data.xlsx)
- Descriptor (preprint): https://zenodo.org/doi/10.5281/zenodo.8378938
- Dataset DOI: https://zenodo.org/doi/10.5281/zenodo.8363894
