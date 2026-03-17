# Data Sources Overview

Overview of datasets and sources considered for probabilistic analysis of construction cost overruns.

| Dataset / Source | Region | Project Type | Main Variables | Cost Overrun Directly Available | Data Format / Accessibility | Advantage | Disadvantage |
|------------------|--------|--------------|----------------|--------------------------------|-----------------------------|-----------|--------------|
| **Swiss Construction Price Index (BFS)** | Switzerland | Building + Civil Engineering | Construction price index, region, building type, time series | ❌ No | CSV / Tables via BFS & opendata.swiss | Real Swiss cost dynamics, long time series | No project-level data |
| **Construction Activity Statistics (BFS)** | Switzerland | Residential + Building | Construction investments, building type, construction volume, region | ❌ No | Tables / Open Data | Good overview of project sizes and construction volume | No actual project costs |
| **Building and Dwelling Register (GWR)** | Switzerland | Residential / Buildings | Year of construction, use, floors, dwellings, building type | ❌ No | Open Data | Very detailed building characteristics (complexity) | No cost information |
| **Cantonal Supplementary Credit Reports** | Switzerland | Public Construction Projects | Project name, original credit, supplementary credit, justification | ⚠️ Indirect | PDF / Political documents | Direct indications of cost overruns | Data difficult to structure |
| **Flyvbjerg Megaproject Dataset** | International | Infrastructure | Planned costs, actual costs, construction time, project type | ✔️ Yes | Research dataset | Well-known, good overrun distributions | Focus on infrastructure, little building construction |
| **Global Rail Megaproject Dataset** | International | Rail Projects | Cost overrun %, schedule delay, project costs | ✔️ Yes | GitHub Dataset | Clean overrun data | Rail projects only |
| **Construction Project Cost Dataset (Kaggle)** | International | Mixed Construction | estimated_cost, actual_cost, project_duration, team_size | ✔️ Yes | CSV / Kaggle | Easy to analyse | Origin and quality partly unclear |
