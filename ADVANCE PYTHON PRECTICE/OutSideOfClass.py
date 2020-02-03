class X:
    a=1000
    b=2000
    def display(self):
        print(X.a)
        print(X.b)
x1=X()
x1.display()
X.c=3000
print(X.a)
print(X.b)
print(X.c)
