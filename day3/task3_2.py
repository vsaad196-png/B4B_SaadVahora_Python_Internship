s = [
    {"name": "Riya", "marks": 100},
    {"name": "Aman", "marks": 95}
]

high = s[0]

for i in s:
    if i["marks"] > high["marks"]:
        high = i

print(high["name"], high["marks"])