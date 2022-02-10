coding='UTF-8'


class warehouse:
    def __init__(self, name):
        self.name = name
        self.hight = hight
        self.length = length
        self.width = width

    def volume(self):
        volume_1 = self.hight * self.length * self.width
        print('Объем склада:', volume_1, 'м3')



class office_equipment:
    def new_equipment(self, name):
        print(self.name)
        office = input('Введите название подразделения, в котором установить оборудование (department_1,2,3): ')
        if office == 'department_1':
            department_1[self.name]=self.name + office
        elif office == 'department_2':
            department_2[self.name]=self.name + office
        else:
            department_3[self.name] =self.name + office

class printer(office_equipment):
    def __init__(self, name, number_formats):
        self.number_formats = number_formats
        self.name = name

class scanner(office_equipment):
    def __init__(self, name, size):
        self.size = size
        self.name = name

class copying_machine(office_equipment):
    def __init__(self, name, capacity_minite):
        self.capacity_minute = capacity_minite
        self.name = name

department_1 = {
    'Склад': 'склад_1'
}
department_2 = {
    'Склад': 'Склад_2'
}

department_3 = {
    'Склад': 'Склад_3'
}

printer_1 = printer('Принтер_1', 5)
printer_1.new_equipment('Принтер_1')
printer_2 = printer('Принтер_2', 5)
printer_2.new_equipment('Принтер_2')
scanner_1 = scanner('Сканер_1', 5)
scanner_1.new_equipment('Сканер_1')
copying_machine_1 = copying_machine('Копировальная машина_1', 45)
copying_machine_1.new_equipment('Копировальная машина_1')

print('В отделе 1:')
print(department_1)
print('В отделе 2:')
print(department_2)
print('В отделе 3:')
print(department_3)


