stock = {"Pen": 10, "Book": 5}

# Add stock
stock["Pen"] += 5

# Sell item
item = "Book"

if item in stock:
    stock[item] -= 1
else:
    print("Product not found")

print(stock)