words = ["apple", "ant", "banana", "bat", "cat", "carrot"]

d = {}

for i in words:
    d.setdefault(i[0], []).append(i)

print(d)