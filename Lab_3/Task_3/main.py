import math

def f(x):
    # Функции новой системы уравнений
    f1 = math.cos(x[0] + 0.5) + x[1] - 0.8
    f2 = math.sin(x[1]) + 2*x[0] - 1.6
    return [f1, f2]

def jacobi_matrix(x):
    # Якобиан новой системы уравнений
    df1_dx1 = -math.sin(x[0] + 0.5)
    df1_dx2 = 1
    df2_dx1 = 2
    df2_dx2 = math.cos(x[1])

    return [[df1_dx1, df1_dx2], [df2_dx1, df2_dx2]]


def newton_raphson(x0, tol, max_iter=100):
    x = x0
    for _ in range(max_iter):
        # Вычисляем значение функции и якобиана в текущей точке
        fx = f(x)
        jacobi = jacobi_matrix(x)

        # Решаем линейную систему уравнений для нахождения приращения 
        delta_x = [0, 0]
        delta_x[0] = (jacobi[1][1]*fx[0] - jacobi[0][1]*fx[1]) / (jacobi[0][0]*jacobi[1][1] - jacobi[0][1]*jacobi[1][0])
        delta_x[1] = (jacobi[0][0]*fx[1] - jacobi[1][0]*fx[0]) / (jacobi[0][0]*jacobi[1][1] - jacobi[0][1]*jacobi[1][0])
        
        # Обновляем x
        x = [x[i] - delta_x[i] for i in range(2)]
        
        if max(abs(delta_x[0]), abs(delta_x[1])) < tol:
            break
            
    return x

x0 = [1.0, 1.0]
eps = 10**(-4)
result = newton_raphson(x0, eps)
print("Решение системы уравнений:", result)