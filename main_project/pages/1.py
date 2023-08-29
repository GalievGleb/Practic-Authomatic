print('Сrенерировать список от 0 до 100 отсортированный на убывание, где числа нечётные и кратны 3')
# result: list = None
result = []

for x in range(100, 0, -1):
    if x % 3 == 0 and x % 2 != 0:
        result.append(x)

print(f'Результат: {result}\n')
