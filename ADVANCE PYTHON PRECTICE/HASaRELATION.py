class X:
    a=1000
    def __init__(self):
        self.b=2000
    def m1(self):
        print("in m1 of x")

class Y:
    c=3000
    def __init__(self):
        self.d=4000
    def m2(self):
        print("in m2 of Y")
    def display(self):
        print(Y.c)
        print(self.d)
        self.m2()
        print(X.a)
        x1=X()
        print(x1.b)
        x1.m1()

y1=Y()
y1.display()

            
