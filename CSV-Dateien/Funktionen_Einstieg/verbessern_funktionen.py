'''
Einführung in Prozeduren und Funktionen
Autor: Alexander Jäger
Verbessert von: Lucas Grundl
Datum: 20.10.2021
'''

# Ueberprueft ob die zahl groesser gleich 0 ist
def check_input(input):
    while input <= 0:
        if input <= 0:
            print("Eingabe muss größer als 0 sein")
    return input


# Eingabe der 1. Zahl & ueberpruefung durch check_input()
z1 = check_input(int(input("Zahl: ")))

# Eingabe der 2. Zahl & ueberpruefung durch check_input()
z2 = check_input(int(input("Zahl: ")))

# Berechnung des größten gemeinsamen Teilers
while z2 != 0:
    if z1 > z2:
        z1 = z1 - z2
    else:
        z2 = z2 - z1

# Ausgabe des größten gemeinsamen Teilers
print('Der größte gemeinsame Teiler ist ' + str(z1))