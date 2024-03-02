a = int(input()) # введите число а
b = int(input()) # введите число b

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ') # вывод четных чисел через пробел