# Construction Cost Overruns — Probabilistic Analysis

A small research-style project for probabilistic analysis of cost overruns in construction projects using Monte Carlo simulation and statistical exploration in Python.

*This project is for an academic mini-challenge on probabilistic modelling of construction cost overruns.*

---

## Project Structure

```
cost-overruns/
├── data/
│   ├── raw/           # Original, unprocessed data (see data/README.md for sources)
│   └── processed/     # Cleaned and transformed data
├── notebooks/         # Jupyter notebooks for exploration and analysis
├── src/
│   └── cost_overruns/ # Main package
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

Install `uv` if you don't have it:

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

### Create and Activate Environment

```bash
# Create virtual environment and install dependencies
uv sync

# Activate the environment (optional; uv run works without activation)
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

### Install Dependencies

Dependencies are declared in `pyproject.toml`. Run:

```bash
uv sync
```

This creates the virtual environment and installs all dependencies.

---

## Usage

### Run Notebooks

```bash
uv run jupyter notebook
```

Or open notebooks directly in VS Code / Cursor.

### Run Tests

```bash
uv run pytest
```

---

## License

MIT (or as required by your institution)
