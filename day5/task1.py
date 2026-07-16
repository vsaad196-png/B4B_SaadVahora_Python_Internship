class Car:
    def __init__(self,b,m,y):
        self.brand=b; self.model=m; self.year=y
    def display_info(self):
        print(self.brand,self.model,self.year)
Car("Toyota","Camry",2020).display_info()
Car("Honda","City",2021).display_info()
Car("Tata","Nexon",2022).display_info()
