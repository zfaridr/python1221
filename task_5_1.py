def odd_nums(max):
    for number in range(1, max + 1, 2):
        yield number

max = 15
odd_numbers = odd_nums(max)

for i in range(max):
    print(next(odd_numbers))