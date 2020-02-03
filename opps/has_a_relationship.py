class X:
    a_ = 1000

    def __init__(self):
        self.b_ = 2000

    def m1(self):
        print('in m1 of X')


class Y:
    c_ = 3000

    def __init__(self):
        self.d_ = 4000

    def m2(self):
        print('in m2 of Y')

    def display(self):
        print(Y.c_)
        print(X.a_)
        print(self.d_)
        print(self.m2())
        print(X.m1(self))
        print(Y.m2(self))

        x1_ = X()
        print(x1_.b_)
        x1_.m1()


y1_ = Y()
y1_.display()


