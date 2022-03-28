staff_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

engineer = staff_data[0].split()
accountant = staff_data[1].split()
lathe_operator = staff_data[2].split()
manager = staff_data[3].split()

print (engineer[0].capitalize() + ', ' + engineer[1].capitalize())
print (accountant[0].capitalize() + ' ' + accountant[1] + ', ' + accountant[2].capitalize())
print (lathe_operator[0].capitalize() + ' ' + lathe_operator[1] + ' ' + lathe_operator[2] + ', ' + lathe_operator[3].capitalize())
print (manager[0].capitalize() + ', ' + manager[1].capitalize())


