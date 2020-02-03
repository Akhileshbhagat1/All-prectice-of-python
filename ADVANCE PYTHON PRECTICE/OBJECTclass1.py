class X:
    def m1(self):
        print("in m1 of x")
class Y(X):
    def m2(self):
        print("in m2 of y")
y1=Y()
print(y1)
p=y1.__str__()
print(p)
