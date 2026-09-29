# Projekt-Pitch: CO₂-Prädiktion aus Gebäudeparametern

**Zielgruppe:** Dozierende  
**Projekt:** Probabilistische Analyse von Gebäude-Treibhausgasemissionen  
**Stand:** September 2025

---

## 1. Ausgangslage

Whole-Life-Carbon (WLC) von Gebäuden ist zentral für Klimastrategien in Planung und Politik – aber früh belastbare Schätzungen fehlen oft. Viele LCA-Studien sind aufwändig und kommen erst spät im Prozess. Ein datengetriebenes Modell, das die flächenbezogene Treibhausgasintensität aus wenigen, früh verfügbaren Gebäudeparametern ableitet, könnte Benchmarking und Risikoabschätzung in frühen Phasen verbessern.

---

## 2. Projektziel

**Prädiktion der flächenbezogenen GHG-Emissionen auf Basis zentraler Gebäudeparameter:**

| Attribut | Beschreibung |
|----------|--------------|
| **bldg_struct_type** | Structure type and main material |
| **bldg_roof_type** | Roof type in terms of geometry |
| **bldg_area_gfa** | Gross Floor Area (m²) |
| **bldg_volume_gbv** | Gross building volume (m³), inkl. Volumen von Wänden und Dächern |
| **bldg_floors_ag** | Number of floors above ground |
| **bldg_floors_bg** | Number of floors below ground |
| **bldg_use_type** | Building type |
| **bldg_use_subtype** | Building sub typology |

**Zielvariable:** `GHG_sum_em_m2a` — summierter GHG-Emissionswert pro m² und Jahr (Whole-Life-Carbon-Intensität).

---

## 3. Datengrundlage

**Quelle:** CarbEnMats / GBDB – *Global Buildings Database Seed on Whole Life Carbon, Energy Performance, and Material Intensity* ([mroeck/carbenmats-buildings](https://github.com/mroeck/carbenmats-buildings))

- Mehr als **1'200 Gebäude-Fallstudien** weltweit
- Über **5'000'000 m²** erfasste Nutzfläche
- Attribute zu Kontext, Entwurf, LCA-Methode, Energie, Materialintensität und GHG über Lebenszyklusphasen
- Lizenz: GNU GPL v3.0

**Relevante Dateien:**

| Datei | Inhalt |
|-------|--------|
| [gbdb_attributes.xlsx](https://github.com/mroeck/carbenmats-buildings/blob/main/gbdb_attributes.xlsx) | Attributbeschreibungen |
| [gbdb_data.xlsx](https://github.com/mroeck/carbenmats-buildings/blob/main/gbdb_data.xlsx) | Gebäude-Datensatz (CORE + FULL) |

Zusätzlich verfügbar: CSV-Varianten (`gbdb_data_core.csv`, `gbdb_data_full.csv`), Zenodo-Releases und Data-Descriptor-Preprint.

---

## 4. Methodischer Ansatz

1. **Datenaufbereitung**
   - Attribute und Zielvariable aus GBDB extrahieren
   - Fehlende Werte und Ausreisser prüfen
   - Kategoriale Features (Struktur, Dach, Nutzung) enkodieren
   - Numerische Features (Fläche, Volumen, Geschosse) skalieren / transformieren

2. **Modellierung**
   - Lineare Regression als Baseline
   - Ggf. Ridge/Lasso bei Multikollinearität (z.B. Fläche vs. Volumen)
   - Optional: Random Forest / Gradient Boosting zur Exploration nicht-linearer Effekte

3. **Validierung**
   - Train/Test-Split und k-fold Cross-Validation
   - Metriken: RMSE, MAE, R²
   - Residualanalyse und Plausibilitätschecks gegen bekannte WLC-Benchmarks

4. **Probabilistische Erweiterung**
   - Residuenverteilung modellieren
   - Konfidenzintervalle für Punktprädiktionen
   - Monte-Carlo-Simulation für Überschreitungswahrscheinlichkeiten (z.B. Grenzwert in kg CO₂e/m²a)

---

## 5. Erwartete Herausforderungen

| Herausforderung | Möglicher Umgang |
|-----------------|------------------|
| Heterogene Quellen und LCA-Scopes | Scope-Filter; ggf. nur CORE-Datensatz oder einheitliche Systemgrenzen |
| Fehlende Werte bei einzelnen Attributen | Imputation oder fallweise Ausschluss; Sensitivitätsanalyse |
| Multikollinearität (GFA ↔ Volumen ↔ Geschosse) | Regularisierung, Feature-Auswahl, VIF-Checks |
| Regionale und typologische Heterogenität | Stratifizierung nach `bldg_use_type` / Subtyp; ggf. separate Modelle |
| Unterschiedliche Reporting-Qualität in Fallstudien | Qualitätsfilter laut Attributdokumentation; Robustheitschecks |

---

## 6. Erwarteter Nutzen

- **Praktisch:** Frühe CO₂-Schätzung aus wenigen, planungsrelevanten Gebäudeparametern
- **Methodisch:** Verknüpfung von deterministischer Prädiktion mit probabilistischer Risikoanalyse
- **Wissenschaftlich:** Nutzung eines offenen, internationalen Whole-Life-Carbon-Datensatzes für Benchmarking und Modellierung

---

## 7. Nächste Schritte

1. Attribute und `GHG_sum_em_m2a` aus GBDB laden und bereinigen
2. Deskriptive Analyse und Visualisierung
3. Modellentwicklung und Validierung
4. Probabilistische Erweiterung (Konfidenzintervalle, Monte Carlo)
5. Kurzbericht mit Ergebnissen und Limitationen

---

*Projekt-Repository: `co2-probability` | Daten: CarbEnMats GBDB (`gbdb_data.xlsx`)*
