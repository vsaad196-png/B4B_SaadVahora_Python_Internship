class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if salary>=self.__salary:
            self.__salary=salary
            print('Salary Updated')
        else:
            print('Salary Cannot Decrease')
e=Employee(20000)
print(e.get_salary())
e.set_salary(25000)
print(e.get_salary())
e.set_salary(15000)
