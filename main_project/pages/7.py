# Написать класс Vector с двумя полями и у типа инт
# Реализовать возможность сложения двух объектов класса Vector через оператор сложения "+"
# В результате сложения получается новый объект класса Vector
# Реализовать возможность сравнить два объекта класса Vector через оператор сравнения '=='
print('Написать класс Vector с pеализацией сложения и сравнения объектов')
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Перегружаем оператор сложения
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Можно складывать только объекты класса Vector")

    def __eq__(self, other):
        # Перегружаем оператор сравнения ==
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False

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
