import math

def ln(x):
    return math.cos(x)

x_values = [round(1.00 + i * 0.04, 4) for i in range(6)]
y_values = [ln(x) for x in x_values]

# Кубический сплайн
def cubic_spline(x, x_values, y_values):
    n = len(x_values)

    for i in range(n - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            h = x_values[i + 1] - x_values[i]
            a = y_values[i]
            b = (y_values[i + 1] - y_values[i]) / h
            c = (3 * (y_values[i + 1] - y_values[i]) - 2 * b * h) / h**2
            d = (2 * (y_values[i] - y_values[i + 1]) + b * h) / h**3

            return a + b * (x - x_values[i]) + c * (x - x_values[i])**2 + d * (x - x_values[i])**3

# Точки, в которых нужно найти значения сплайна
points = [1.05, 1.09, 1.13, 1.15, 1.17]

# Находим значения сплайна в указанных точках
for point in points:
    spline_value = cubic_spline(point, x_values, y_values)
    print(f'Значение кубического сплайна в точке {point}: {spline_value}')