m = int(input('Введите максимальную массу в килограммах, которую может выдержать одна лодка: '))
n = int(input('Введите количество рыбаков: '))
a = []
b = []
for i in range(n):
    a.append(int(input('Введите вес рыбака: ')))
 
for x in range(len(a)):
    if a[x] + min(a) <= m:
        b += [[a[x], min(a)]]
        a[x] += m
        a[a.index(min(a))] += m
    else:
        if a[x] > m:
            continue
        else:
            b += [[a[x]]]
print('Минимальное количество лодок для перевозки рыбаков равно:')
print(len(b))