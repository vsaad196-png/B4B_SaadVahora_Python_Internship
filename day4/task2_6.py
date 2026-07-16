def make_validator(min_value):
    def check(n):
        print(n>=min_value)
    return check
v1=make_validator(10)
v2=make_validator(20)
v1(15); v1(5)
v2(25); v2(15)
