class X:

    def m1(self):
        print('in m1 of X')


class Y(X):

    def m2(self):
        print('in m2 of Y')


class Z(X):

    def m3(self):
        print('in m3 of Z')


y1_ = Y()
a = y1_.__hash__()
print(a)
y1_.m1()
y1_.m2()

z1_ = Z()
b = z1_.__hash__()
print(b)
z1_.m1()
z1_.m3()

