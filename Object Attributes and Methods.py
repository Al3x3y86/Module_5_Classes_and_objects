
# Ваша задача:
# Создайте новый класс House
# Задайте ему новый атрибут numberOfFloors = 10
# В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"

class House:
    def __init__(self):
        self.numberOfFloors = 10

my_house = House()

for floor in range(1, my_house.numberOfFloors + 1):
    print("Текущий этаж равен", floor)







