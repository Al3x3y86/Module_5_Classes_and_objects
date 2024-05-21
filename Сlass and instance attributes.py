# Ваша задача:
# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса
# Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print

class Building:
    total = 0

    def __init__(self):
        Building.total += 1

# Создаем 40 объектов класса Building
for _ in range(40):
    b = Building()
    print(f'Building {Building.total}')  # Выводим созданный объект на экран



