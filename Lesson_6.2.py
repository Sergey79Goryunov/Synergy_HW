x_num = int(input('Введите натуральное число: '))
divider = 0 # фиксируем количество натуральных делителей числа

for i in range(1, x_num + 1):
    if x_num % i == 0:
        divider = divider + 1
print(divider) # выводим количество натуральных делителей числа