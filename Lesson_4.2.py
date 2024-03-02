five_digit_number = int(input('Введите пятизначное число: '))
units = five_digit_number % 10 # вычисляем единицы
tens = five_digit_number % 100 // 10 # вычисляем десятки
hundreds = five_digit_number % 1000 // 100 # вычисляем сотни
thousands = five_digit_number % 10000 // 1000 # вычисляем тысячи
tens_of_thousands = five_digit_number // 10000 # вычисляем десятки тысяч
print((tens ** units) * hundreds / (tens_of_thousands - thousands)) # выводим решение
