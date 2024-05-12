
# Ваша задача:
# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на
# параметр floors и выводить в консоль numberOfFloors


class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Новое количество этажей:", self.numberOfFloors)

my_house = House()
my_house.setNewNumberOfFloors(5)
