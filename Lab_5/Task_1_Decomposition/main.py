import math
from integral import *
from floatRange import *
import matplotlib.pyplot as plt

FOIRIER_EPS = math.pow(10, -4)
N = 1
pi = math.pi

def func(x):
    return math.cos(2*x)

def fourier(func, N, x, T):
    a0 = 2 / T * integral(func, 0, T)
    f = a0 / 2
    for k in range(1, N + 1):
        a = 2 / T * integral(lambda x: func(x) * math.cos(k * x), 0, T)
        b = 2 / T * integral(lambda a: func(a) * math.sin(k * a), 0, T)
        f += a * math.cos(k * x) + b * math.sin(k * x)

    return f


if __name__ == '__main__':
    
    x_cords = floatRange(0, 7, 0.05)
    y_cords = [fourier(func, N, i, 2*pi) for i in x_cords]

    plt.grid()
    plt.plot(x_cords, y_cords, marker = 'o', markersize=2)
    plt.show()

