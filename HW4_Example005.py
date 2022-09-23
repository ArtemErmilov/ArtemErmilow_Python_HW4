# Задача 5

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

from os import system
system ('cls')

def RLE_encoder(text:str):
    '''
    Функция сжатия текста по RLE
    '''
    text_out=[]
    if text[0]=='\ufeff':
        text_out.append(text[1])
        index_in =1
    else:
        text_out.append(text[0])
        index_in =0
    index_=1
    for letter in text[index_in+1::]:
        
        if letter==text_out[-1]:
            index_+=1
        else:
            text_out.append(str(index_))
            text_out.append(letter)
            index_=1
    
    text_out.append(str(index_))
    
    return text_out


def RLE_decoder(list_:list):
    '''
    Распоковка текста по RLE
    '''
    text_out=''
    a=''
    for letter in list_:
        letter=str(letter)
        if letter.isdigit()==True and a!='':
            text_out=text_out+a*int(letter)
            letter=''
        a=letter
        
    return text_out



text_lisi_in =[]
# Чтение теста из файла RLE_r.txt и запись его в список text_lisi_in
data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\RLE_r.txt', 'r', encoding='utf-8')
for da in data:
    text_lisi_in.append(da)
data.close()

# Сжатие текста по RLE и запись его в список text_lisi_encoder
text_lisi_encoder=[]
for text in text_lisi_in:
    text_lisi_encoder.append(RLE_encoder(text))


# Запись сжатого текста из text_lisi_encoder в файл RLE_w_encoder.txt с разделением элементов через(,)
data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\RLE_w_encoder.txt', 'w', encoding='utf-8')
for dat in text_lisi_encoder:
    for da in dat:
        data.writelines(da)
        data.writelines(',')
data.close()

# Чтение сжатого текста из файла RLE_w_encoder.txt, и запись его в text_lisi_in_encoder
text_lisi_in_encoder=[]
data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\RLE_w_encoder.txt', 'r', encoding='utf-8')
for dat in data:
    text_lisi_in_encoder.append(dat)
data.close()

tecxt_ceng =text_lisi_in_encoder[0]

# Распаковка текста и запись его в text_lisi_decoder
text_lisi_decoder=[]
for codtext in text_lisi_in_encoder:
    text_lisi_decoder.append(RLE_decoder(codtext.split(',')))
text_lisi_decoder[0]
# Запись распоковоанного текста в файл RLE_w_decoder.txt
data = open(r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Python\Homework\HW4\RLE_w_decoder.txt', 'w', encoding='utf-8')
for dat in text_lisi_decoder:
    data.writelines(f'{dat} \n')        
data.close()

print (tecxt_ceng)
print (text_lisi_in_encoder)
print(text_lisi_decoder)
