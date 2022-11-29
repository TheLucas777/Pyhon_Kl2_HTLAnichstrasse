'''
Datenanalyse der Landtagswahlen in Vomp Tirol
Autor: Lucas Grundl
Datum: 24.10.2021
'''

import matplotlib.pyplot as plt

# Liest die alle daten des ortes Vomp aus
def get_vomp(file):
    file = open(file, "r") # Datei öffnen
    data = [] # Liste erstellen

    # Daten in einzelne Liste speichern (splitten)
    for i in file:
        if "Vomp" in i:
            data = i.split(";")
    file.close()

    # Daten zurückgeben
    return data


# Liest die Wahlbeteiligung aus
def get_wahlbeteiligung(data):
    #entfertnt alle einträge bis zur wahlbeteiligung
    for i in range(10):
        data.pop(0)

    wahlbeteiligung = data[0].replace(",", ".") # Komma durch Punkt ersetzen
    # Wahlbeteiligung in float umwandeln und zurückgeben
    return float(wahlbeteiligung)


jahre = [1989, 1994, 1999, 2003, 2008, 2013, 2018] # Jahre in denen gewählt wurde
wahlbeteiligung = [] # Liste für die Wahlbeteiligung

for i in jahre:
    # fügt die wahlbeteiligung des jahres in die liste ein
    wahlbeteiligung.append(get_wahlbeteiligung(get_vomp("{}.csv".format(i))))



# Plot
plt.title("Wahlbeteiligung in Vomp Tirol", fontsize=20) # Titel
plt.ylim(0, 100) # Y-Achse von 0 bis 100
plt.plot(jahre, wahlbeteiligung, label="Wahlbeteiligung") # Daten
plt.show() # Diagramm anzeigen