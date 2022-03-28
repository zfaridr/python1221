list_1 = []
with open('ngins_logs.txt.txt', 'r', encoding='utf-8') as file:
    for line in file:
        list_1.append(line)
remote_adr = []
request_type = []
requested_sources = []

for i in range(len(list_1)):
    i_list = list_1[i].split(' ')
    remote_adr.append(i_list[0])
    i_list[5] = i_list[5][1:]
    request_type.append(i_list[5])
    requested_sources.append(i_list[6])

final_list = []
for i in range(len(remote_adr)):
    set = (remote_adr[i], request_type[i], requested_sources[i])
    final_list.append(set)

print(final_list, type(final_list))
