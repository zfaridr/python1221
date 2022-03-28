max = 15

odd_numbers_gen = (num for num in range(1, max + 1, 2))

for i in range(max):
    print(next(odd_numbers_gen))