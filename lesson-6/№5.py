class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Пишем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Пишем маркером')


pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()
