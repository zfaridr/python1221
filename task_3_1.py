user_number = input('Введите число на английском языке ')

numbers_translations = {
    'zero':'ноль',
    'one':'один',
    'two':'два',
    'three':'три',
    'four':'четыре',
    'five':'пять',
    'six':'шесть',
    'seven':'семь',
    'eight':'восемь',
    'nine':'девять',
    'ten':'десять'
}

def num_translate(number):
    print (numbers_translations.get(number, 'None'))

num_translate(user_number)