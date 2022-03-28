import sys

list_users = []
list_hobby = []

with open('users.csv', 'r') as file_1:
    for line in file_1:
        list_users.append(line)
        list_users = [line.rstrip() for line in list_users]

with open('hobby.csv', 'r') as file_2:
    for line in file_2:
        list_hobby.append(line)
        list_hobby = [line.rstrip() for line in list_hobby]

users_hobby = {}

if len(list_hobby) <= len(list_users):
    for i in range(len(list_users)):
        if i <= len(list_hobby)-1:
            users_hobby[list_users[i]]=list_hobby[i]
        else:
            users_hobby[list_users[i]] = 'None'
else:
    for i in range(len(list_hobby)):
        try:
            users_hobby[list_users[i]] = list_hobby[i]
        except IndexError:
            sys.exit(1)

with open('users_hobby.csv', 'w') as file_3:
    for keys, items in users_hobby.items():
        string = '{}: {} \n'.format(keys, items)
        file_3.write(string)


