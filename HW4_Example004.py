# Задача №4
# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное 
# количество символов влево или вправо. При расшифровке происходит обратная операция. 
# 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - 
# сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# 
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

from os import system
system ('cls')
import Base

def encoder_caesar(text:str,key:int):
    '''
    Кодирование по "Шифру Цезаря", смещение каждой буквы происходит в лево или право по алфавиту
    на определённое количество символов. Смещение зависит от ключа.
    text - шифруемый текст
    key - ключ шифрования, если ключ положительный, то происходит смешение в лево,
         если отрицательный то смещение в право.
    '''
    dictionary_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    dictionary_ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    dictionary_en= "abcdefghijklmnopqrstuvwxyz"
    dictionary_en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_text =''
    for letter in text:
        if dictionary_ru.find(letter)>-1:
            new_text+=dictionary_ru[(dictionary_ru.find(letter)+key)%32]
        elif dictionary_ru_upper.find(letter)>-1:
             new_text+=dictionary_ru_upper[(dictionary_ru_upper.find(letter)+key)%32]
        elif dictionary_en.find(letter)>-1:
            new_text+=dictionary_en[(dictionary_en.find(letter)+key)%25]
        elif dictionary_en_upper.find(letter)>-1:
             new_text+=dictionary_en_upper[(dictionary_en_upper.find(letter)+key)%25]
        else:
            new_text+=letter
    return new_text

def decoder_caesar(text:str,key:int):
    '''
    Декодирование по "Шифру Цезаря", смещение каждой буквы происходит в лево или право по алфавиту
    на определённое количество символов. Смещение зависит от ключа.
    text - декодируемый текст
    key - ключ декодирования, если ключ отрицательный то происходит смешение в лево,
         если положительный то смещение в право.
    '''
    dictionary_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    dictionary_ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    dictionary_en= "abcdefghijklmnopqrstuvwxyz"
    dictionary_en_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_text =''
    for letter in text:
        if dictionary_ru.find(letter)>-1:
            new_text+=dictionary_ru[(dictionary_ru.find(letter)-key)%32]
        elif dictionary_ru_upper.find(letter)>-1:
             new_text+=dictionary_ru_upper[(dictionary_ru_upper.find(letter)-key)%32]
        elif dictionary_en.find(letter)>-1:
            new_text+=dictionary_en[(dictionary_en.find(letter)-key)%25]
        elif dictionary_en_upper.find(letter)>-1:
             new_text+=dictionary_en_upper[(dictionary_en_upper.find(letter)-key)%25]
        else:
            new_text+=letter
    return new_text


key = Base.check_number('Введите ключ для шифрования: ')

text_lisi_in =[]

data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\Caesars_cipher_r.txt', 'r', encoding='utf-8')
for da in data:
    text_lisi_in.append(da)
data.close()

text_lisi_encoder=[]

for text in text_lisi_in:
    text_lisi_encoder.append(encoder_caesar(text,key))

data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\Caesars_cipher_w_encrypted.txt', 'w', encoding='utf-8')
for da in text_lisi_encoder:
      data.write(da)
data.close()

text_lisi_in =[]

data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\Caesars_cipher_w_encrypted.txt', 'r', encoding='utf-8')
for da in data:
    text_lisi_in.append(da)
data.close()

text_lisi_decoder=[]

for text in text_lisi_in:
    text_lisi_decoder.append(decoder_caesar(text,key))

data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\Caesars_cipher_w_decrypted.txt', 'w', encoding='utf-8')
for da in text_lisi_decoder:
      data.write(da)
data.close()