class Transport: # объявляем родительский класс "транспорт"

    def __init__(self, name, max_speed, mileage): # в констукторе задаем атрибуты класса: название, скорость и пробег
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self): # создаем метод класса
        return "Название автомобиля: " + self.name + " Максимальная скорость: " + str(self.max_speed) + " Пробег: " + str(self.mileage)

Autobus = Transport("Renault Logan", 180, 12) # создаем объект класса
print(Autobus) # выводим атрибуты класса "автобус" с присвоенными значениями
