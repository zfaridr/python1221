coding: 'utf-8'
import re
e_mail = input('Введите email ')

splitted = re.split(r'@', e_mail)
info = {
    'username': splitted[0],
    'domain': splitted[1]
}
print(info)