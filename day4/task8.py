def require_positive(fun):
    def check(a,b):
        if a<=0 or b<=0:
            print("Error! Number must be positive.")
        else:
            fun(a,b)
    return check
@require_positive
def divide(a,b):
    print(a/b)
divide(20,5)
divide(-10,2)
