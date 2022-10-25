'''
Matplotlib - Aufgabe 1
Lucas
24.20.22
'''

import matplotlib.pyplot as plt

# Daten
file = open("daten.txt", "r")

# Daten in Liste speichern (splitten)
daten = []
for line in file:
    line = line.strip("\n")
    daten.append(line.split("\t"))

# Daten in einzelne Listen speichern
x = []
y = []
for i in range(len(daten)):
    x.append(float(daten[i][0]))
    y.append(float(daten[i][1]))

# Plot
plt.plot(x, y)
plt.show()
file.close()
