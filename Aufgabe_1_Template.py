#Test Julius Telesch 
#Hier der Test ob pushen über SSH funktioniert
"""
Gerüst zur Lösung der Aufgabe 1 zur Übung Algorithmische Lösung technischer Probleme - Interpolation
"""
# Importieren der Plotting Bibliothek matplotlib
import matplotlib.pyplot as plt
# Importieren der Funktion interp1d aus der Bibliothek scipy.interpolate
from scipy.interpolate import interp1d
# auf die Funktion kann im Folgenden über interp1d(x, y, kind='<<Methode wählen>>') zugegriffen werden
# als Ergebniss wird eine Funktion zurückgegeben wlche anschließend mit zu interpolierenden x-Werten 
# aufgerufen werden kann: 
    #>> interpfun = interp1d(Temperaturen, Dichten, kind='linear') 
    #>> rho_280 = interpfun(280)
# rho_280 ist in diesem Fall die Dichte bei T=280K
# importieren der Bibliothek numpy
import numpy as np
# mit numpy können leicht diskrete Wertebereiche definiert werden. Dies wird z. B. für das Darstellen der
# von interp1d zurückgegebenen Funktion verwendet. Mit der Funktion np.linspace(start, stop, num)
# können N (num) gleichverteilte Punkte zwischen start und stop definiert werden:
    #>> interpfun = interp1d(Temperaturen, Dichten, kind='linear') 
    #>> Ts = np.linspace(250, 310, 60)
    #>> rhos = interpfun(Ts)
# Ts ist in diesem Fall ein Array (kann vereinfacht als Liste betrachtet werden) von Temperaturen
# [250, 251, 252, ..., 310] und rhos die dazugehörigen Dichten

# Listen mit den gegebenen Temperaturen und Dichten
Temperaturen = [308.15, 298.15, 288.15, 278.15, 268.15, 258.15, 248.15]  # in K
Dichten = [1.1455, 1.1839, 1.225, 1.269, 1.3163, 1.3673, 1.4224]  # in kg/m3


# Darstellen der Daten in einem Diagramm
# Erstellen der Abbildung (Figure) und einer Achse
fig, ax = plt.subplots()
# Plotten der Datenpunkte (scatter plot) der beiden Sensoren
ax.scatter(Temperaturen, Dichten)
# Axenbeschriftung
ax.set_xlabel("Temperatur in °C")
ax.set_ylabel("Dichte in kg/m3")

# Anzeigen des erstellten Plots
# Wenn das Programm in einem Terminal über "python Script.py" ausgeführt wird
# sollt nach dem fig.show() Befehl noch ein input() Befehl gesetzt werden, um
# das Schließen des Programms zu verhindern.
# alternativ can Python durch den Zusatz -i im interaktiven Modus gestartet werden,
# wo duch die Pythonkonsole nach Ablauf des Programms weiterhin zur Verfügung steht 
fig.show()



def interpolate_linear(x1, x2, y1, y2, x):
    # (x1, y1) und (x2, y2) sind die gegebenen Stützstellen
    # Abfrage ob x zwischen x1 und x2
    
    # wenn ja: dann y(x) über lineare interpolation berechnen
    
    # wenn nein: Hinweis ausgeben dass x nicht zwischen x1 und x2 
    pass

def nearest_neighbours(xi, yi, x):
    # xi und yi sind Listen der bekannten Werte
    # Abfrage ob x zwischen dem kleinsten und größten xi liegt

    # wenn ja: suche das xi welches am nähesten zu x ist und finde den zugehörigen Funktionswert yi
    
    # wenn nein: Hinweis ausgeben dass x nicht zwischen x1 und x2 
    pass

def interpolate_linear_from_list(xi, yi, y):
    # xi und yi sind Listen der bekannten Werte
    # Abfrage ob x zwischen dem kleinsten und größten xi liegt
    
    # wenn ja: suche die beiden xi zwischen denen x liegt und finde die zugehörigen Funktionswerte yi
    # rufe die Funktion interpolate_linear mit den gefundenen Werten auf und gib das Ergebnis dieser zurück
    
    # wenn nein: Hinweis ausgeben dass x nicht zwischen x1 und x2 
    pass


# Teilaufgabe 1
# T = 260 K : interpolate_linear(Temperaturen[0], Temperaturen[-1], Dichten[0], Dichten[-1], 260)
# Hinweis: mit [-1] kann auf das letzte, mit [-2] auf das vorletzte, usw... Element einer Liste zugegriffen werden
# T = 280 K : interpolate_linear(Temperaturen[0], Temperaturen[-1], Dichten[0], Dichten[-1], 280)
# T = 300 K : interpolate_linear(Temperaturen[0], Temperaturen[-1], Dichten[0], Dichten[-1], 300)

# Teilaufgabe 2
# Wie 1, nur mit Funktion "nearest_neighbour" und der Übergabe von Listen
# T = 260 K : nearest_neighbour(Temperaturen, Dichten, 260)
# usw...

# Teilaufgabe 3
# Wie 2, nur mit Funktion "interpolate_linear_from_list"
# T = 260 K : interpolate_linear_fom_list(Temperaturen, Dichten, 260)
# usw...
