import numpy as np


def cubic_spline_interpolation(X, Y, N, XX, A, B):
    n = len(X) - 1
    if n < 1:
        print("Кубический сплайн не может быть построен.")
        return 1, None

    if any(np.diff(X) < 0):
        print("Нарушен порядок возрастания аргумента в входном векторе.")
        return 2, None

    if XX < X[0] or XX > X[n]:
        print("Входное значение точки XX не находится в интервале [X[0], X[n]].")
        return 3, None

    h = np.diff(X)
    alpha = np.zeros(n + 1)
    for i in range(1, n):
        alpha[i] = 3 / h[i] * (Y[i + 1] - Y[i]) - 3 / h[i - 1] * (Y[i] - Y[i - 1])

    l = np.zeros(n + 1)
    mu = np.zeros(n + 1)
    z = np.zeros(n + 1)
    l[0] = 1
    mu[0] = 0
    z[0] = 0

    for i in range(1, n):
        l[i] = 2 * (X[i + 1] - X[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = 1
    z[n] = 0
    c = np.zeros(n + 1)
    b = np.zeros(n)
    d = np.zeros(n)

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (Y[j + 1] - Y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    i = 0
    while XX > X[i + 1]:
        i += 1

    YY = Y[i] + b[i] * (XX - X[i]) + c[i] * (XX - X[i]) ** 2 + d[i] * (XX - X[i]) ** 3

    return 0, YY


# Меню использования
X = np.array([0,1,1,3,4])
Y = np.array([0, 1, 8, 27, 64])
N = 4
XX = 4.5
A = 3
B = 30

IER, YY = cubic_spline_interpolation(X, Y, N, XX, A, B)
if IER == 0:
    print("Интерполяционное значение функции в точке XX =", XX, ":", YY)
else:
    print("Ошибка при выполнении интерполяции =", IER)
print("X,Y =", X,Y)