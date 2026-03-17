# Projekt-Pitch: Baukosten-Prädiktion aus Holzbau-Kennzahlen

**Zielgruppe:** Dozierende  
**Projekt:** Probabilistische Analyse von Baukosten  
**Stand:** März 2025

---

## 1. Ausgangslage

Baukosten sind schwer vorherzusagen. Investoren, Bauherren und Planer benötigen verlässliche Schätzungen, um Budgets zu planen und Risiken zu bewerten. Bisherige Ansätze stützen sich oft auf Erfahrungswerte oder grobe Faustformeln. Ein datengetriebenes Modell, das Baukosten aus wenigen, früh verfügbaren Parametern ableitet, könnte die Planungssicherheit erhöhen.

---

## 2. Projektziel

**Prädiktion der Baukosten (CHF/m²) auf Basis von vier zentralen Parametern:**

| Parameter | Beschreibung | Ausprägungen im Datensatz |
|-----------|--------------|---------------------------|
| **Geschoss** | Anzahl Geschosse / Gebäudehöhe | 3, 4, 5, 6, 7, 8 (aus Typologie extrahierbar) |
| **Material** | Bauweise / Konstruktionstyp | Rahmenbauweise, Massivbauweise (Holz) |
| **Untergeschoss** | Vorhandenheit unterirdischer Nutzung | Vorhanden (inkl. Tiefgarage), Nicht vorhanden |
| **Bauherrschaft** | Bauherrentyp | Privat, Institutionell, Genossenschaft, Institution |

**Zielvariable:** Baukosten pro m² Hauptnutzfläche (BKP 1–5 / m² HNF oder BKP 2 / m² HNF), indexiert auf 04.2023.

---

## 3. Datengrundlage

**Quelle:** Lignum & Bundesamt für Umwelt – *Holzbaukennzahlen für Investoren – Wohnbauten* (Abschlussbericht 120135)

- **18 Fallbeispiele** Schweizer Wohnbauten in Holzbauweise (2019–2022)
- **17 Neubauten**, 1 Sanierung/Aufstockung
- Vollständige Kennwerte: Volumen (GV), Flächen (GF, HNF), Baukosten (BKP 1–5, BKP 2, BKP 214), Wirtschaftlichkeit, Nachhaltigkeit

**Datenformat:** CSV (`data/holzbaukennzahlen_fallbeispiele.csv`), Semikolon-getrennt, UTF-8

---

## 4. Methodischer Ansatz

1. **Feature-Engineering**
   - Geschosszahl aus Typologie extrahieren (z.B. „6-geschossig“ → 6)
   - Material: Rahmenbauweise vs. Massivbauweise (binär oder kategorial)
   - Untergeschoss: aus Spalte `tiefgarage` ableiten (Tiefgarage impliziert Untergeschoss)
   - Bauherrschaft: kategorial (4 Klassen)

2. **Modellierung**
   - Lineare Regression als Baseline
   - Ggf. Ridge/Lasso bei Multikollinearität
   - Optional: einfache Ensemble-Methoden (Random Forest) zur Exploration nicht-linearer Effekte

3. **Validierung**
   - Leave-one-out oder k-fold Cross-Validation (kleiner Datensatz)
   - Metriken: RMSE, MAE, R²
   - Sensitivitätsanalyse der Koeffizienten

4. **Probabilistische Erweiterung**
   - Residuenverteilung modellieren
   - Konfidenzintervalle für Punktprädiktionen
   - Anbindung an Monte-Carlo-Simulation für Kostenrisiko (Überschreitungswahrscheinlichkeiten)

---

## 5. Erwartete Herausforderungen

| Herausforderung | Möglicher Umgang |
|----------------|------------------|
| Kleiner Stichprobenumfang (n=18) | Strikte Validierung, Vorsicht bei Überinterpretation |
| Ranges statt exakter Werte (GV, GF, HNF) | Mittelwerte oder Kategorien nutzen |
| Fehlende BKP-214-Werte bei einigen Projekten | Nur BKP 1–5 / BKP 2 als Zielvariable |
| Heterogenität (Neubau vs. Sanierung) | Fall 18 ggf. ausschliessen oder separat modellieren |

---

## 6. Erwarteter Nutzen

- **Praktisch:** Frühe Kostenschätzung aus wenigen, planungsrelevanten Parametern
- **Methodisch:** Verknüpfung von deterministischer Prädiktion mit probabilistischer Risikoanalyse
- **Wissenschaftlich:** Nutzung eines strukturierten Schweizer Holzbau-Datensatzes für Baukostenforschung

---

## 7. Nächste Schritte

1. Feature-Extraktion aus CSV (Geschoss, Material, Untergeschoss, Bauherrschaft)
2. Deskriptive Analyse und Visualisierung
3. Modellentwicklung und Validierung
4. Probabilistische Erweiterung
5. Kurzbericht mit Ergebnissen und Limitationen

---

*Projekt-Repository: `cost-overruns` | Daten: `data/holzbaukennzahlen_fallbeispiele.csv`*
