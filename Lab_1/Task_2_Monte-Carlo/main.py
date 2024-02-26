import cv2 as cv                                          # Библиотека для работы с изображениями
import random                                             
import math

IMAGE_DIR = "images/"
TARGET_PIXEL = (84, 28, 0)

def average(array: list) -> float:
    return sum(array)/len(array)


def calculate_area(IMG_PATH: str, field_area: float, AREA_PIXEL_RGB: tuple, n: int) -> tuple:
    input_img = cv.imread(IMG_PATH, cv.IMREAD_COLOR)  
    height, width = input_img.shape[:2]

    work_img = input_img
    
    lakePixel = 0                                             # Переменная для подсчёта точек, попавших в озеро
    areaPixel = 0                                             # Переменная для подсчёта точек, попавших за пределы озера

    for i in range(0, n):
        pixel = (random.randint(0, height-1), random.randint(0, width-1)) # Выбираем случайный пиксель
        
        if tuple(work_img[pixel[0]][pixel[1]]) == AREA_PIXEL_RGB:
            lakePixel += 1
            work_img[pixel[0]][pixel[1]] = (0, 255, 0)
            
        elif tuple(work_img[pixel[0]][pixel[1]]) != (0, 0, 255) and tuple(work_img[pixel[0]][pixel[1]]) != (0, 255, 0):
            areaPixel += 1 
            work_img[pixel[0]][pixel[1]] = (0, 0, 255)
        
        else:
            continue
                       
    return (lakePixel/areaPixel) * field_area, work_img


def standard_deviation(data: list) -> float:
    n = len(data)
    mean_value = average(data)
    total = 0
    
    for x in data:
        total += (x - mean_value) ** 2
        
    variance = total / n
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation


n = int(input("Введите n: "))                             # Ввод данных
s = float(input("Введите площадь области в км: "))
repeat = int(input("Сколько бросков сделать: "))

data = []

for i in range(repeat):
    area, img = calculate_area(IMG_PATH=IMAGE_DIR+'simf_lake.jpg', field_area=s, AREA_PIXEL_RGB=TARGET_PIXEL, n=n)
    data.append(area)

#area, img = calculate_area(IMG_PATH=IMAGE_DIR+'simf_lake.jpg', field_area=s, AREA_PIXEL_RGB=TARGET_PIXEL, n=n)


cv.imshow('img', img)           #вывод изображения
print(f"Значение площади: {average(data)} km^2")
print(f"Значение погрешности: +-{standard_deviation(data)*1_000_000} m^2")
cv.waitKey(0)


