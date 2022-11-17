import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Entrées
N = 500
T = np.linspace(0, 1, N)

# Points de contrôle de la courbe
P = np.array([
	[-0.5, 0],
	[2, 2.5],
	[-2, 2.5],
	[0.5, 0]
])


# Calcul de la loi binômiale
def binom(n, p):
	return factorial(n) / (factorial(p) * factorial(n - p))


# Polynôme de Bernstein
def bernstein(n, i, t):
	return binom(n, i) * (t ** i) * ((1 - t) ** (n - i))


# Courbe de Bézier à partir des points de contrôle
def bezier(P):
	n = len(P) - 1
	X = []
	Y = []
	for t in T:
		x, y = 0, 0
		for i in range(n + 1):
			x += bernstein(n, i, t) * P[i, 0]
			y += bernstein(n, i, t) * P[i, 1]
		X.append(x)
		Y.append(y)
	return X, Y


# Calcul et affichage des valeurs de notre courbe
Xaff, Yaff = bezier(P)
plt.plot(Xaff, Yaff, "b", label="Courbe de Bézier")
plt.plot(P[:, 0], P[:, 1], "r:x", label="Points de contrôle")
plt.legend()
plt.title("Courbe de Bézier de 4 points")
plt.show()
