coding='UTF-8'

row_1_1 = [2, 4, 6, 7]
row_2_1 = [11, 3, 7, 9]
row_1_2 = [2, 5, 34, 12]
row_2_2 = [32, 72, 8, 10]
row_1_3 = [23, 6, 9, 19]
row_2_3 = [4, 12, 35, 7]

list_1 = [row_1_1, row_1_2, row_1_3]
list_2 = [row_2_1, row_2_2, row_2_3]

class matrix:
    def __init__(self, data_1):
        self.list_1 = data_1
    def matrix_print(self):
        for i in self.list_1:
            print(i)
    def __str__(self):
        print('Матрица')
        for item in self.list_1:
            text_1 = ''
            for i in item:
                if item.index(i) < (len(item)) - 1:
                    text_1 = text_1 + str(i) + ', '
                else:
                    text_1 = text_1 + str(i)

            print('|',text_1,'|')



    def __add__(self, other):
        return matrix(
            self.list_1 + other.list_1
            )
    def matrix_result(self):
        print('Матрица суммарная')
        for item in self.list_1:
            if self.list_1.index(item) <= len(self.list_1)//2 - 1:
                text_1 = ''
                for i in item:
                    item[item.index(i)] = i + self.list_1[self.list_1.index(item) + (len(self.list_1)//2)][item.index(i)]

            else:
                self.list_1.remove(item)

        for item in self.list_1:
            text_1 = ''
            for i in item:
                if item.index(i) < (len(item)) - 1:
                    text_1 = text_1 + str(i) + ', '
                else:
                    text_1 = text_1 + str(i)

            print('|', text_1, '|')



matrix_1 = matrix(list_1)
matrix_2 = matrix(list_2)
matrix_1.matrix_print()
matrix_1.__str__()


matrix_sum = matrix_1 + matrix_2
matrix_sum.__str__()
matrix_sum.matrix_result()



