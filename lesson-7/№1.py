class Matrix:
    def __init__(self, lists=None):
        if lists is None:
            lists = [[3, 2], [4, 6], [1, 4]]
        self.lists = lists
        self.my_matrix = []

    def __str__(self):
        return '\n'.join([str(i) for i in self.lists])

    def __add__(self, other):
        if len(other) == len(self.lists):
            for num, el in enumerate(other, 0):
                if len(other[num]) == len(self.lists[num]):
                    a = []
                    a.append(other[num][0] + self.lists[num][0])
                    a.append(other[num][1] + self.lists[num][1])
                    self.my_matrix.append(a)
                else:
                    return print('Матрицы не равны!')
        else:
            return print('Матрицы не равны!')
        print('\n'.join([str(i) for i in self.my_matrix]))


a = Matrix()
print(a)
a + [[4, 4], [10, 7], [11, 5]]

