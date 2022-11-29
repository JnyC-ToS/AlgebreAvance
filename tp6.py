import matplotlib.pyplot as plt
import numpy as np

X = [7, 0, -8, -8, 0, 7]
Y = [0, 4, -3, 3, -4, 0]
T = [0, 1, 2, 3, 4, 5]
n = len(X)
Naff = 1000


def phi1(x):
	return (x - 1) ** 2 * (1 + 2 * x) if 0 < x <= 1 else 0


def phi2(x):
	return x ** 2 * (3 - 2 * x) if 0 < x <= 1 else 0


def phi3(x):
	return x * (x - 1) ** 2 if 0 < x <= 1 else 0


def phi4(x):
	return (x - 1) * x ** 2 if 0 < x <= 1 else 0


def _funcHermite(X, Y, V, x):
	res = 0
	for i in range(len(X) - 1):
		d = X[i + 1] - X[i]
		t = (x - X[i]) / d
		res += Y[i] * phi1(t) + Y[i + 1] * phi2(t) + d * (V[i] * phi3(t) + V[i + 1] * phi4(t))
	return res


funcHermite = np.vectorize(_funcHermite, excluded=["X", "Y", "V", 0, 1, 2])


def matrice(n):
	m = np.zeros((n, n))
	m[0, 0] = m[n - 1, n - 1] = 2
	for i in range(1, n - 1):
		m[i, i] = 4
	for i in range(0, n - 1):
		m[i, i + 1] = m[i + 1, i] = 1
	return m


def vectZ(x):
	n = len(x)
	return 3 * np.array([x[min(i + 1, n - 1)] - x[max(0, i - 1)] for i in range(n)])


M = matrice(n)
Vx = np.linalg.solve(M, vectZ(X))
Vy = np.linalg.solve(M, vectZ(Y))
Taff = np.linspace(T[0], T[n - 1], Naff)
Xaff = funcHermite(T, X, Vx, Taff)
Yaff = funcHermite(T, Y, Vy, Taff)

plt.plot(Xaff, Yaff, "b")
# plt.plot(X, Y, "kx")  # Visualize spline points
plt.plot(4, 2, "bx")  # 👁
plt.title("Spline cubique représentant un poisson")
plt.axis("equal")
plt.show()


# Bonus: Heart drawing

X = [0, 1, 2,  0, -2, -1, 0]
Y = [0, 1, 0, -2,  0,  1, 0]
T = [0, 1, 2,  3,  4,  5, 6]
n = len(X)
Naff = 1000

M = matrice(n)
Vx = np.linalg.solve(M, vectZ(X))
Vy = np.linalg.solve(M, vectZ(Y))
Taff = np.linspace(T[0], T[n - 1], Naff)
Xaff = funcHermite(T, X, Vx, Taff)
Yaff = funcHermite(T, Y, Vy, Taff)

plt.plot(Xaff, Yaff, "r")
plt.plot(X, Y, "kx")
plt.title("Spline cubique représentant un cœur")
plt.axis("equal")
plt.show()
