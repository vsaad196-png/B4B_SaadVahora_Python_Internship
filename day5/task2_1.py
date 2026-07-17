class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course
    def study(self):
        print(self.name,"is studying",self.course)

s=Student("Ali",20,"Python")
s.study()
