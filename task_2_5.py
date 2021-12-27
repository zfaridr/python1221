prices = [53.12, 44.34, 89.45, 12.87, 127.6, 6.18, 83.88, 32.78, 56.54, 99.99, 49.59, 45.18, 67.55, 54.02, 3.18, 57.18]

text_prices = 'цены'

for i in prices:
    i = str(i)
    i_separated = i.split('.')
    if len(i_separated[0]) < 2:
        i_separated[0] = '0' + i_separated[0]
    if len(i_separated[1]) < 2:
        i_separated[1] = '0' + i_separated[1]
    i = i_separated[0] + ' руб ' + i_separated[1] + ' коп' + ','
    text_prices = text_prices + ' ' + i

print(text_prices)
identification_before = id(prices)
print(identification_before)
prices.sort()
identification_after = id(prices)
print(identification_after)
if identification_before == identification_after:
    print('объект остался тот же')
else:
    print('объект поменялся')
print(prices)

prices_s = sorted(prices, reverse=True)
print(prices_s)
print(prices_s[0:5])
prices_s_r = sorted(prices_s[0:5])
print(prices_s_r)
text_prices_s = 'цены'
for i in prices_s_r[0:5]:
    i = str(i)
    i_separated_s = i.split('.')
    if len(i_separated_s[0]) < 2:
        i_separated_s[0] = '0' + i_separated_s[0]
    if len(i_separated_s[1]) < 2:
        i_separated_s[1] = '0' + i_separated_s[1]
    i = i_separated_s[0] + ' руб ' + i_separated_s[1] + ' коп' + ','
    text_prices_s = text_prices_s + ' ' + i
print(text_prices_s)