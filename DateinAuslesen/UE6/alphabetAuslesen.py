'''
Das Alphabet auslesen aus einer Datei
Datum: 2023-01-29
Autor: Lucas Grundl
'''

from tkinter import filedialog as fd  # fd.askopenfile() lässt den user eine datei auswählen


# dict erstellen mit alphabet als key und 0 als value
alphabet = {"A": 0,"B": 0,"C": 0,"D": 0,"E": 0,"F": 0,"G": 0,"H": 0,"I": 0, "J": 0,"K": 0,"L": 0,"M": 0,
            "N": 0,"O": 0,"P": 0,"Q": 0,"R": 0,"S": 0,"T": 0,"U": 0,"V": 0,"W": 0,"X": 0,"Y": 0,"Z": 0}

with open(fd.askopenfilename()) as file: # mit open() schießt datei automatisch
    for line in file: # Zeilenweise auslesen
        for char in line: # Zeichenweise auslesen
            if char.isalpha():  # wenn char ein buchstabe ist
                alphabet[char.upper()] += 1  # dann erhöhe jeweiligen Buchstaben um 1


# Ausgabe an den User
print("Die Datei besteht aus:")
for key, value in alphabet.items():  # für jeden key und value in alphabet
    print(f"{key}: {value}", end="       ")  # ausgabe an den User
    print(f"{round(value / sum(alphabet.values()) * 100, 2)}%")
    # round() rundet auf 2 nachkommastellen
    # sum() addiert alle werte in alphabet.values() zusammen
    # value / sum(alphabet.values()) * 100 berechnet den prozentwert
    print("------------------")
