list_1 = []
with open('ngins_logs.txt.txt', 'r', encoding='utf-8') as file:
    for line in file:
        list_1.append(line)
remote_adr = []

for i in range(len(list_1)):
    i_list = list_1[i].split(' ')
    remote_adr.append(i_list[0])

count_list = []
counted = []
for i in range(len(remote_adr)):
    if remote_adr[i] not in counted:
        count_list.append(remote_adr.count(remote_adr[i]))
        counted.append(remote_adr[i])

print(
    'Спамер с IP ',
    remote_adr[count_list.index(max(count_list))],
    ' отправил ',
    max(count_list),
    ' запросов.'
)
