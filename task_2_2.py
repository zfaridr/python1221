initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(initial_list)
final_list = []
for i in initial_list:
    try:
        i_number = int(i)
    except ValueError:
        final_list.append(i)
    else:
        final_list.append('"')
        i_check = int(i)
        if i_check >= 10:
            final_list.append(i)
        elif len(i) < 2:
            i = '0' + i[:1]
            final_list.append(i)
        elif len(i) == 2:
            i = i[0] + '0' + i[1]
            final_list.append(i)
        final_list.append('"')

print(final_list)

text = final_list[0]
k = 1
while k < len(final_list):
    if k == 3 or k == 7 or k == 14 or k == 2 or k == 6 or k == 13:
        text = text + final_list[k]
    else:
        text = text + " " + final_list[k]
    k = k + 1

print(text)










