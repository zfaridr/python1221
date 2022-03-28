coding='UTF-8'

class data:
    def __int__(self, dd_mm_yyyy):
        self.date = dd_mm_yyyy

    @classmethod
    def extract_date(cls, dd_mm_yyyy):
        new_list = dd_mm_yyyy.split('-')
        day = int(new_list[0])
        month = int(new_list[1])
        year = int(new_list[2])
        print ('Сегодня ', day, ' день ', month, ' месяца ', year, ' года')

    @staticmethod
    def validation(self):
        month = int(dd_mm_yyyy.split('-')[1])
        if 0 < month <= 12:
            return(data.extract_date(dd_mm_yyyy))
        else:
            print('Ошибка! В году 12 месяцев!')

dd_mm_yyyy = input('Введите дату в формате "день-месяц-год" ')
data.validation(dd_mm_yyyy)


