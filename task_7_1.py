coding: 'UTF-8'

import os

main_folder = input('Имя корневой папки проекта ')
folders = []
n = int(input('Количество папок '))

for i in range(n):
    folders.append(input('Введите имя папки ' + str(i) + ' '))

if not os.path.exists(main_folder):
    os.mkdir(main_folder)

for i in folders:
    dir_path = os.path.join(main_folder, i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

