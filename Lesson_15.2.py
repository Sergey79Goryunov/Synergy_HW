class Transport: # объявляем родительский класс "транспорт"

    def __init__(self, name, max_speed, mileage): # в конструкторе задаем атрибуты класса: название, скорость и пробег
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity): # создаем метод класса
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport): # объявляем класс наследник "автобус"

    def seating_capacity(self, capacity = 50): # задаем методу значение вместимости
        return super ().seating_capacity (capacity = 50)

School_bus = Autobus("Renault Logan:", 180, 12) # создаем объект класса
print(School_bus.seating_capacity()) # выводим название и вместимость