class X:
    a=1000
    b=2000
    def display(self):
        print(X.a)
        print(X.b)
    def modify(self):
        X.a = X.a+100
        X.b = X.b-100

x1=X()
x1.display()
x1.modify()
x1.display()
x2=X()
x2.display()
x2.modify()
x2.display()
