def get_value(lst,i):
    try:
        return lst[i]
    except IndexError:
        return None

print(get_value([1,2,3],5))
