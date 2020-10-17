class Worker:
    def __init__(self):
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.position = 'programer'
        self._income = {'wage': 50000, 'bonus': 10000}


class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname


    def get_total_income(self):
        a, b = self._income.values()
        return a + b


a = Position()
print(a.get_full_name())
print(a.get_total_income())
