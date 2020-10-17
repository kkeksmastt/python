from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        for i in cycle(self.__color):
            if i == 'yellow':
                print(i)
                sleep(2)
            else:
                print(i)
                sleep(7)


traffic_light = TrafficLight()
print(traffic_light.running())
