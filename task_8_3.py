def type_logger(func):
    def return_type (arg):
        print(arg, ': ', type(arg))
    return return_type

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5)

