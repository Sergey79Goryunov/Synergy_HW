a = set(input('Введите числа первого списка: ').split())
b = set(input('Введите числа второго списка: ').split())

print (f'Количество повторяющихся чисел в списках: {len(a.intersection(b))}')