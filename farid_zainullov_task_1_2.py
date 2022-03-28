list = []
list_remove1 = []
list_remove2 = []
for i in range (1, 1000):
    if i % 2 != 0:
        list.append(i ** 3)
print(list)

for i in list:
    number = str(i)
    sum_i = 0
    k_i = 0
    while k_i <= (len(number) - 1):
        number_k = int(number[k_i])
        sum_i = sum_i + number_k
        k_i += 1
    if (sum_i % 7) != 0:
        list_remove1.append(i)

for i in list_remove1:
    if i in list:
        list.remove(i)
print(list)
print(sum(list))
list_buffer = []
for i in list:
    i = i + 17
    list_buffer.append(i)

list = list_buffer
print(list)
for i in list:
    number = str(i)
    sum_i = 0
    k_i = 0
    while k_i <= (len(number) - 1):
        number_k = int(number[k_i])
        sum_i = sum_i + number_k
        k_i += 1
    if (sum_i % 7) != 0:
        list_remove2.append(i)

for i in list_remove2:
    if i in list:
        list.remove(i)
print(list)
print(sum(list))
