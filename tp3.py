import numpy as np
import matplotlib.pyplot as plt

# Entrées
a = 0  # Borne inférieure
b = 2 * np.pi  # Borne supérieure
n = 4  # Nombre de points
f = np.sin  # Fonction
aff = 500  # Nombre de points à l'affichage

# Points (X, Y) de la fonction
X = np.linspace(a, b, n)
Y = f(X)
coefs = Y.copy()

# Différences divisées
for i in range(0, n - 1):
	for j in range(i + 1, n):
		coefs[j] = (coefs[j] - coefs[i]) / (X[j] - X[i])


# Polynôme à l'aide de la base de Netwon
def Newton(x):
	s = coefs[0]
	N = 1
	for k in range(1, n):
		N *= x - X[k - 1]
		s += coefs[k] * N
	return s


# Ajouter un point
def AddPoint(x, y):
	global X, Y, coefs, n
	X = np.append(X, x)
	Y = np.append(Y, y)
	N = 1
	for k in range(0, n):
		N *= x - X[k]
	beta = (y - Newton(x)) / N
	coefs = np.append(coefs, beta)
	n += 1


# Points du polynôme
P = [Newton(x) for x in X]

# Valeurs pour l'affichage
Xaff = np.linspace(a, b, aff)
Yaff = f(Xaff)
P4aff = [Newton(xaff) for xaff in Xaff]

# Ajout des points A(1, sin(1)) puis B(5, sin(5))
AddPoint(1, np.sin(1))
P5aff = [Newton(xaff) for xaff in Xaff]
# AddPoint(5, np.sin(5))
# P6aff = [Newton(xaff) for xaff in Xaff]

# Affichage
plt.xlim(a, b)
plt.ylim(-1.2, 1.2)
plt.axvline(0, color="k", linestyle="--", linewidth=1)
plt.axhline(0, color="k", linestyle="--", linewidth=1)
plt.axhline(-1, color="k", linestyle=":", linewidth=0.5)
plt.axhline(1, color="k", linestyle=":", linewidth=0.5)
plt.plot(Xaff, Yaff, "r-", label="$f(x)$")
plt.plot(Xaff, P4aff, "b-", label=f"$P_4(x)$")
plt.plot(Xaff, P5aff, "g-", label=f"$P_5(x)$")
# plt.plot(Xaff, P6aff, "m-", label=f"$P_6(x)$")
plt.legend()
plt.title("Interpolation d'une fonction à l'aide d'un polynôme")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
