#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности. Не использовать множества.
#[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from os import system
system ('cls')
import Base

my_list = [1,1,1,1,2,2,2,3,3,3,4]

number_list =[]
number_list.append(my_list[0])


for i in my_list:
    if number_list.count(i)==0:
        number_list.append(i)

print (my_list, '->',number_list)