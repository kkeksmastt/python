class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, weight, thickness):
        return self._width * self._length * weight * thickness


a = Road(10000, 20)
print(a.mass(25, 4))
