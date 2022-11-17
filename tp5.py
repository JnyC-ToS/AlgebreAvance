import matplotlib.pyplot as plt
import numpy as np

X = [-5, -2, 0, 3, 6]
Y = [-4, -1, 1, 1, -1]
V = [3, 0, 3, -2, 0]


def phi1(x):
	return (x - 1) ** 2 * (1 + 2 * x) if 0 <= x <= 1 else 0


def phi2(x):
	return x ** 2 * (3 - 2 * x) if 0 <= x <= 1 else 0


def phi3(x):
	return x * (x - 1) ** 2 if 0 <= x <= 1 else 0


def phi4(x):
	return (x - 1) * x ** 2 if 0 <= x <= 1 else 0


def _funcHermite(x):
	for i in range(len(X) - 1):
		if X[i] <= x <= X[i + 1]:
			d = X[i + 1] - X[i]
			t = (x - X[i]) / d
			return Y[i] * phi1(t) + Y[i + 1] * phi2(t) + d * (V[i] * phi3(t) + V[i + 1] * phi4(t))
	return 0


funcHermite = np.vectorize(_funcHermite)

Xaff = np.linspace(X[0], X[-1], 500)
Yaff = funcHermite(Xaff)

plt.xlim(X[0], X[-1])
plt.ylim(np.min(Yaff), np.max(Yaff))
plt.plot(Xaff, Yaff, "b-", label="$P(x)$")
plt.plot(X, Y, "rx", label="Points (X, Y)")
for i in range(len(X)):
	plt.plot((X[i] - 1, X[i] + 1), (Y[i] - V[i], Y[i] + V[i]), "k:")
plt.legend()
plt.title("Polynôme d'Hermite")
plt.show()
