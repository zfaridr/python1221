import os
import sys
import shutil

if not os.path.exists('my_project'):
    os.mkdir('my_project')

dir_path_1 = os.path.join('my_project', 'settings')
if not os.path.exists(dir_path_1):
        os.makedirs(dir_path_1)
dir_path_2 = os.path.join('my_project', 'mainapp')
if not os.path.exists(dir_path_2):
        os.makedirs(dir_path_2)
dir_path_2_1 = os.path.join('my_project', 'mainapp', 'templates')
if not os.path.exists(dir_path_2_1):
        os.makedirs(dir_path_2_1)
dir_path_2_1_1 = os.path.join('my_project', 'mainapp', 'templates', 'mainapp')
if not os.path.exists(dir_path_2_1_1):
        os.makedirs(dir_path_2_1_1)
dir_path_3 = os.path.join('my_project', 'authapp')
if not os.path.exists(dir_path_3):
        os.makedirs(dir_path_3)
dir_path_3_1 = os.path.join('my_project', 'authapp', 'templates')
if not os.path.exists(dir_path_3_1):
        os.makedirs(dir_path_3_1)
dir_path_3_1_1 = os.path.join('my_project', 'authapp', 'templates', 'authapp')
if not os.path.exists(dir_path_3_1_1):
        os.makedirs(dir_path_3_1_1)
dir_path_4 = os.path.join('my_project', 'templates')
if not os.path.exists(dir_path_4):
        os.makedirs(dir_path_4)
with open('my_project/settings/__init__.py', 'a', encoding='utf-8') as new_file:
        print('__init__.py', ' создан')
with open('my_project/settings/dev.py', 'a', encoding='utf-8') as new_file:
        print('dev.py', ' создан')
with open('my_project/settings/prod.py', 'a', encoding='utf-8') as new_file:
        print('prod.py', ' создан')
with open('my_project/mainapp/__init__.py', 'a', encoding='utf-8') as new_file:
        print('__init__.py', ' создан')
with open('my_project/mainapp/models.py', 'a', encoding='utf-8') as new_file:
        print('models.py', ' создан')
with open('my_project/mainapp/views.py', 'a', encoding='utf-8') as new_file:
        print('views.py', ' создан')
with open('my_project/mainapp/templates/mainapp/base.html', 'a', encoding='utf-8') as new_file:
        print('base.html', ' создан')
with open('my_project/mainapp/templates/mainapp/index.html', 'a', encoding='utf-8') as new_file:
        print('index.html', ' создан')
with open('my_project/authapp/__init__.py', 'a', encoding='utf-8') as new_file:
        print('__init__.py', ' создан')
with open('my_project/authapp/models.py', 'a', encoding='utf-8') as new_file:
        print('models.py', ' создан')
with open('my_project/authapp/views.py', 'a', encoding='utf-8') as new_file:
        print('views.py', ' создан')
with open('my_project/authapp/templates/authapp/base.html', 'a', encoding='utf-8') as new_file:
        print('base.html', ' создан')
with open('my_project/authapp/templates/authapp/index.html', 'a', encoding='utf-8') as new_file:
        print('index.html', ' создан')

shutil.copytree('my_project/authapp/templates/authapp', 'my_project/templates/authapp')
shutil.copytree('my_project/mainapp/templates/mainapp', 'my_project/templates/mainapp')




