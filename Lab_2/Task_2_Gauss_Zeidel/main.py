def gauss_zeidel(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(A)
    x = x0.copy()
    iter_count = 0
    while iter_count < max_iter:
        x_new = x.copy()
        for i in range(n):
            x_new[i] = (b[i] - sum(A[i][j] * x_new[j] for j in range(n) if j != i)) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new
        x = x_new
        iter_count += 1
    print("Метод Гаусса-Зейделя не сошелся за", max_iter, "итераций.")
    return x

n = int(input("Введите n: "))

print("Введите матрицу: ")
matrix = [[int(i) for i in input().split()] for j in range(n)]

print("Введите b: ")
b = [int(input()) for i in range(n)]
x0 = [0, 0, 0]

result = gauss_zeidel(matrix, b, x0)

for i in range(len(result)):
    print(f"x{i+1} = {result[i]}")