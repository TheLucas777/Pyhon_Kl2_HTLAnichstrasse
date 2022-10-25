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
plt.title("Aufgabe 1", fontsize=20, color="white")
plt.figure(facecolor='black')
ax = plt.axes()
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_facecolor("black")
plt.xlabel("x", fontsize=15)
plt.ylabel("y", fontsize=15)
plt.plot(x, y, color="white")
plt.show()
file.close()
