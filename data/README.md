# Data

This folder contains datasets used for probabilistic analysis of construction cost overruns.

## Folder Structure

- `raw/` — Original, unprocessed data files
- `processed/` — Cleaned and transformed datasets ready for analysis

---

## Construction Project Cost Data (Kaggle)

**Dataset used in this project**

| Field | Value |
|-------|-------|
| **Title** | Construction Project Cost Data |
| **Author** | prasadahirekar |
| **Source** | [Kaggle](https://www.kaggle.com/datasets/prasadahirekar/construction-project-cost-data) |
| **Download** | [construction_project_data.csv](https://www.kaggle.com/datasets/prasadahirekar/construction-project-cost-data?resource=download) |
| **License** | *See dataset page on Kaggle — verify and comply with the license shown there.* |

### Attribution

This dataset is used under the terms of its license on Kaggle. When using or publishing results based on this data, provide attribution:

- **Author:** prasadahirekar  
- **Dataset:** Construction Project Cost Data  
- **Source:** https://www.kaggle.com/datasets/prasadahirekar/construction-project-cost-data  

### Variables

- `Project_ID`, `Project_Name`
- `Cost_Estimate`, `Actual_Cost`
- `Start_Date`, `End_Date`
- `Risk_Factor`, `Region`

### Usage

Place `construction_project_data.csv` in `data/raw/`. The file is excluded from version control via `.gitignore`. Others must download it from Kaggle (free account required).
