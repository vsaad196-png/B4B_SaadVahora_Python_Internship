mode="Global"
def outer():
    mode="Outer"
    def inner():
        mode="Inner"
        print(mode)
    inner()
    print(mode)
outer()
print(mode)
