"""
1.2 Виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана користувачем).

Олійник Богдан Сергійович 122\Д
"""

import numpy as np
mac = np.zeros((3,3),dtype = np.int)#Створимо масив з нулів типу цілих чисел
for y in range(3):
    for x in range(3):
        mac[x,y]=int(input('A['+str(y)+','+str(x)+']='))# робимо так щоб мінялися містями x i y , і тоді матриця залишается такою ж а ітерація йде вертикально
print(mac)
