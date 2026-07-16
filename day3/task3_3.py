book = {
    1: {"title": "Python", "copies": 5},
    2: {"title": "Java", "copies": 3}
}

book[1]["copies"] = book[1]["copies"] - 1

print(book)