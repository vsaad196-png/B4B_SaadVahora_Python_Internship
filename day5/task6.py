class Rectangle:
    def __init__(self,w,h):
        self.width=w
        self.height=h
    def __eq__(self,other):
        return self.width*self.height==other.width*other.height
r1=Rectangle(4,5)
r2=Rectangle(2,10)
print('Equal' if r1==r2 else 'Not Equal')
