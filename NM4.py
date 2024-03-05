import numpy as np

# Функция, которую нужно проинтегрировать
def f(x):
    return x**2

# Метод средних прямоугольников для вычисления интеграла
def middle_rectangle(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)  # Середины подинтервалов
    y = f(x)
    return h * np.sum(y)

# Оценка погрешности с использованием правила Рунге
def runge_rule(I, In, p):
    return abs(I - In) / (2**p - 1)



a = 0 # Нижний предел интегрирования
b = 4  # Верхний предел интегрирования
p = 2 # Показатель сходимости метода
h_min = 0.00001 # минимальный шаг
n = 2 # начальное кол-во шагов

In = middle_rectangle(f, a, b, n)
I2n = middle_rectangle(f, a, b, 2*n)
print(f"Вычисленное значение интеграла: {I2n}")
print(f"Оценка погрешности с использованием правила Рунге: {runge_rule(I2n, In, p)}")

while True:
    In = I2n
    n = 2 * n  # h/2
    I2n = middle_rectangle(f, a, b, 2 * n)

    if not runge_rule(I2n, In, p) / (-2):
        print("\n")
        print("Погрешность не уменьшилась\n")
        break

    h_cur = (b - a) / n

    if not h_cur > h_min:
        print("\n")
        print("Шаг интегрирования стал недопустимо малым\n")
    break

h_cur = (b - a) / n






