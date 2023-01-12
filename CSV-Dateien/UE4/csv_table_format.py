'''
CSV Datein in eine Tabelle umwandeln
Autor: Lucas Grundl
Datum: 10.01.23
'''

# Importe
from tkinter import filedialog as fd  # fd.askopenfile() lässt den user eine datei auswählen
import csv  # csv.reader() liest die datei aus (besser als normales open(), da automatisch
            # getrennt wird)

# with open() schießt datei automatisch
with open(fd.askopenfilename()) as file:
    csv_f = csv.reader(file)

    # Zeilen auslesen
    for row in csv_f:

        # anhand der einträge ----- strich erstellen
        for i in row:
            print(16 * "-", end="")
        print("")  # nächste Zeile

        # Einträge formatieren Zahlen rechtsbündig und Text linksbündig
        for i in row:
            i = i.strip(" ")

            try:
                i = int(i)  # versucht i in int umzuwandeln
                print(f"{i:>15.15}", end="|")  # wenn dies möglich dann rechtsbündig anzeigen
            except ValueError:  # wenn nicht
                try:
                    i = float(i)  # versucht i in float umzuwandeln
                    print(f"{i:>15.15}", end="|")  # wenn dies möglich dann rechtsbündig anzeigen

                except ValueError:  # wenn nicht
                    print(f"{i:<15.15}", end="|")  # dann linksbündig anzeigen
        print("") # nächste Zeile
