"""
1.Напишіть програми, що виконують такі операції з масивами (використовувати вбудовані методи по роботі з масивами заборонено):
виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотному порядку;
Олійник Богдан Сергійович 122/Д
"""

import numpy as np   #Імпортуєм бібліотеку numpy

i=int(input('Введіть кількість стрічок:'))       #створимо зміну в яку будемо вводити кількість стрічок

j=int(input("Введіть кількість стовпчиків:"))        #створимо зміну в яку будемо вводити кількість стовпчиків

mac = np.zeros((i,j),dtype = np.int)     #Створимо масив з нулів типу цілих чисел

for x in range(i-1,-1,-1):        #робимо так щоб ми проходились по кожному елементу стрічки починаючи з останього в зворотнбому порятку з степом i-1, -1 
    
    for y in range(j-1,-1,-1):      #робимо так щоб ми проходились по кожному елементу стовпчика починаючи з останього в зворотнбому порятку з степом j-1, -1 
        
        mac [x,y]=int(input('A[' + str(y+1) + ',' + str(x+1) + ']='))      #ми робимо так щоб програма проходила по кожній ітерації значень які ми вводимо і так щоб елементи вказувались в зворотньому порятку ми міняємо x та y  
    
print(mac)     #Виводимо нашу матрицю
