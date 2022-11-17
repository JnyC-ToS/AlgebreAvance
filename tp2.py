import numpy as np
import matplotlib.pyplot as plt

# Entrées
# a = 0  # Borne inférieure
# b = 2 * np.pi  # Borne supérieure
# n = 10  # Nombre de points
# f = np.sin  # Fonction
a = -5  # Borne inférieure
b = 5  # Borne supérieure
n = 27  # Nombre de points
f = np.vectorize(lambda x: 1 / (1 + 10 * (x ** 2)))  # Fonction
aff = 500  # Nombre de points à l'affichage

# Points (X, Y) de la fonction
X = np.linspace(a, b, n)
Y = f(X)


# Base de Lagrange
def Lk(k, x):
	p = 1
	for i in range(0, n):
		if i != k:
			p *= (x - X[i]) / (X[k] - X[i])
	return p


# Polynôme
def Lagrange(x):
	s = 0
	for k in range(0, n):
		s += Y[k] * Lk(k, x)
	return s


# Points du polynôme
P = [Lagrange(x) for x in X]

# Valeurs pour l'affichage
Xaff = np.linspace(a, b, aff)
Yaff = f(Xaff)
Paff = [Lagrange(xaff) for xaff in Xaff]

# Affichage
plt.xlim(a, b)
# plt.ylim(-1, 1)
plt.ylim(-2, 2)
plt.axvline(0, color="k", linestyle="--", linewidth=1)
plt.axhline(0, color="k", linestyle="--", linewidth=1)
plt.plot(Xaff, Yaff, "b-", label="$f(x)$")
plt.plot(Xaff, Paff, "r-", label=f"$P(x)$")
# plt.legend()
plt.legend(loc="lower center")
plt.title("Interpolation d'une fonction à l'aide d'un polynôme")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
