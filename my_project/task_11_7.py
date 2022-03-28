class complex_numbers:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return (
            self.number + other.number
        )
    def __mul__(self, other):
        return (
            self.number + other.number
        )
class complex_num_1(complex_numbers):
    def __add__(self, other):
        return (
            2 * self.number + other.number
        )
    def __mul__(self, other):
        return (
            3 * self.number * other.number
        )

complex_1 = complex_num_1(34)
complex_2 = complex_num_1(12)

complex_3 = complex_1 + complex_2
complex_4 = complex_1 * complex_2

print(complex_3)
print(complex_4)