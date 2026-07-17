class Bird:
    def fly(self):
        print("Bird can fly")
class Airplane:
    def fly(self):
        print("Airplane can fly")
class Drone:
    def fly(self):
        print("Drone can fly")
def show(obj):
    obj.fly()
show(Bird())
show(Airplane())
show(Drone())
