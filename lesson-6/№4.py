class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_pilice = is_police

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Остоновка')

    def turn(self, direction):
        print(f'Повернули {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость! Текущая скорость {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость! Текущая скорость {self.speed} км/ч')
        else:
            print(f'Текущая скорость {self.speed} км/ч')


class PoliceCar(Car):
    pass


town_car = TownCar(100, 'red', 'Hundai', False)
town_car.go()
town_car.turn('направо')
town_car.show_speed()
town_car.stop()

sport_car = SportCar(200, 'green', 'Porshe', False)
sport_car.go()
sport_car.turn('направо')
sport_car.show_speed()
sport_car.stop()

police_car = PoliceCar(150, 'red', 'Hundai', True)


work_car = WorkCar(40, 'yellow', 'Hundai', False)