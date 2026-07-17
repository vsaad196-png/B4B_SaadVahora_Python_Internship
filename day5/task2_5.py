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
        print(self.brand,self.model,self.speed)
s=SportsCar()
s.info()
