def build_invoice(name,*prices,**details):
    print("Customer:",name)
    print("Total Price:",sum(prices))
    for k,v in details.items():
        print(k,":",v)

build_invoice("Saad",100,200,300,discount=50,tax=20)
