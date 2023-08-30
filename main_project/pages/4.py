print('Объединить два списка в один (желательно несколько способов)')
a = [1, 2, 3]
b = [3, 4, 5]
result_1: list = None
result_2: list = None

result_1 = a + b  # Можно также записать как result_1 = b + a для другого порядка
result_2 = a.copy()  # Создаем копию списка a, чтобы не изменять оригинальный список
print(result_2)
result_2.extend(b)   # Расширяем список a элементами из списка b
print(result_2)

print(f'Результат 1-ый : {result_1}')
print(f'Результат 2-ой : {result_2}\n')
