coding='UTF-8'

class zero_dev_error(Exception):
    def __init__(self, txt):
        self.txt = txt

number = input('Введите число ')
try:
    user_number = int(number)
    if user_number == 0:
        raise zero_dev_error('На ноль делить нельзя)')

except zero_dev_error as err_1:
    print(err_1)

else:
    print(12/user_number)

print('Продолжаем...')

