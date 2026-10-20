# Ziele der Mini-Challenge

Wir schätzen die Treibhausgasintensität eines Gebäudes, `GHG_sum_em_m2a`, aus ein paar Angaben, die man früh in der Planung kennt. Die Daten kommen aus dem CarbEnMats-GBDB, beschrieben im [Projekt-Pitch](projekt_pitch.md).

Wir sind zu dritt und haben Wahrscheinlichkeitsrechnung noch nicht gehabt. Nebenher läuft eine Prüfung, die den ganzen Methodenkasten abdeckt. Die Challenge selbst soll deshalb klein bleiben: ein Modell, eine verständliche Wahrscheinlichkeitsaussage, ein kurzer Bericht.

Im Repo steht dafür bisher der Pitch, die Datennotiz und eine Python-Umgebung mit NumPy, pandas, Matplotlib, SciPy und Jupyter. Die GBDB-Dateien legen wir lokal nach `data/raw`, sie gehören nicht ins Git. Gerechnet ist noch nichts. Das Paket `src/cost_overruns` liegt von einer früheren Aufgabe herum, das lassen wir liegen. scikit-learn brauchen wir nicht.

Der Pitch zählt mehrere Verfahren auf. Für die Abgabe setzen wir auf eines. Den Rest lernen wir für die Prüfung und schreiben im Modellentscheid kurz auf, warum er hier nicht zum Zug kommt.

## Hauptziel

Am Ende können wir aus den Rohdaten für ein Beispielgebäude eine Intensität schätzen und sagen, wie wahrscheinlich ein von uns festgelegter Grenzwert in kg CO₂e/m²a überschritten wird.

Dafür gilt ein einziges Regressionsmodell, ausgewählt wie unten beschrieben. Wir vergleichen es in der 5-fachen Cross-Validation mit einer Schätzung, die nur den Mittelwert aus dem jeweiligen Trainingsfold nimmt. Den RMSE rechnen wir immer in kg CO₂e/m²a, auch wenn das Modell auf dem Logarithmus geschätzt wurde. Liegt unser RMSE darunter, schreiben wir das so hin. Liegt er darüber, kürzen wir die Feature-Liste einmal und berichten danach das Ergebnis, das wir haben. Die Challenge scheitert nicht an diesem Vergleich.

Die Überschreitungswahrscheinlichkeit kommt aus 10'000 Ziehungen. Dieselben Ziehungen liefern das 90-%-Intervall, als 5-%- und 95-%-Quantil. Im Bericht stehen ausserdem Datenfilter, der Modellentscheid, RMSE, MAE und R² und wie oft der wahre Wert auf dem Testdatensatz in diesem Intervall liegt. Wenn die Abdeckung nicht bei 90 % liegt, schreiben wir das hin. Bei so unterschiedlichen Fallstudien ist das ein Befund, kein Grund, das Modell wegzuwerfen.

Zeitlich rechnen wir mit etwa vier Wochen neben der Prüfung. Eine feste Frist steht im Pitch nicht. Wenn der Kurs eine setzt, schieben wir die Schritte von dort zurück.

## Was wir der Reihe nach abliefern

**Woche 1. Daten.** Eine bereinigte Tabelle in `data/processed` mit `GHG_sum_em_m2a` und den Gebäudeangaben aus dem Pitch, soweit sie nach dem Aufräumen noch da sind. Dazu eine knappe Notiz: wie viele Gebäude am Anfang, wie viele am Ende, wo Werte fehlen, welcher Filter zu LCA-Scope oder Datenqualität galt. Zeilen ohne Zielwert fliegen raus. Extrem hohe oder negative Intensitäten schauen wir uns an und lassen sie nur mit einem Satz Begründung weg. Nutzungsarten mit weniger als fünf Gebäuden fassen wir als „sonstige“ zusammen. Wenn `bldg_use_subtype` dabei zu viele seltene Stufen hat, nehmen wir nur `bldg_use_type`.

**Woche 2. Hinschauen.** Ein Notebook mit der Verteilung der Zielgrösse, der Korrelation von Fläche, Volumen und Geschossen über Terrain und dem VIF dieser Grössen. Untergeschosse nehmen wir in denselben Blick, wenn die Spalte genug gefüllt ist. Daraus die Feature-Liste für die erste Regression. Kategorien werden zu 0/1-Spalten, eine Stufe je Merkmal bleibt die Referenz und zählt nicht als eigener Koeffizient.

Die Zielgrösse ist schon pro Quadratmeter gerechnet. Fläche sagt dann vor allem, ob grosse Gebäude eine andere Intensität haben als kleine. Volumen und Fläche hängen ausserdem mechanisch zusammen, weil das Volumen mit der Fläche wächst. Beide bleiben nur drin, wenn sie nach diesem Blick wirklich Verschiedenes beitragen.

In derselben Woche setzen wir uns einmal zusammen und klären die paar Begriffe, die wir für die Ziehungen brauchen: Verteilung, Mittelwert, Standardabweichung, Quantil, und worin eine Punktschätzung und ein Intervall auseinanderliegen. Eine Stunde reicht.

**Mitte Woche 3. Modell festnageln.** Eine Seite `reports/modellentscheid.md`: wie viele Gebäude, welche Features, welches Modell, welche Alternative wir verworfen haben, CV-RMSE gegen den Mittelwert, ein Satz zu den Residuen. Danach bleiben wir bei diesem Modell. Wer mag, darf den RMSE eines weiteren Verfahrens als einzelne Vergleichszahl dazuschreiben. Die Simulation hängt am festgelegten Modell.

**Woche 4. Zahl und Wahrscheinlichkeit.** Am festgelegten Modell: RMSE, MAE und R², einmal auf dem Hold-out und einmal in der 5-fachen Cross-Validation, immer neben dem Mittelwert und immer in kg CO₂e/m²a. Für das Beispielgebäude das 90-%-Intervall und die Überschreitungswahrscheinlichkeit aus denselben 10'000 Ziehungen. Auf dem Testdatensatz nachzählen, wie oft der wahre Wert im Intervall liegt, und das in einem Satz einordnen. Der Kurzbericht in `reports/` soll so sein, dass eine von uns die Zahlen mit `uv sync` aus `data/raw` noch einmal erzeugen kann.

## Wie wir das Modell wählen

Solange die Tabelle nicht steht, wissen wir das endgültige Modell nicht. Unsere Annahme bis dahin: gewöhnliche lineare Regression auf einer kurzen Feature-Liste. Die Wahrscheinlichkeit holen wir uns, indem wir zur Punktschätzung eine Zufallszahl aus der Normalverteilung addieren, mit Mittelwert 0 und der Standardabweichung der Residuen.

Das passt zu dem, was wir können und was der Pitch will. Wir bekommen Koeffizienten, die man als Struktur, Nutzung und Grösse lesen kann. Die Ziehungen gehen mit NumPy. Und wir können die Kette selbst erklären: Schätzung, Residuum, viele Ziehungen, Anteil über dem Grenzwert. Ridge, Lasso, Random Forest und Gradient Boosting lernen wir für die Prüfung. In der Challenge werden sie nur dann das Projektmodell, wenn die Schritte unten uns dazu zwingen.

Wir kürzen zuerst die Liste, schätzen dann, und entscheiden am Residuenbild.

Die Stichprobe: n ist die Zahl der Gebäude mit Zielwert und vollständigen Features. Faustregel: höchstens ein Koeffizient auf 15 Gebäude, Stufen der Kategorien mitgezählt, die Referenzstufe nicht. Sind es mehr Koeffizienten, lassen wir zuerst den Subtyp weg, danach das schwächere von Fläche und Volumen.

Dann Fläche, Volumen und Geschosse. Korrelation und VIF. Liegt eine Korrelation über 0.8 oder ein VIF über 10, fällt das doppelte Merkmal weg. Von Fläche und Volumen bleibt eines. Geschosse bleiben, solange ihr VIF danach unter 10 liegt. Das Modell ist weiterhin die lineare Regression, nur mit der kürzeren Liste.

Diese Regression rechnen wir mit 5-facher Cross-Validation und vergleichen sie mit dem Mittelwert des jeweiligen Trainingsfolds. Den RMSE holen wir auf die Skala kg CO₂e/m²a zurück, sobald wir logarithmisch schätzen. Die Residuen schauen wir uns als Histogramm an und im Streudiagramm gegen die angepassten Werte.

Liegt der CV-RMSE über dem des Mittelwerts, kürzen wir die Liste noch einmal, die seltensten Kategorien zuerst, und wiederholen den Vergleich ein einziges Mal. Danach berichten wir, was herauskommt.

Sind die Residuen stark rechtsschief oder ist der Zusammenhang sichtbar gekrümmt, schätzen wir dieselbe Regression mit `log(GHG_sum_em_m2a)`. Ziehungen und Grenzwert rechnen wir mit der Exponentialfunktion auf kg CO₂e/m²a zurück. Das verhindert auch negative Intensitäten, die bei einer Normalverteilung um einen kleinen Schätzwert auf der Originalskala leicht entstehen. Sehen die Residuen danach brauchbar aus, ohne starken Bogen und ohne extremen Trichter, ist das unser Modell.

Ridge nehmen wir nur, wenn wir zwei stark zusammenhängende Merkmale wirklich beide brauchen und sich ihre Vorzeichen von Fold zu Fold drehen. Lasso lassen wir in dem Fall weg. Wir wollen eine stabile Schätzung mit einer Residuenstreuung, und Lasso würde nur eine zweite Auswahlmethode danebenstellen. Die Ziehungen bleiben angepasster Wert plus normalverteiltes Residuum. Im Modellentscheid schreiben wir dazu, dass das Intervall die Streuung der Residuen am Ridge-Fit zeigt und die Unsicherheit der Koeffizienten nicht enthält.

Wenn die Residuen auch dann unruhig bleiben, hören wir auf und beschreiben das Bild im Bericht.

Random Forest und Gradient Boosting erklären wir in der Prüfung. Hier darf ihr CV-RMSE als eine Zahl im Modellentscheid stehen, auf demselben Split. Intervall und Überschreitungswahrscheinlichkeit bauen wir daran nicht noch einmal. Dafür bräuchten wir ein eigenes Verfahren, und das wäre eine andere Arbeit.

Auf der Seite zum Modellentscheid stehen: n und die Feature-Liste, bis zu welchem Schritt wir gegangen sind, der Name des Modells, die beiden CV-RMSE auf der Originalskala, optional die eine Vergleichszahl, und ein Satz zu den Residuen. Der Satz sagt, ob wir auf der Originalskala oder logarithmisch mit Rücktransformation simulieren.

Für die Prüfung merken wir uns den Unterschied, den unsere Rechnung bewusst klein hält. Wir ziehen nur die Residuenstreuung. Ein Prognoseintervall aus dem Lehrbuch ist breiter, weil dort noch die Unsicherheit der Koeffizienten dazukommt. Ein Konfidenzintervall ist noch einmal etwas anderes: es meint den mittleren Schätzwert oder einen einzelnen Koeffizienten, nicht ein neues Gebäude. Die Überschreitungswahrscheinlichkeit in unserer Abgabe ist der Anteil der 10'000 Ziehungen über dem Grenzwert.

## Wer was macht

Eine Person räumt die Daten auf und macht die Beschreibung, bis Feature-Liste und n stehen. Eine Person geht die Modellwahl durch und schreibt `reports/modellentscheid.md`. Eine Person macht die Simulation und den Bericht. Die Begriffsstunde in Woche 2 machen wir zu dritt, bevor die Ziehungen losgehen.
