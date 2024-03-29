import math

# Функция для расчета кубического сплайна
def cubic_spline(x_values, y_values):
    n = len(x_values) - 1
    h = [x_values[i + 1] - x_values[i] for i in range(n)]
    
    alpha = [0] + [3 * ((y_values[i + 1] - y_values[i]) / h[i] - (y_values[i] - y_values[i - 1]) / h[i - 1]) for i in range(1, n)]
    l, mu, z = [1], [0], [0]
    
    for i in range(1, n):
        l.append(2 * (x_values[i + 1] - x_values[i - 1]) - h[i - 1] * mu[i - 1])
        mu.append(h[i] / l[i])
        z.append((alpha[i] - h[i - 1] * z[i - 1]) / l[i])
    
    l.append(1)
    z.append(0)
    c = [0] * (n + 1)
    b = [0] * n
    d = [0] * n
    
    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y_values[j + 1] - y_values[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])
    
    return b, c, d

# Функция для вычисления значения кубического сплайна в точке
def evaluate_cubic_spline(x, x_values, y_values, b, c, d):
    i = 0
    while x > x_values[i + 1]:
        i += 1
    
    h = x - x_values[i]
    interpolated_value = y_values[i] + b[i] * h + c[i] * h ** 2 + d[i] * h ** 3

    return interpolated_value

# Заданные параметры
x_values = [1.00, 1.04, 1.08, 1.12, 1.16, 1.20]
y_values = [math.cos(x) for x in x_values]

# Вычисление кубического сплайна
b, c, d = cubic_spline(x_values, y_values)

# Значения сплайна в заданных точках
points_to_evaluate = [1.1, 1.09, 1.13, 1.15, 1.18]
for point in points_to_evaluate:
    spline_value = evaluate_cubic_spline(point, x_values, y_values, b, c, d)
    print(f"Значение кубического сплайна в точке {point}: {spline_value:.4f}")