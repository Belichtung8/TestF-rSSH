"""
Gerüst zur Lösung der Aufgabe 3 zur Übung Algorithmische Lösung technischer Probleme - Interpolation
"""
# Importieren der Plotting Bibliothek matplotlib
import matplotlib.pyplot as plt
# Importieren von PIL zum einlesen des Bildes
from PIL import Image
# Importieren der Funktion interp2d aus der Bibliothek scipy.interpolate
from scipy.interpolate import interp2d
# Importieren von numpy
import numpy as np


# Definieren des Pfades zum Bild
IMG_PATH = r"Daten_Aufgabe_3/Rohbild_64x64.jpg"


# Funktion um das Bild zu laden und die Pixelwerte in einer Liste zurückzugeben
def load_image_to_list(image_path):
    im = Image.open(image_path)    
    width, height = im.size
    return list(im.getdata())


# Funktion zum darstellen eines quadratischen Bildes
def show_img(pixelList):
    plt.figure()
    # Breite des Bildes berechnen
    width = int(len(pixelList)**0.5)
    # Datentyp der Pixelliste zu unsigned Integer 8Bit (0-255) ändern
    imgArr = np.array(pixelList).astype(np.uint8)
    # Reshape 1D-Array zu 2-Array
    imgArr = imgArr.reshape((width, width))
    # 2D Array darstellen ohne Pixel-Interpolation und mit Color-Map jet
    plt.imshow(imgArr, vmax=255, vmin=0, cmap='jet', interpolation='none', aspect='equal')


    
    
pixel_list = load_image_to_list(IMG_PATH)
show_img(pixel_list)


def interpolate_bilinear(pixel_list):
    # berechnen Sie die Kantenlänge des Bildes (m x m Pixel)
    # nutzen sie eine for - Schleifen um über die Pixelliste zu itterieren
    # nutzen sie ihr wissen über Höhe und Breite des Bildes
    pass




def main():
    pass



if __name__ == "__main__":
    main()