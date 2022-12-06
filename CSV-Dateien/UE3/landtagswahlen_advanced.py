'''
Datenanalyse der Landtagswahlen (mit UI)
Autor: Lucas Grundl
Datum: 24.10.2021
'''

import matplotlib.pyplot as plt
import csv

gemeinden = []
wahlen_2018 = open("2018.csv", "r") # Datei öffnen




# Liest die alle daten des ortes Vomp aus
def get_ort(file,ort):
    file = open(file, "r") # Datei öffnen
    data = [] # Liste erstellen

    # Daten in einzelne Liste speichern (splitten)
    for i in file:
        if ort in i:
            data = i.split(";")
    file.close()

    # Daten zurückgeben
    return data


# Liest die Wahlbeteiligung aus
def get_wahlbeteiligung(data):
    erg = data[10].replace(",", ".") # Komma durch Punkt ersetzen
    # Wahlbeteiligung in float umwandeln und zurückgeben
    return float(erg)


jahre = [1989, 1994, 1999, 2003, 2008, 2013, 2018] # Jahre in denen gewählt wurde
wahlbeteiligung = [] # Liste für die Wahlbeteiligung

# Lade alle gemeiden in eine liste
wh = csv.reader(wahlen_2018, delimiter=";")
i = 0
for line in wh:
    if i > 1:
        gemeinden.append(line[3])
    i += 1
wahlen_2018.close()

uiOrt = input("Ort: ")

for i in jahre:
    # fügt die wahlbeteiligung des jahres in die liste ein
    wahlbeteiligung.append(get_wahlbeteiligung(get_ort("{}.csv".format(i), uiOrt)))



# Plot
plt.title("Wahlbeteiligung in {} Tirol".format(uiOrt), fontsize=20) # Titel
plt.ylim(0, 100) # Y-Achse von 0 bis 100
plt.plot(jahre, wahlbeteiligung, label="Wahlbeteiligung") # Daten
plt.show() # Diagramm anzeigen