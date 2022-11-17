import numpy as np
import matplotlib.pyplot as plt

# Entrées
a = 0  # Borne inférieure
b = 2 * np.pi  # Borne supérieure
n = 5  # Nombre de points
f = np.sin  # Fonction
aff = 500  # Nombre de points à l'affichage

# Points (X, Y) de la fonction
X = np.linspace(a, b, n)
Y = f(X)

# Matrice de Vandermonde
V = np.vander(X, increasing=True)
# Résolution du système
A = np.linalg.solve(V, Y)


# Polynôme (optimisé avec Horner)
def polynom(x):
	s = A[n - 1]
	for k in range(n - 2, -1, -1):
		s = s * x + A[k]
	return s


# Points du polynôme
P = [polynom(x) for x in X]

# Écart max
E = np.max(np.abs(Y - P))
X_e = X[np.argmax(np.abs(Y - P))]

# Valeurs pour l'affichage
Xaff = np.linspace(a, b, aff)
Yaff = f(Xaff)
Paff = [polynom(xaff) for xaff in Xaff]
Eaff = np.max(np.abs(Yaff - Paff))
index = np.argmax(np.abs(Yaff - Paff))
XEaff = Xaff[index]
YEaff = Yaff[index]
PEaff = Paff[index]

# Affichage
plt.xlim(0, 2 * np.pi)
plt.ylim(-1, 1)
plt.axhline(0, color="k", linestyle="--", linewidth=1)
plt.plot(Xaff, Yaff, "b-", label="$f(x)$")
plt.plot(Xaff, Paff, "r-", label=f"$P(x)$")
plt.plot((XEaff, XEaff), (YEaff, PEaff), "gx-")
plt.text(XEaff + 0.05, (YEaff + PEaff) / 2, f"$E_{{max}}={Eaff:.5f}$")
plt.legend()
plt.title("Approximation d'une fonction à l'aide d'un polynôme")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
