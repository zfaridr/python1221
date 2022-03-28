nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
n = int(input('Введите количество шуток '))
jokes_set = []

from random import randint

def get_jokes(y):
    i = 1
    while i <= y:
        x1 = randint(0, 4)
        x2 = randint(0, 4)
        x3 = randint(0, 4)
        new_joke = nouns[x1] + ' ' + adverbs[x2] + ' ' + adjectives[x3]
        jokes_set.append(new_joke)
        i += 1

get_jokes(n)
print (jokes_set)

