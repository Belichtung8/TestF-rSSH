"""
Gerüst zur Lösung der Aufgabe 2 zur Übung Algorithmische Lösung technischer Probleme - Interpolation
"""
# Importieren der Plotting Bibliothek matplotlib
import matplotlib.pyplot as plt


# Relative Pfade zu den Daten der beiden Sensoren
# relativ bedeutet dass die Dateiaddressen bezogen auf das Arbeitsverzeichnis interpretiert werden
# dabei ist es wichtig das Skript im korrekten Verzeichnis, in diesem Fall dem "Case" Ordner, 
# auszuführen
FILENAME_SENSOR1 = "Daten_Aufgabe_2/sensor_1.csv"
FILENAME_SENSOR2 = "Daten_Aufgabe_2/sensor_2.csv"

# Funktion zum einlesen der Daten
def load_textfile(filepath: str, skip_n_lines: int = 1, delimiter: str =','):
    # öffnen der Datei mit der Addresse filepath
    # "open" übernimmt zwei Parameter: Dateiaddresse und Modus ("r" - read only, 
    # "w" - create new file for writing (Löscht bereits vorhandene Datein mit gleichem Namen),
    # "a" - append to the end of a file)
    # "open" gibt ein File Handler (fh) zurück, welcher ähnlich zu einem Pointer in C ist
    with open(filepath, "r") as fh:
        # "readlines" List alle Zeilen der Datei ein und speichert diese in einer Liste
        lines = fh.readlines()
        # leere Liste zum speichern der Zeitwerte
        # die jeweiligen Werte können mit der .append() Methode an die Liste angefügt werden
        timestamps = []
        # leere Liste zum speichern der Temperaturwerte
        temperatures = []
        # Itteration über alle Zeilen der Datei
        # enumerate() ordnet jeder Zeile eine Nummer zu:
        # (0, erste_Zeile_der_Datei) --> i, line
        # (1, zweite_Zeile_der_Datei) --> i, line ...usw.
        for i, line in enumerate(lines):
            # überspringen der ersten n Zeilen um Kopfzeilen zu überspringen
            if i < skip_n_lines:
                # "continue" springt wieder zum anfang der Schleife und es wird
                # mit der nächsten Itteration fortgefahren ohne die unterhalb stehenden
                # Befehle ausgeführt zu haben
                continue
            # die Daten sind mittels "," getrennt, das Trennsymbol kann als
            # Parameter "delimiter" an die Funktion übergeben werden und
            # ist standardmäßig als "," definiert
            # mit Hilfe der split() Methode können Zeichenketten (strings) an
            # bestimmten Symbolen getrennt werden
            # split gibt eine Liste der getrennten Elemente zurück, in diesem Fall 2
            # das erste Element wird in der Variable "time" gespeichert und das Zweite
            # in der Variable "temp"
            time, temp = line.split(delimiter)
            # die beiden Variablen werden nun an die vorbereiteten Listen übergeben
            # bei den in "time" und "temp" gespeicherten Werten handelt es sich allerdings noch um
            # Zeichenketten (strings)
            # um später numerische Operationen vornehmen zu können werden die Zeichenketten mit Hilfe
            # der Funktion "float()" in Fließkommazahlen umgewandelt
            timestamps.append(float(time))
            temperatures.append(float(temp))
        # nachdem über alle Zeilen der Datei itteriert wurde werden die beiden Listen
        # von der Funktion als Rückgabewerte ausgegeben
        return timestamps, temperatures
            
def interpolate_linear(x, xp, yp):
    """ x - Liste der zu interpolierenden Punkte 
        xp - Liste der x-Koordinaten der bekannten Stützstellen 
        yp - Liste der y-Koordinaten der bekannten Stützstellen 
        
        Rückgabewert: Liste mit interpolierten y-Werten an den Stellen x"""
    pass
   

# Laden der Daten aus den Datein mit den oben definierten Addressen über die 
# oben definierte Funktion "load_textfile"
Zeit1, Temperatur1 = load_textfile(FILENAME_SENSOR1)
Zeit2, Temperatur2 = load_textfile(FILENAME_SENSOR2)

# Darstellen der geladenen Daten in einem Diagramm
# Erstellen der Abbildung (Figure) und einer Achse
fig, ax = plt.subplots()
# Plotten der Datenpunkte (scatter plot) der beiden Sensoren
ax.scatter(Zeit1, Temperatur1, label='Sensor 1')
ax.scatter(Zeit2, Temperatur2, label='Sensor 2')
#Legende erstellen
ax.legend()
# Axenbeschriftung
ax.set_ylabel("Temperatur in °C")
ax.set_xlabel("Zeit in s")

# Anzeigen des erstellten Plots
# Wenn das Programm in einem Terminal über "python Script.py" ausgeführt wird
# sollt nach dem fig.show() Befehl noch ein input() Befehl gesetzt werden, um
# das Schließen des Programms zu verhindern.
# alternativ can Python durch den Zusatz -i im interaktiven Modus gestartet werden,
# wo duch die Pythonkonsole nach Ablauf des Programms weiterhin zur Verfügung steht 
fig.show()




