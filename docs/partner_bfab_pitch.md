# Kooperationsangebot: Kostenprognose aus Projektdaten

**An:** bfab.ch  
**Von:** Studiengang Data Science & AI, FHNW; Co-Partner: bimdo GmbH  
**Modul:** Wahrscheinlichkeitsrechnen  
**Stand:** März 2025

---

## Zweck des Dokuments

Beschreibung eines studentischen Projekts im Modul Wahrscheinlichkeitsrechnen: Aufbau eines probabilistischen Modells zur Schätzung von Baukosten pro m² und/oder m³ aus historischen Kostendaten. Das Dokument fasst Rahmen, Anforderungen an bfab, Datenschutz und Lizenzierung zusammen.

---

## Herausforderung

Viele Kostenmodelle stützen sich auf **fremde Daten** und **proprietäre Berechnungsmodelle**; die zugrunde liegende Logik ist für Nutzerinnen und Nutzer oft nicht nachvollziehbar.

**Ziel dieses Projekts** ist deshalb, ein **Open-Source-Wahrscheinlichkeitsmodell** zu entwickeln — **einsehbar** in Code und Dokumentation — für die Kalkulation von **Preisen pro m² und m³**, **basierend auf den eigenen Daten**, nicht auf undokumentierten Fremdreferenzen.

---

## Inhalt des Projekts

- **Zielvariable:** Kostenindikatoren pro m² und/oder pro m³, abhängig von Datenlage und Definitionen bei bfab.
- **Input:** Strukturierte, historische Projektkostendaten sowie Projektmerkmale; Abstimmung mit den internen Kalkulationslogiken von bfab.
- **Methode:** Wahrscheinlichkeitsrechnung / probabilistische Modellierung (z. B. Modellierung von Unsicherheit, nicht nur Punktprognosen).
- **Ergebnis für bfab:** Dokumentierter Prototyp zur Berechnung bzw. probabilistischen Schätzung von Kostendaten aus den bereitgestellten Projektdaten (z. B. als Pipeline oder kleines Werkzeug).

---

## Erwarteter Mehrwert für bfab

- **Externe Einordnung der Datengrundlage:** Blick von aussen auf Vorhandenes und Fehlendes — als Bewertung, inwieweit die Kostendaten als **Fundament für daten- und KI-basierte Verfahren** taugen. Kein Ersatz für interne Datenstrategie, aber strukturiertes Feedback aus Projektperspektive.
- **Dokumentierter Prototyp:** Umsetzung, mit der aus den gelieferten Daten Kostenaussagen (z. B. pro m²/m³) abgeleitet werden; **Dokumentation** von Datenfluss, Annahmen, Modellgrenzen und — soweit möglich — **Unsicherheit** der Schätzung statt nur eines Einzelwerts.
- Kurze Abstimmung mit Kostenkalkulatoren zu Datenqualität, Engpässen und tragfähigen Annahmen für das Modell (siehe auch Erwartungen an bfab).

---

## Erwartungen an bfab

1. **Daten**  
   - Grössenordnung: **150–200** Datensätze (Projekte oder vergleichbare Einheiten).  
   - Einheitliche Definitionen von Flächen, Volumen und relevanten Kostenpositionen.   
   - Indexierung und durchgängige Datenführung werden für die Modellqualität als vorteilhaft eingestuft; Umsetzung liegt bei bfab.

2. **Fachinput**  
   - **Ein bis zwei Gespräche** mit Personen aus dem Bereich Kostenkalkulation zur Klärung von Bottlenecks in Daten und Prozessen sowie zur Abstimmung von Vorschlägen für Datenstruktur und Modellgrenzen.

---

## Vertraulichkeit und Datenverwendung

- **NDA:** Vereinbarung möglich.  
- Rohdaten: keine Weitergabe an Dritte; keine Nutzung ausserhalb des beschriebenen Projekts.  
- Wissenschaftliche Dokumentation: nur anonymisierte oder aggregierte Angaben, soweit erforderlich; Abstimmung mit bfab im Einzelfall.

---

## Software und Lizenz

- Code und methodisches Vorgehen werden unter der **MIT-Lizenz** veröffentlicht.  
- Rohdaten von bfab sind nicht Teil der Veröffentlichung und bleiben Eigentum bzw. unter Kontrolle von bfab.  
- FHNW, bimdo und bfab können den veröffentlichten Code nach Massgabe der MIT-Lizenz weiterverwenden und anpassen.

---

## Institutioneller Rahmen

- **FHNW**, Studiengang Data Science & AI, Modul Wahrscheinlichkeitsrechnen.  
- **bimdo GmbH** als Co-Partner für Praxisbezug und Abstimmung zur Umsetzung.

---

*Abstimmungsgrundlage für bfab.ch. Kann bei Bedarf als PDF exportiert werden.*
