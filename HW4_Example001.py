# Задача 1.
# 1 - Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from os import system
system ('cls')
import Base



number = Base.check_number_more (2, 'Введите число больше 2-х: ')

my_list=[]
divider = 2
while number/divider>=1:
    if number%divider==0:
        my_list.append(divider)
    divider = Base.prime_number(divider)


print (f'N={number} -> {my_list}')

#print (prime_number (number))