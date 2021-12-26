percents = dict()

for i in range(1, 100):
    if 5 <= i <= 20:
        percents[i]='процентов'
    else:
        number = str(i)
        if number[len(number) - 1] == '1':
            i = int(number)
            percents[i] = 'процент'
        elif number[len(number) - 1] == '2' or number[len(number) - 1] == '3' or number[len(number) - 1] == '4':
            i = int(number)
            percents[i] = 'процента'
        else:
            percents[i] = 'процентов'
for key, value in percents.items():
    print(key, value)
