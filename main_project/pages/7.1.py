# Написать класс Vector с двумя полями x и y типа инт
# Реализовать возможность сложения двух объектов класса Vector через оператор сложения "+"
# В результате сложения получается новый объект класса Vector
# Реализовать возможность сравнить два объекта класса Vector через оператор сравнения '=='
class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Можно складывать только объекты Vector")

    def __eq__(self, other):
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y


# Создаем объекты Vector
v1 = Vector(x=1, y=1)
v2 = Vector(x=4, y=-5)

# Складываем объекты Vector
v3 = v1 + v2

print(f"Результирующий вектор: x={v3.x}, y={v3.y}")

# Проверяем, что оператор сравнения работает корректно
assert v3.x == 5
assert v3.y == -4
assert Vector(4, -5) == v2