min_sum_inv = int(input("Минимальная сумма инвестиций "))
michael = int(input("Cколько долларов у Майкла "))
ivan = int(input("Сколько долларов у Ивана "))

if (michael >= min_sum_inv) and (ivan >= min_sum_inv):
    print(2)
elif (michael >= min_sum_inv) and (ivan <= min_sum_inv):
    print("Mike")
elif (michael <= min_sum_inv) and (ivan >= min_sum_inv):
    print("Ivan")
elif (michael <= min_sum_inv) and (ivan <= min_sum_inv) and ((michael + ivan) >= min_sum_inv):
    print(1)
elif (michael <= min_sum_inv) and (ivan <= min_sum_inv) and ((michael + ivan) <= min_sum_inv):
    print(0)