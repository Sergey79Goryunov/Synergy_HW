num_zero = 0 # фиксируем счетчик нулей на ноль
for i in range(int(input())): # задаем число, например 5, вводим по очереди пять любых чисел
    if int(input()) == 0: # проверяем если в вводе есть нули
        num_zero += 1 # считаем нули
print(num_zero) # выводим количество посчитанных нулей