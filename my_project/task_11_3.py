coding='UTF-8'
class type_error(Exception):
    def __init__(self, txt):
        self.txt = txt

i = 1
list_1 = []

while i == 1:
    try:
        item = input('Введите элемент списка: ')
        if type(int(item)) == int:
            list_1.append(int(item))
        else:
            raise type_error('Вводите только числа!')
    except ValueError:
        print('Вводите только числа')
    finally:
        answer = input('Продолжаем увеличивать список?')
        if answer != 'да' and answer != 'Да':
            break

print(list_1)
print('Продолжаем...')


