import matplotlib.pyplot as plt
import time
plt.style.use = ("seaborn-whitegrid")
GRAPH_STEP = 0.1

def createBasePolynom(x_values: list, i: int):
    def basePolynom(x: float) -> float:
        numerator = 1 
        denominator = 1

        for j in range(0, len(x_values)):
            if i == j:
                continue 
            
            numerator *= (x - x_values[j])
            denominator *= (x_values[i] - x_values[j])
            
        return numerator/denominator

    return basePolynom


def createLagrange(x_values, y_values):
    basepolynoms = []

    for i in range(len(x_values)):
        basepolynoms.append(createBasePolynom(x_values, i))

    def lagrange(x):
        result = 0
        for i in range(len(y_values)):
            result += y_values[i] * basepolynoms[i](x)

        return result

    return lagrange


def floatRange(start, stop, step):
    cur = start
    result = []
    
    while cur != stop:
        result.append(cur)
        cur += step

    return result


#x_cords = [float(i) for i in input("Введите x-координаты: ").split()]
#y_cords = [float(i) for i in input("Введите y-координаты: ").split()]

x_cords = [1, 2, 3, 4, 5]
y_cords = [7.2, 10, 4.9, 10, 3.2]

lagrangePolynom = createLagrange(x_cords, y_cords) 

for x in range(len(x_cords)):
    print(f"y{x} = {lagrangePolynom(x_cords[x])}")

#fig, ax = plt.subplots()


y = [lagrangePolynom(i) for i in x]

plt.grid()
plt.plot(x, y, marker = 'o', markersize=3)
plt.show()
