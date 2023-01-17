'''
Liest die Buchstaben aus einer Datei aus
Autor: Lucas Grundl
Datum: 17.01.2023
'''

from tkinter import filedialog as fd  # fd.askopenfile() lässt den user eine datei auswählen


with open(fd.askopenfilename()) as file: # mit open() schießt datei automatisch
    for line in file: # Zeilenweise auslesen
        erg = 0

        for char in line: # Zeichenweise auslesen
            if char.isalpha():  # wenn char ein buchstabe ist
                erg += 1  # dann erhöhe erg um 1

        print(f"Die Datei besteht aus {erg} Buchstaben") # ausgabe an den User