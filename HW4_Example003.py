# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии 
# тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.

# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:

# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4


from os import system
from random import randint
system ('cls')



data_list =[]
data_new_list =[]

data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\file.txt', 'r', encoding='utf-8')
for da in data:
    data_list.append(da)
data.close()



for data_new in data_list:
    if data_new.find(str(5)) > -1:  
        data_new_list.append(data_new.upper() )
    else:
        data_new_list.append(data_new)

data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\file.txt', 'w', encoding='utf-8')
for da in data_new_list:
      data.write(da)
data.close()


print (data_list)
print (data_new_list)
