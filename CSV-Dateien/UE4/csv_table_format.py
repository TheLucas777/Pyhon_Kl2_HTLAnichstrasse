'''
CSV Datein in eine Tabelle umwandeln
Autor: Lucas Grundl
Datum: 10.01.23
'''

# Importe
from tkinter import filedialog as fd    # fd.askopenfile() lässt den user eine datei auswählen


with open(fd.askopenfilename()) as file:
    splitchar = input("Bitte gib an wie die CSV Datei getrennt ist: ")  # Trennzeichen
    #data = file.readlines() # Liest alle Zeilen der Datei
    for line in file:
        print(len(line)*"-")
        print(line.strip("\n").split(splitchar))


#daten verarbeiten und formatieren

#for i in range(len(data)):
#    print(len(data) * "-")
#    spalte = data[i].split(splitchar) # Splittet die Zeile an den Semikolons
#    for j in range(len(spalte)):
#        print(f"|{spalte[j]}", end="")
#    print("|",end="")
