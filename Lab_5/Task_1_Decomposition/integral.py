import math
INTEGRAL_EPS = math.pow(10, -4)

def integral(f, a: float, b: float, eps=INTEGRAL_EPS) -> float:
    
    def sympson_calc(f, a, b, n) -> float:
        h = (b - a) / n
        sum = f(a) + f(b)
        k = 0
        for i in range(1, n):
            k = 2 + 2 * (i % 2)
            sum += k * f(a + i * h)
        sum *= h / 3
        return sum

    n = 4
    d, Ih, Ih2 = 1, 1, 1

    while abs(d) >= eps:
        Ih = sympson_calc(f, a, b, n)
        n *= 2
        Ih2 = sympson_calc(f, a, b, n)
        d = (Ih - Ih2) / 15

    return Ih2 + d