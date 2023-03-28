'''
Programm liest daten aus "daten.txt" und erstellt ein Diagramm mit matplotlib
daten sind corona infektionen in 4 ländern

Lucas Grundl
24.20.22
'''

import matplotlib.pyplot as plt

# Datei öffnen
file = open("time_series_covid19_confirmed_global.csv", "r")

# Daten in einzelne Liste speichern (splitten)
austria = []
germany = []
sweden = []
uk = []

for i in file:
    i = i.strip("\n")
    if "Austria" in i: # Wenn "Austria" in der Zeile ist
        austria = i.split(",") # Alle Werte in der Zeile in einzelnen Listeneinträge speichern
    elif "Germany" in i:
        germany = i.split(",")
    elif "Sweden" in i:
        sweden = i.split(",")
    elif "United Kingdom" in i:
        uk = i.split(",")

file.close() # Datei schließen da sie nicht mehr benötigt wird


# Ersten 4 Einträge entfernen
for i in range(0,4):
    austria.pop(0)
    germany.pop(0)
    sweden.pop(0)
    uk.pop(0)

# Werte in float umwandeln
austria = [float(i) for i in austria] # alle werte werden mit einem for loop in einen float umgewandelt
germany = [float(i) for i in germany]
sweden = [float(i) for i in sweden]
uk = [float(i) for i in uk]


# Plot
# Diagramm Infektionen Österreich
plt.title("Corona Infektionen Österreich", fontsize=20) # Titel
plt.plot(austria, label="Austria") # Daten
plt.show() # Diagramm anzeigen

# Diagramm Infektionen Deutschland
plt.title("Corona Infektionen Deutschland", fontsize=20)
plt.plot(germany, label="Germany")
plt.show()

# Diagramm Infektionen Schweden
plt.title("Corona Infektionen Schweden", fontsize=20)
plt.plot(sweden, label="Sweden")
plt.show()

# Diagramm Infektionen UK
plt.title("Corona Infektionen Vereinigtes Königreich", fontsize=20)
plt.plot(uk, label="United Kingdom")
plt.show()


# Infektionen Österreichs werden in einer Datei gespeichert
file = open("austria.txt", "w") # Datei öffnen/erstellen

for i in austria: # Alle Werte in der Liste durchgehen
    file.write(str(i) + "\n") # Wert in Datei schreiben mit \n für neue Zeile

file.close() # Datei schließen
print("Gesammtinfektionen Österreich:  {:.2f} Mio.".format(austria[-1]/1000000)) # Gesammtinfektionen Österreichs ausgeben