name_1 = input('Введите первое имя ')
name_2 = input('Введите второе имя ')
name_3 = input('Введите третье имя ')
name_4 = input('Ведите четвертое имя ')
name_set = [name_1, name_2, name_3, name_4]
first_letter_names = dict()

def thesaurus():
    for i in name_set:
        name_set_sp = list(i)
        first_letter_names[name_set_sp[0]]=i


thesaurus()

print (first_letter_names)