class X:
    def m1(self):
        print ("in m1 of x")
    def m2(self):
        print("in m2 of x")
class Y(X):
    def m1(self):
        print("in m1 of y")
    def m3(self):
        print("in m3 of y")
    def display(self):
        self.m1()
        super().m1()
        self.m2()
        self.m3()
y1=Y()
y1.display()

