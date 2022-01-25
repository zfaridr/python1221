def val_checker(func):
    def checker (arg):
        if arg < 0:
            print ('ValueError')
    return checker

@val_checker
def calc_cube(x):
    return x ** 3

a = calc_cube(-5)
print(a)

