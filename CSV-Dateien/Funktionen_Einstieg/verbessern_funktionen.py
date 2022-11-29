'''
Einführung in Prozeduren und Funktionen
Autor: Alexander Jäger
Verbessert von: Lucas Grundl
Datum: 20.10.2021
'''

# Ueberprueft ob die zahl groesser gleich 0 ist
def check_input():
    inp = 0
    while inp <= 0:
        inp = int(input("Zahl: "))
        if inp <= 0:
            print("Die Zahl muss größer als 0 sein!")
        else:
            return inp


# Eingabe der 1. Zahl & ueberpruefung durch check_input()
z1 = check_input()

# Eingabe der 2. Zahl & ueberpruefung durch check_input()
z2 = check_input()

# Berechnung des größten gemeinsamen Teilers
while z2 != 0:
    if z1 > z2:
        z1 = z1 - z2
    else:
        z2 = z2 - z1

# Ausgabe des größten gemeinsamen Teilers
print('Der größte gemeinsame Teiler ist ' + str(z1))