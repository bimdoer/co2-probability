"""Explorative Analyse der Pitch-Variablen gegen GHG_sum_em_m2a.

Liest data/raw/gbdb_data_full.csv und schreibt die Abbildungen nach figures/.
Die Rohdatei ist nicht im Git; Download siehe data/README.md.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "gbdb_data_full.csv"
FIG = ROOT / "figures"

PREDS = [
    "bldg_struct_type",
    "bldg_roof_type",
    "bldg_area_gfa",
    "bldg_volume_gbv",
    "bldg_floors_ag",
    "bldg_floors_bg",
    "bldg_use_type",
    "bldg_use_subtype",
]
TARGET = "GHG_sum_em_m2a"
INK = "#1f2933"
BAR = "#3d5a80"
MUTED = "#9aa5b1"
ACCENT = "#c44900"


def load() -> pd.DataFrame:
    if not DATA.exists():
        raise FileNotFoundError(
            f"{DATA} fehlt. gbdb_data_full.csv nach data/raw/ legen "
            "(siehe data/README.md)."
        )
    cols = PREDS + [TARGET, "site_region_geoscheme", "scope_LCS_B6"]
    return pd.read_csv(
        DATA,
        sep=";",
        usecols=cols,
        na_values=["No data", "no data", "NA", "N/A", ""],
        low_memory=False,
    )


def _style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.edgecolor": "#d9e2ec",
            "axes.labelcolor": INK,
            "xtick.color": INK,
            "ytick.color": INK,
            "text.color": INK,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": False,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.titlesize": 12,
            "axes.titleweight": "bold",
            "axes.labelsize": 10,
        }
    )


def _save(fig: plt.Figure, name: str) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG / name, dpi=140, bbox_inches="tight")
    plt.close(fig)


def plot_target(y: pd.Series) -> None:
    edges = [0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 30, 70]
    labels = ["0–2", "2–4", "4–6", "6–8", "8–10", "10–12", "12–14", "14–16", "16–20", "20–30", "30+"]
    counts = pd.cut(y, bins=edges, labels=labels, right=False).value_counts().reindex(labels)
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.bar(labels, counts.to_numpy(), color=BAR, width=0.86)
    ax.set_title("Gebäude je Klasse der GHG-Intensität")
    ax.set_xlabel("GHG_sum_em_m2a (kg CO₂e/m²·a)")
    ax.set_ylabel("Anzahl Gebäude")
    for i, n in enumerate(counts.to_numpy()):
        ax.text(i, n + 4, str(int(n)), ha="center", va="bottom", fontsize=8, color=INK)
    ax.set_ylim(0, counts.max() * 1.18)
    _save(fig, "eda_zielverteilung.png")


def plot_missing(df: pd.DataFrame) -> None:
    labels = [
        "Volumen",
        "Geschosse UG",
        "Dachtyp",
        "Geschosse OG",
        "Strukturtyp",
        "Bruttogeschossfläche",
        "Nutzungssubtyp",
        "Ziel GHG",
        "Nutzungstyp",
    ]
    cols = [
        "bldg_volume_gbv",
        "bldg_floors_bg",
        "bldg_roof_type",
        "bldg_floors_ag",
        "bldg_struct_type",
        "bldg_area_gfa",
        "bldg_use_subtype",
        TARGET,
        "bldg_use_type",
    ]
    pct = [100 * df[c].isna().mean() for c in cols]
    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    y = np.arange(len(labels))
    colors = [ACCENT if p >= 80 else BAR for p in pct]
    ax.barh(y, pct, color=colors, height=0.72)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Fehlende Angaben (% der 1'294 Gebäude)")
    ax.set_title("Fehlende Werte der Pitch-Variablen")
    for i, p in enumerate(pct):
        ax.text(p + 1.2, i, f"{p:.1f}", va="center", fontsize=8, color=INK)
    _save(fig, "eda_fehlend.png")


def _median_bars(categories: list[str], values: list[float], title: str, name: str, xlabel: str) -> None:
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    y = np.arange(len(categories))
    ax.barh(y, values, color=BAR, height=0.72)
    ax.axvline(10.58, color=ACCENT, linestyle="--", linewidth=1, label="Gesamtmedian 10.6")
    ax.set_yticks(y, categories)
    ax.invert_yaxis()
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.55, -0.18))
    for i, v in enumerate(values):
        ax.text(v + 0.15, i, f"{v:.1f}", va="center", fontsize=8, color=INK)
    ax.set_xlim(0, max(values) * 1.18)
    _save(fig, name)


def plot_structure(df: pd.DataFrame) -> None:
    order = [
        ("frame steel", "Stahlrahmen"),
        ("massive brick", "Massiv Ziegel"),
        ("massive wood", "Massiv Holz"),
        ("frame concrete", "Betonrahmen"),
        ("massive concrete", "Massiv Beton"),
        ("frame wood", "Holzrahmen"),
    ]
    labels, values = [], []
    for key, label in order:
        part = df.loc[df["bldg_struct_type"] == key, TARGET].dropna()
        labels.append(f"{label} ({len(part)})")
        values.append(float(part.median()))
    missing = df.loc[df["bldg_struct_type"].isna(), TARGET].dropna()
    labels.append(f"Fehlend ({len(missing)})")
    values.append(float(missing.median()))
    _median_bars(
        labels,
        values,
        "Median-Intensität nach Strukturtyp",
        "eda_struktur.png",
        "Median GHG_sum_em_m2a (kg CO₂e/m²·a)",
    )


def plot_subtype(df: pd.DataFrame) -> None:
    order = [
        ("Multi-family house", "Mehrfamilienhaus"),
        ("Single family house", "Einfamilienhaus"),
        ("Retail and Restaurant", "Handel"),
        ("Semi-detached", "Doppelhaushälfte"),
        ("School and Daycare", "Schule / Kita"),
        ("Office", "Büro"),
        ("Row house", "Reihenhaus"),
    ]
    labels, values = [], []
    for key, label in order:
        part = df.loc[df["bldg_use_subtype"] == key, TARGET].dropna()
        labels.append(f"{label} ({len(part)})")
        values.append(float(part.median()))
    _median_bars(
        labels,
        values,
        "Median-Intensität nach Nutzungssubtyp",
        "eda_nutzung.png",
        "Median GHG_sum_em_m2a (kg CO₂e/m²·a)",
    )


def plot_gfa(df: pd.DataFrame) -> None:
    edges = [0, 500, 1000, 2000, 5000, 10000, 20000, 50000, 1e9]
    labels = ["<0.5", "0.5–1", "1–2", "2–5", "5–10", "10–20", "20–50", ">50"]
    g = df[["bldg_area_gfa", TARGET]].dropna()
    g["bin"] = pd.cut(g["bldg_area_gfa"], bins=edges, labels=labels, right=False)
    med = g.groupby("bin", observed=False)[TARGET].median()
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.bar(labels, med.to_numpy(), color=BAR, width=0.86)
    ax.axhline(10.58, color=ACCENT, linestyle="--", linewidth=1, label="Gesamtmedian 10.6")
    ax.set_title("Median-Intensität nach Bruttogeschossfläche")
    ax.set_xlabel("Bruttogeschossfläche (1'000 m²)")
    ax.set_ylabel("Median GHG_sum_em_m2a (kg CO₂e/m²·a)")
    ax.legend(frameon=False)
    for i, v in enumerate(med.to_numpy()):
        ax.text(i, v + 0.25, f"{v:.1f}", ha="center", va="bottom", fontsize=8)
    ax.set_ylim(0, med.max() * 1.2)
    _save(fig, "eda_flaeche.png")


def plot_floors(df: pd.DataFrame) -> None:
    fa = df[["bldg_floors_ag", TARGET]].dropna()
    fa["floors"] = fa["bldg_floors_ag"].clip(upper=12).round().astype(int)
    keep = [1, 2, 3, 4, 5, 6, 7, 8, 12]
    labels = ["1", "2", "3", "4", "5", "6", "7", "8", "12+"]
    med = []
    for k in keep:
        med.append(float(fa.loc[fa["floors"] == k, TARGET].median()))
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.bar(labels, med, color=BAR, width=0.86)
    ax.axhline(10.58, color=ACCENT, linestyle="--", linewidth=1, label="Gesamtmedian 10.6")
    ax.set_title("Median-Intensität nach oberirdischen Geschossen")
    ax.set_xlabel("Geschosse oberirdisch (12+ zusammengefasst)")
    ax.set_ylabel("Median GHG_sum_em_m2a (kg CO₂e/m²·a)")
    ax.legend(frameon=False)
    ax.set_ylim(0, max(med) * 1.25)
    _save(fig, "eda_geschosse.png")


def plot_context(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6))

    b6_order = [("Yes", "B6 enthalten"), ("No", "B6 nicht enthalten")]
    b6_vals = [float(df.loc[df["scope_LCS_B6"] == k, TARGET].median()) for k, _ in b6_order]
    miss = float(df.loc[df["scope_LCS_B6"].isna(), TARGET].median())
    axes[0].bar(["B6 enthalten", "B6 fehlt", "Angabe fehlt"], b6_vals + [miss], color=[BAR, ACCENT, MUTED])
    axes[0].set_title("Median nach Betriebsenergie-Scope")
    axes[0].set_ylabel("Median GHG_sum_em_m2a (kg CO₂e/m²·a)")
    for i, v in enumerate(b6_vals + [miss]):
        axes[0].text(i, v + 0.2, f"{v:.1f}", ha="center", fontsize=8)
    axes[0].set_ylim(0, 14)

    reg = (
        df.groupby("site_region_geoscheme")[TARGET]
        .agg(n="count", median="median")
        .sort_values("median")
    )
    names = {
        "Western Asia": "Westasien",
        "Eastern Asia": "Ostasien",
        "Western Europe": "Westeuropa",
        "Northern Europe": "Nordeuropa",
        "Northern America": "Nordamerika",
        "Southern Europe": "Südeuropa",
        "South-eastern Asia": "Südostasien",
        "South America": "Südamerika",
        "Australia and New Zealand": "Australien / NZ",
    }
    labels = [f"{names.get(i, i)} ({int(reg.loc[i, 'n'])})" for i in reg.index]
    axes[1].barh(labels, reg["median"].to_numpy(), color=BAR, height=0.72)
    axes[1].set_xlabel("Median (kg CO₂e/m²·a)")
    axes[1].set_title("Median nach Weltregion")
    fig.tight_layout()
    _save(fig, "eda_scope_region.png")


def main() -> None:
    _style()
    df = load()
    y = df[TARGET].dropna()
    plot_target(y)
    plot_missing(df)
    plot_structure(df)
    plot_subtype(df)
    plot_gfa(df)
    plot_floors(df)
    plot_context(df)
    print(f"Abbildungen geschrieben nach {FIG}")


if __name__ == "__main__":
    main()
