# Data

Datasets for probabilistic prediction of building GHG intensity (`GHG_sum_em_m2a`).

## Folder Structure

- `raw/` — Original, unprocessed data files
- `processed/` — Cleaned and transformed datasets ready for analysis

---

## CarbEnMats / GBDB

**Primary dataset for this project**

| Field | Value |
|-------|-------|
| **Title** | Global Buildings Database Seed on Whole Life Carbon, Energy Performance, and Material Intensity (GBDB CarbEnMats) |
| **Source** | [mroeck/carbenmats-buildings](https://github.com/mroeck/carbenmats-buildings) |
| **Attributes** | [gbdb_attributes.xlsx](https://github.com/mroeck/carbenmats-buildings/blob/main/gbdb_attributes.xlsx) |
| **Data** | [gbdb_data.xlsx](https://github.com/mroeck/carbenmats-buildings/blob/main/gbdb_data.xlsx) |
| **License** | GNU GPL v3.0 |

### Citation

- Descriptor: https://zenodo.org/doi/10.5281/zenodo.8378938
- Dataset: https://zenodo.org/doi/10.5281/zenodo.8363894

### Usage

Place downloaded GBDB files (e.g. `gbdb_data.xlsx`, `gbdb_attributes.xlsx`) in `data/raw/`. Raw Excel/CSV files are excluded from version control via `.gitignore`.
