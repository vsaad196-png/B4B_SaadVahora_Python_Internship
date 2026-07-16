d = {
    "Pen": 10,
    "Book": 120,
    "Bag": 200,
    "Bottle": 50,
    "Box": 150
}

a = {
    i: d[i] 
    for i in d 
     if d[i] > 100
     }

print(a)