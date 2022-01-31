coding='UTF-8'

class road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass_asphalt = (self._length * self._width * 25 * 5)/1000000
        print ('Необходимая масса асфальта ', mass_asphalt, ' тыс.т')

road_1 = road(12000, 8)
road_1.mass()
