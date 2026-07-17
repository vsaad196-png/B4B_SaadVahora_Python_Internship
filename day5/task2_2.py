class Employee:
    def calculate_salary(self):
        return 10000
class Developer(Employee):
    def calculate_salary(self):
        return 10000+5000
class Designer(Employee):
    def calculate_salary(self):
        return 10000+3000
print(Developer().calculate_salary())
print(Designer().calculate_salary())
