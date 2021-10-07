import os
import sys
import shutil
from pathlib import Path

a = {}
pyt = ''
f = open('put.txt')
for c in f:
    pyt = c
z = pyt
os.chdir(pyt)


# создание папки################################
def pap(w):
    try:
        os.mkdir(w)
    except FileExistsError:
        print('Такая папка же существует')


###############################################
# Удаление папки################################
def delete(w):
    try:
        os.rmdir(w)
    except FileNotFoundError:
        print('Такой папки не существует')


###############################################
# Вывод текущей директории######################
def dir():
    print(os.getcwd())


###############################################
# Просмотр каталога ######################
def cont():
    print(os.listdir(os.getcwd()))


###############################################
# Переход вниз######################
def per_vn(w):
    if w not in (os.listdir(os.getcwd())):
        print('Такой папки нет')
    else:
        os.chdir(w)
        print(os.getcwd())


###############################################
# Переход наверх######################
def per_vv():
    if len(os.path.split(os.getcwd())[0]) >= len(z) or len(os.path.split(os.getcwd())[0]) + 1 >= len(z):
        os.chdir(os.path.split(os.getcwd())[0])
        print(os.getcwd())
    else:
        print("Дальше нельзя!!!")
        print(os.getcwd())


###############################################
# Создание пустого файла######################
def create(w):
    if w not in (os.listdir(os.getcwd())):
        file = open(w, "w+")
        file.close()
    else:
        print("Такой файл уже есть")


###############################################
# Запись в файл######################
def add(file, w):
    if file not in (os.listdir(os.getcwd())):
        print("Такого файла нет")
    else:
        f = open(file, "a")
        f.write(w)
        f.close()


###############################################
# Просмотр файла######################
def cet(w):
    if w not in (os.listdir(os.getcwd())):
        print("Такого файла нет")
    else:
        file = open(w, "r")
        print(file.read())
        file.close()


###############################################
# Удаление файла######################
def rem(w):
    if w not in (os.listdir(os.getcwd())):
        print("Такого файла нет")
    else:
        os.remove(w)


###############################################
# Копирование файла######################
def cop(w, p):
    pu1 = ''
    pu2 = ''
    k1 = []
    k2 = []
    filename = w
    for root, dirnames, filenames in os.walk(pyt):
        for file in filenames:
            if file == filename:
                k1.append(os.path.join(root, file))
    if len(k1) == 0:
        print("Такого файла нет")
    if len(k1) == 1:
        pu1 = k1[0]
    if len(k1) > 1:
        print("Нашлось много таких файлов выберите точный путь")
        for i in range(len(k1)):
            print(i + 1, ') ', k1[i])
        e = int(input('Введите номер пути: '))
        while e < 0 or e > len(k1):
            print("Что-то не то")
            z = int(input('Введите номер пути: '))
        pu1 = k1[e - 1]
    for root, dirnames, filenames in os.walk(pyt):
        for file in dirnames:
            if file == p:
                k2.append(os.path.join(root, file))
    if len(k2) == 0:
        print("Такой папки нет")
    if len(k2) == 1:
        pu2 = k2[0]
    if len(k2) > 1:
        print("Нашлось много таких папок выберите точный путь")
        for i in range(len(k2)):
            print(i + 1, ') ', k2[i])
        e = int(input('Введите номер пути: '))
        while e < 0 or e > len(k2):
            print("Что-то не то")
            e = int(input('Введите номер пути: '))
        pu1 = k2[z - 1]
    if pu1 != '' and pu2 != '':
        shutil.copy(pu1, pu2)
    else:
        print("НЕЛЬЗЯ ВЫПОЛНИТЬ")


###############################################
# Перемещение файла######################
def per(w, p):
    pu1 = ''
    pu2 = ''
    k1 = []
    k2 = []
    filename = w
    for root, dirnames, filenames in os.walk(pyt):
        for file in filenames:
            if file == filename:
                k1.append(os.path.join(root, file))
    if len(k1) == 0:
        print("Такого файла нет")
    if len(k1) == 1:
        pu1 = k1[0]
    if len(k1) > 1:
        print("Нашлось много таких файлов выберите точный путь")
        for i in range(len(k1)):
            print(i + 1, ') ', k1[i])
        e = int(input('Введите номер пути: '))
        while e < 0 or e > len(k1):
            print("Что-то не то")
            e = int(input('Введите номер пути: '))
        pu1 = k1[e - 1]
    for root, dirnames, filenames in os.walk(pyt):
        for file in dirnames:
            if file == p:
                k2.append(os.path.join(root, file))
    if len(k2) == 0:
        print("Такой папки нет")
    if len(k2) == 1:
        pu2 = k2[0]
    if len(k2) > 1:
        print("Нашлось много таких папок выберите точный путь")
        for i in range(len(k2)):
            print(i + 1, ') ', k2[i])
        e = int(input('Введите номер пути: '))
        while e < 0 or e > len(k2):
            print("Что-то не то")
            e = int(input('Введите номер пути: '))
        pu1 = k2[e - 1]
    if pu1 != '' and pu2 != '':
        try:
            shutil.move(pu1, pu2)
        except IOError:
            print('Такой файл уже существует. Переменуйте файл')

    else:
        print("НЕЛЬЗЯ ВЫПОЛНИТЬ")


###############################################
###Переименование файла########################
def nam(w, n):
    pu1 = ''
    k1 = []
    filename = w
    for root, dirnames, filenames in os.walk(pyt):
        for file in filenames:
            if file == filename:
                k1.append(os.path.join(root, file))
    if len(k1) == 0:
        print("Такого файла нет")
    if len(k1) == 1:
        pu1 = k1[0]
    if len(k1) > 1:
        print("Нашлось много таких файлов выберите точный путь")
        for i in range(len(k1)):
            print(i + 1, ') ', k1[i])
        e = int(input('Введите номер пути: '))
        while e < 0 or e > len(k1):
            print("Что-то не то")
            e = int(input('Введите номер пути: '))
        pu1 = k1[e - 1]

    path, filename = os.path.split(pu1)
    xx = os.path.join(path, n)
    os.rename(pu1, xx)


##############################################
print(
    "Справка по командам: \n1) Создание папки (с указанием имени) - pap;\n2) Удаление папки по имени - delete;\n3) "
    "Перемещение между папками вверх - per_vv;\n4)Перемещение между папками вниз - per_vn;\n5) Создание пустых файлов "
    "с указанием имени - create;\n6) Запись текста в файл - add;\n7) Просмотр содержимого текстового файла - cet;\n8) "
    "Удаление файлов по имени - rem;\n9) Копирование файлов из одной папки в другую - cop;\n10 Перемещение файлов - "
    "per;\n11 Переименование файлов - nam;")
while True:
    q = input("Название команды: ")
    if q == "exit":
        print("Выход")
        sys.exit()
    if q == "pap":
        w = input("Название папки:")
        pap(w)
    if q == "delete":
        w = input("Название папки:")
        delete(w)
    if q == "dir":
        dir()
    if q == 'cont':
        cont()
    if q == 'per_vn':
        w = input('Название папки: ')
        per_vn(w)
    if q == 'per_vv':
        per_vv()
    if q == 'create':
        w = input('Название файла: ')
        create(w)
    if q == 'add':
        file = input('Название файла: ')
        w = input("Текст: ")
        add(file, w)
    if q == 'cet':
        w = input('Название файла: ')
        cet(w)
    if q == 'rem':
        w = input('Название файла: ')
        rem(w)
    if q == 'cop':
        w = input('Название файла: ')
        p = input('Название папки, куда копировать: ')
        cop(w, p)
    if q == 'per':
        w = input('Название файла: ')
        p = input('Название папки, куда переносить: ')
        per(w, p)
    if q == 'nam':
        w = input('Название файла: ')
        n = input('Имя на которое менять: ')
        nam(w, n)
