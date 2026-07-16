count=0
def call():
    global count
    count+=1
for i in range(4): call()
print("Count:",count)
