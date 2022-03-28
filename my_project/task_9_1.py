coding: "utf-8"

import time
import sys

class traffic_light:
    def __init__(self, colour1, colour2, colour3):
        self.__colour1 = colour1
        self.__colour2 = colour2
        self.__colour3 = colour3

    def running(self):
        if self.__colour1 == 'red' or self.__colour1 == 'Red':
            print(f'{self.__colour1}')
            time.sleep(7)
        else:
            print('Нарушен порядок переключения цветов')
            sys.exit()
        if self.__colour2 == 'yellow' or self.__colour2 == 'Yellow':
            print(f'{self.__colour2}')
            time.sleep(2)
        else:
            print('Нарушен порядок переключения цветов')
            sys.exit()
        if self.__colour3 == 'green' or self.__colour3 == 'Green':
            print(f'{self.__colour3}')
            time.sleep(4)
        else:
            print('Нарушен порядок переключения цветов')
            sys.exit()

        print('You can go')

lights = traffic_light('red', 'yellow', 'green')
lights.running()


