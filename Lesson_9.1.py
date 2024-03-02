number = int(input("Введите количество элементов списка "))
set_number = list(map(int, input().split()))[:number] # вводим числа через пробел
diff_number = set(set_number) # выявляем неповторяющиеся числа

print(len(diff_number)) # выводим количество неповторяющихся чисел