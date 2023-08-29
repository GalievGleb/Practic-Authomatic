# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго - соответственно
#  вначениями нашего словаря.
# Желательно несколько решений
list1: list = ['a', 'b', 'c', 'd']
list2: list = [1, 2, 3, 4]

result_1: dict = None
result_2: dict = None

result_1 = {}
for i in range(len(list1)):
    result_1[list1[i]] = list2[i]

result_2 = dict(zip(list1, list2))

print(f'Результат : {result_1}')
print(f'Результат : {result_2}')