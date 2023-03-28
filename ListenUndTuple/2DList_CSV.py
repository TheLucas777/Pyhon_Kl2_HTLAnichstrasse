'''
CSV-Dateien erstellen mit einer 2D-Liste
Author: Lucas Drundl
Date: 28-03-2023
'''

import csv
import random

def liste_erstellen(zeilen,spalten,titel):
    liste = [] # hardcode Spalten

    #erstellt titel
    list2 = []
    for i in range(spalten):
        list2.append(f"{titel} {i+1}")
    liste.append(list2)

    #erstellt zeilen
    for i in range(1,zeilen+1):
        liste.append([])

        #zufallszahlen erstellen
        for j in range(5):
            randomnum = int(random.randint(1,100))
            liste[i].append(randomnum)

    return liste

def csv_schreiben(liste,filename):
    with open(f"{filename}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";") #generiert eine csv datei mit semikolon als trennzeichen
        writer.writerows(liste) #schreibt die liste in die csv datei

#User Input
zeilen = int(input("Wie viele Zeilen? "))
spalten = int(input("Wie viele Spalten? "))
titel = input("Titel der Spalten? ")
filename = input("Dateiname? ")

liste = liste_erstellen(zeilen,spalten,titel)

csv_schreiben(liste,filename)