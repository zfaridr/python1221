duration = int(input('Введите количество секунд '))
print(type(duration))

if duration <= 60:
    print (duration, 'сек')
elif duration <= 3600:
    min = duration // 60
    sec = duration % 60
    print (min, 'мин', sec, 'сек')
elif duration <= 86400:
    hours = duration // 3600
    min = (duration % 3600) // 60
    sec = (duration % 3600) % 60
    print(hours, 'ч', min, 'мин', sec, 'сек')
else:
    days = duration // 86400
    hours = (duration % 86400) // 3600
    min = ((duration % 86400) % 3600) // 60
    sec = ((duration % 86400) % 3600) % 60
    print(days, 'сут', hours, 'ч', min, 'мин', sec, 'сек')

