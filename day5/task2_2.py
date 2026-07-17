class Employee:
    def calculate_salary(self):
        return 10000
class Developer(Employee):
    def calculate_salary(self):
        return 10000+5000
class Designer(Employee):
    def calculate_salary(self):
        return 10000+3000

print("employee salary",Employee().calculate_salary())
print("developer salary:",Developer().calculate_salary())
print("designer salary",Designer().calculate_salary())
