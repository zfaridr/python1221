coding: "UTF-8"

class stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class pen(stationery):
    def draw(self):
        print('Применение ручки')
class pencil(stationery):
    def draw(self):
        print('Применение карандаша')
class handle(stationery):
    def draw(self):
        print('Применение маркера')

info_1 = stationery('Отрисовка')
info_2 = pen('Ручка')
info_3 = pencil('Карандаш')
info_4 = handle('Маркер')

info_1.draw()
info_2.draw()
info_3.draw()
info_4.draw()
