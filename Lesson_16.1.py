class Cassa: # создаем класс "касса"
    summa = 15730 # сумма денег в кассе (может быть любой)
    def top_up(self, pokup): # метод пополнение кассы
        self.pokup = pokup

        pokup += Cassa.summa
        return f"в кассе {pokup}"

    def count_1000(self): # метод количество тысячных купюр
        print(Cassa.summa // 1000)

    def take_away(self, x): # метод забираем деньги из кассы
        if x <= self.summa:
            self.summa -=x
        else:
            return f"не достаточно денег"

action = Cassa() # объект класса
print(action.top_up(270)) # или варианты ниже
# print(action.count_1000())
# print(action.take_away(15000))
# print(action.take_away(20000))