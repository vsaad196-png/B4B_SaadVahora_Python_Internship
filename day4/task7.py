import time
def timer(fun):
    def show():
        s=time.time()
        fun()
        print("Time:",time.time()-s)
    return show
@timer
def add():
    t=0
    for i in range(1,1000001):
        t+=i
    print(t)
add()
