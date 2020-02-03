class X:

    def m1(self):
        print('in m1 of X')


class Y(X):

    def m2(self):
        print('in m2 of Y')


class Z(Y):

    def m3(self):
        print('in m3 of Z')


z1_ = Z()
a_ = z1_.__hash__()
print(a_)
z1_.m3()
z1_.m2()
z1_.m1()
