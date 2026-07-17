class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @property
    def kelvin(self):
        return self.celsius+273.15
t=Temperature(30)
print('Celsius:',t.celsius)
print('Kelvin:',t.kelvin)
