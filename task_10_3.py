coding="utf-8"

class cells:
    def __init__(self, box_numbers, in_row):
        self.box_numbers = box_numbers
        self.in_row = in_row
    def __add__(self, other):
         return cells(
            self.box_numbers + other.box_numbers,
            self.in_row
         )
    def __sub__(self, other):
        if self.box_numbers > other.box_numbers:
            return cells(
                self.box_numbers - other.box_numbers,
                self.in_row
            )
        elif other.box_numbers > self.box_numbers:
            return cells(
                other.box_numbers - self.box_numbers,
                self.in_row
            )
        else:
            print('Разность равна 0')

    def __mul__(self, other):
         return cells(
            self.box_numbers * other.box_numbers,
            self.in_row
         )

    def __floordiv__(self, other):
        if self.box_numbers > other.box_numbers:
            return cells(
                self.box_numbers // other.box_numbers,
                self.in_row
            )
        else:
            return cells(
                other.box_numbers // self.box_numbers,
                self.in_row
            )
    def make_order(self):
        for i in range(self.box_numbers // self.in_row):
            row = ''
            for i in range(self.in_row):
                row = row + '*'
            print (row)

        last_row = ''
        for i in range(self.box_numbers % self.in_row):
            last_row = last_row + '*'
        print(last_row)




cell_1 = cells(16, 4)
cell_2 = cells(13, 5)

cell = cell_1 + cell_2
print(cell.box_numbers)
cell = cell_1 - cell_2
print(cell.box_numbers)
cell = cell_1 * cell_2
print(cell.box_numbers)
cell = cell_1 // cell_2
print(cell.box_numbers)
cell_1.make_order()
cell_2.make_order()