word = input('Введите слово: ')

a_vowel=word.count('a') # считаем количество гласных a
e_vowel=word.count('e') # считаем количество гласных e
i_vowel=word.count('i') # считаем количество гласных i
o_vowel=word.count('o') # считаем количество гласных o
u_vowel=word.count('u') # считаем количество гласных u

sum_vowels=a_vowel+e_vowel+i_vowel+o_vowel+u_vowel # суммирует гласные

print("сумма гласных",sum_vowels) #суммирует количество гласных

print("сумма согласных",len(word)-sum_vowels)  # считаем все буквы вслове, минусуем гласные и выводим количество согласных

if (a_vowel==0):
    print ("гласная a False")
else:
    print("a =",a_vowel)

if (e_vowel==0):
    print ("гласная e False")
else:
    print("e =",e_vowel)

if (i_vowel==0):
    print ("гласная i False")
else:
    print("i =",i_vowel)

if (o_vowel==0):
    print ("гласная o False")
else:
    print("o =",o_vowel)

if (u_vowel==0):
    print ("гласная u False")
else:
    print("u =",u_vowel)