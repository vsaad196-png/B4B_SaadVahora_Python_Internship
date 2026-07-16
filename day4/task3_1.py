def safe_division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except TypeError:
        print('Enter numbers only')

safe_division(10,2)
safe_division(10,0)
