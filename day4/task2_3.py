def counter():
    c=0
    def inc():
        nonlocal c
        c+=1
        return c
    return inc
a=counter(); b=counter()
print(a(),a(),a())
print(b(),b())
