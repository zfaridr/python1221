coding='UTF-8'

class car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        print('Машина ', self.name, 'поехала')

    def stop(self):
        print('Машина ', self.name, 'остановилась')

    def turn(self):
        print('Машина ', self.name, 'повернула')

    def show_speed(self):
        print ('Скорость машины ', self.name, ' ', self.speed, ' км/ч')

class town_car(car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        print('Скорость машины ', self.name, ' ', self.speed, ' км/ч')

class work_car(car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        print('Скорость машины ', self.name, ' ', self.speed, ' км/ч')

class sport_car(car):
    def message(self):
        print('Это спортивный автомобиль')

class police_car(car):
    def message(self):
        print('Это автомобиль полиции')

car_1 = car(300, 'green', 'toyota', False)
car_2 = town_car(65, 'red', 'lexus', False)
car_3 = work_car(50, 'blue', 'lada', False)
car_4 = sport_car(350, 'red', 'ferrari', False)
car_5 = police_car(180, 'yellow', 'mazda', True)

car_1.go()
car_1.stop()
car_1.turn()
car_1.show_speed()

car_2.go()
car_2.stop()
car_2.turn()
car_2.show_speed()

car_3.go()
car_3.stop()
car_3.turn()
car_3.show_speed()

car_4.go()
car_4.stop()
car_4.turn()
car_4.show_speed()
car_4.message()

car_5.go()
car_5.stop()
car_5.turn()
car_5.show_speed()
car_5.message()

