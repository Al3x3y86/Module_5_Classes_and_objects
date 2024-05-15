# Ваша задача:
# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса
# Building total 
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print

from random import randint
class Building:
    total = 0

    def __init__(self):
        Building.total += 1


Buildings = []
Building_size = randint(1, 40)
while len(Buildings) < Building_size:
    new_Building = Building()
    Buildings.append(new_Building)
print(Building.total)



