from scipy.integrate import quad
import numpy as np


def f(x):
    return x ** 2

a = 0
b = 2

num_points = 10000
x_random = np.random.uniform(a, b, num_points)
y_random = np.random.uniform(0, f(b), num_points)

under_curve = np.sum(y_random < f(x_random))

area = (b - a) * (f(b)) * (under_curve / num_points)

print(f"Estimated area under the curve (Monte Carlo): {area}")


# test


def f(x):
    return x ** 2

integral, error = quad(f, a, b)

print(f"Test result (quad): {integral}")
