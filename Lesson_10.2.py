exponentiation_dict = {} # словарь возведения в собственную степень

for number in range(10, -6,-1):
    exponentiation_dict[number] = number ** number
print(exponentiation_dict)
