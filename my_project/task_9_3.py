coding='UTF-8'

income_parts = {
    'wage': '1000',
    'bonus': '500'
}

class worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income_parts

class position(worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_full_income(self):
        full_income = int(self._income['wage']) + int(self._income['bonus'])
        print('Income ', full_income)

worker_1=position('Peter', 'Parker', 'intern', income_parts)
worker_1.get_full_name()
worker_1.get_full_income()