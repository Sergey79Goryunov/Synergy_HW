class Transport: # объявляем родительский класс "транспорт"

    def __init__(self, name, max_speed, mileage): # в констукторе задаем атрибуты класса: название, скорость и пробег
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Transport): # объявляем класс наследник "автобус"

    def __init__(self, name, max_speed, mileage): # наследуем атрибуты родительского класса "транспорт"
        super().__init__(name, max_speed, mileage)

    def __str__(self): # создаем метод класса
        return "Марка автомобиля: " + self.name + " Максимальная скорость: " + str(self.max_speed) + " Пробег: " + str(self.mileage)

bus = Bus("Renault Logan", 180, 12) # создаем объект класса
print(bus) # выводим атрибуты класса "автобус" с присвоенными значениями