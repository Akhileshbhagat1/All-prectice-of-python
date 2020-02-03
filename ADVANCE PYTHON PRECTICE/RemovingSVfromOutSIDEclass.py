class X:
    def __init__(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
x1=X()
x1.display()
del x1.b

print(x1.a)
x2=X()
print(x2.a)
print(x2.b)

