coding='UTF-8'
from abc import ABC, abstractmethod

class abstract_class(ABC):
    @abstractmethod
    def texture_amount(self):
        pass

class clothes(abstract_class):
    def __init__(self, item, VH):
        self.item = item
        self.size = VH

    @property
    def texture_amount(self):
        if self.item == 'пальто':
            amount = round(self.size/6.5 + 0.5, 2)
            print(amount)
        elif self.item == 'костюм':
            amount = round(2*self.size + 0.3, 2)
            print(amount)
        else:
            print('Одежда не распознана, введите "костюм" или "пальто"')

clothes_1 = clothes('костюм', 47.23)
print(clothes_1.texture_amount)

