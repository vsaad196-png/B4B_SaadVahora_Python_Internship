num = [10, 25, 15, 40, 50]

first = num[0]
second = num[0]

for i in num:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("Second largest number is:", second)