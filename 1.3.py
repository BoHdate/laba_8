"""
виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;
Олійник Богдан Сергійович 122\Д
"""

import random
import numpy as np
m1 = np.zeros((3,3),dtype=np.int)  #робимо масив з нулів типу цілих чисел
for x in range(3):
    for y in range(3):
        m1[x,y] = random.randint (-10,10)
m2 = np.zeros((3,3),dtype = np.int)
for z in range(3):
    for d in range(3):
        m2[z,d]=random.randint(-10,10)

mac = np.zeros((3,3),dtype=np.int)  #наперед створюємо масив з нулів для подільшої роботи з ним
print('Матриця M1:   \n', m1)  #виводимо наші матриці
print('Матриця M2:  \n', m2)
for a in range(3):
    for b in range(3):
        mac[a,b]=m1[a,b] * m2[a,b]  #потім перемножуємо наші матриці по елементно
print('Матриця mac:  \n', mac)  # виводимо нову матрицю
