# CO₂ Probability — Building GHG Prediction

A small research-style project for probabilistic prediction of building greenhouse-gas intensity (`GHG_sum_em_m2a`) from early-stage building parameters, using statistical modelling and Monte Carlo simulation in Python.

*Academic mini-challenge on probabilistic modelling of whole-life carbon for buildings.*

**Data:** [CarbEnMats GBDB](https://github.com/mroeck/carbenmats-buildings)

---

## Project Structure

```
co2-probability/
├── data/
│   ├── raw/           # Original GBDB files (see data/README.md)
│   └── processed/     # Cleaned and transformed data
├── notebooks/         # Jupyter notebooks for exploration and analysis
├── src/               # Main package (to be implemented)
├── docs/              # Project pitch and data notes
├── reports/           # Written reports and outputs
├── figures/           # Saved plots and visualisations
├── tests/             # Unit tests
├── pyproject.toml
└── README.md
```

---

## Setup

### Prerequisites

- [uv](https://docs.astral.sh/uv/) — fast Python package and project manager

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Create environment and install dependencies

```bash
uv sync
```

---

## Usage

```bash
uv run jupyter notebook
uv run pytest
```

---

## Docs

Shareable project pitch: [`docs/index.html`](docs/index.html) (source: [`docs/projekt_pitch.md`](docs/projekt_pitch.md))

---

## License

MIT (or as required by your institution). Upstream GBDB data is GPL-3.0 — comply with that license when redistributing derived data.
