def result(marks):
    low = min(marks)
    high = max(marks)
    avg = sum(marks) / len(marks)
    return low, high, avg

marks = [40, 60, 80, 70, 90]

low, high, avg = result(marks)

print(low)
print(high)
print(avg)