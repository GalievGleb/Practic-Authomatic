# Написать абстрактный класс "Figure", в котором содержится пустой метод calc_area()
# Написать классы "Square", "Circle", которые наследуются и переопределяют метод calc_area() для каждой фигуры
# Класс "Square" имеет поле side (сторона) типа int
# Класс "Circle" имеет поле radius (радиус) типа int
from math import pi
print('Написать абстракцию, и классы которые наследуются и переопределяют метод')


class Figure:
    def calc_area(self):
        raise NotImplementedError("Метод calc_area() должен быть переопределен в подклассе")

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side ** 2

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return pi * self.radius ** 2

square = Square(side=4)
circle = Circle(radius=3)

print(f'Площадь Квадрата={square.calc_area()}')
print(f'Площадь Круга={circle.calc_area()}')

assert square.calc_area() == 16, 'Неверно посчитана площадь квадрата!'
assert round(circle.calc_area(), 9) == 28.274333882, "Неверно посчитана площадь круга!"
