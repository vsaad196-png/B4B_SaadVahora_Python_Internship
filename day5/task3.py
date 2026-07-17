class Circle:
    def __init__(self, radius):
        self.radius=radius

    @property
    def area(self):
        return 3.14*self.radius*self.radius

    @property
    def circumference(self):
        return 2*3.14*self.radius

c=Circle(5)
print('Radius:',c.radius)
print('Area:',c.area)
print('Circumference:',c.circumference)
