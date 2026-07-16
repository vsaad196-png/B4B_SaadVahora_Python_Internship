from functools import reduce
numbers=[10,45,25,80,60]
print(reduce(lambda a,b:a if a>b else b,numbers))
