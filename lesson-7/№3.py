class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        self.cells += other
        return self.cells

    def __sub__(self, other):
        if self.cells > other:
            self.cells -= other
            return self.cells
        else:
            print('Клетки не могут уйти в минус')

    def __mul__(self, other):
        if other > 0:
            self.cells *= other
            return self.cells
        elif other == 0:
            print('Не стоит умножать клетки на ноль')
        else:
            print('Умножение на отрицательное число')

    def __truediv__(self, other):
        if other > 0:
            self.cells //= other
            return self.cells
        elif other == 0:
            print('Деление на ноль')
        else:
            print('Деление на отрицательное число')

    def __repr__(self):
        return f'{self.cells}'

    def make_order(self, my_len):
        b = self.cells
        a = ''
        while b > 0:
            if b > my_len:
                b -= my_len
                a += '*' * my_len + '\n'
            else:
                my_len = b
                b = 0
                a += '*' * my_len
        print(a)


a = Cell(13)
print(a + 10)
print(a - 11)
print(a * 9)
print(a / 8)
a.make_order(5)
