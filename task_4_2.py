import requests

currency_code = input('Введите код валюты ')
def currency_rates(currency_code):
    rate_from_site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    number_1 = rate_from_site.text.find(currency_code)
    number_2 = rate_from_site.text.find('Value', number_1)
    g = (number_2 + 6)
    n = (number_2 + 12)
    course_2 = rate_from_site.text[g: n]
    course_numbers = []
    for i in course_2:
        try:
            i_number = int(i)
        except ValueError:
            course_numbers.append('.')
        else:
            course_numbers.append(i)
    course_string = ''
    for i in course_numbers:
        course_string = course_string + i
    course = float(course_string)
    print(type(course))
    print(course)
    print('Курс рубля к ' + currency_code + ' ' + course_string)

currency_rates(currency_code)
