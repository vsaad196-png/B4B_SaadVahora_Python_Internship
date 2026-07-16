def make_greeting(language):
    def greet(name):
        if language=="hindi": print("Namaste,",name)
        else: print("Hello,",name)
    return greet
g=make_greeting("hindi"); g("Saad")
