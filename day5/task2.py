class Counter:
    count=0
    def __init__(self): Counter.count+=1
    @classmethod
    def total(cls): print(cls.count)
for i in range(5): Counter()
Counter.total()
