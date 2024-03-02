def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

a = int(input('Введите число: '))
for i in range(a, 0, -1):
    print(factorial(i)) # выводим факториалы в убывающем порядке от введенного числа