def print_matrix(matrix: list) -> None:
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

def extend_matrix(matrix, b):
    i = 0
    for row in matrix:
        row.append(b[i])
        i += 1

def gauss_jordan(matrix):
    n = len(matrix)

    for i in range(n):
        pivot = matrix[i][i]  # Выбираем ведущий элемент

        for j in range(i, n + 1): 
            matrix[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = matrix[k][i]

                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    return [row[-1] for row in matrix]


n = int(input("Введите n: "))

print("Введите матрицу: ")
matrix = [[int(i) for i in input().split()] for j in range(n)]

print("Введите b: ")
b = [int(input()) for i in range(n)]

extend_matrix(matrix, b)

result = gauss_jordan(matrix)

for i in range(len(result)):
    print(f"x{i+1} = {result[i]}")

#print_matrix(gauss_jordan(matrix)) 