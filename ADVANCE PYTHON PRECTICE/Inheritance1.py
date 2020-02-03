class X:
    a=1000
    def m1(self):
        print("in m1 of x")
class Y(X):
    b=2000
    def __init__(self):
        self.c=3000
    def m2(self):
        print("in m2 of y")
    def display(self):
        print(Y.b)
        print(self.c)
        self.m2()
        print(Y.a)
        self.m1()
y1=Y()
y1.display()



























        
