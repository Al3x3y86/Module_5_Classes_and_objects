# Ваша задача:
# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса
# Building total 
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print

class Building:
    total = 0

    def __init__(self):
        Building.total += 1
        print(self)  # Выводим созданный объект при инициализации

    def __str__(self):
        return f'Building {Building.total}'  # Переопределяем строковое представление объекта


for _ in range(40):
    b = Building()

print(f'Total buildings created: {Building.total}')



