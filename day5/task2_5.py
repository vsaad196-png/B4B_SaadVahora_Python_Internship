class Vehicle:
    def __init__(self):
        self.brand="Toyota"
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.model="Fortuner"
class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.speed=250
    def info(self):
        print("car brand:",self.brand," car model:",self.model,"  speed:",self.speed)
s=SportsCar()
s.info()
