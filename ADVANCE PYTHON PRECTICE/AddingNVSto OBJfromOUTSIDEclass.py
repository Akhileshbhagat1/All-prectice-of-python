class X:
    def __init__(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
x1=X()
x1.display()
x1.c=3000
print(x1.b)
print(x1.c)
print(x1.c)
x2=X()
print(x2.a)
print(x2.b)
print(x2.c)
