class Car:
    def __init__(self, cost, color, mileage):
        self.cost = cost
        self.color = color
        self.mileage = mileage
    def drive(self):
        print("Vroom vroom!")
        self.mileage += 50

car1 = Car(30000, "blue", 10000)
car2 = Car(1000000, "gold", 0)

car1.drive()
car2.drive()
print(car1.mileage)
print(car2.mileage)
