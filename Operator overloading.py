
# Ваша задача:
# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности
# self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения


class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors) and (self.buildingType == other.buildingType)

# Cравнения
building1 = Building(5, "residential")
building2 = Building(5, "residential")
building3 = Building(5, "office")

print(building1 == building2)
print(building1 == building3)
