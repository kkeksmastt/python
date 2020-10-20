from abc import abstractmethod


class Dress:
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc(self):
        pass


class Coat(Dress):
    @property
    def calc(self):
        return self.size / 6.5 + 0.5


class Suit(Dress):
    @property
    def calc(self):
        return 2 * self.size + 0.3


a = Coat(10)
b = Suit(10)
print(a.calc)
print(b.calc)