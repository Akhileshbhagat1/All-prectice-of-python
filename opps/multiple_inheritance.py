class X:

    def m1(self):
        print('in m1 of X')


class Y:

    def m2(self):
        print('in m2 of Y')


class Z(X, Y):

    def m3(self):
        print('in m3 of Z')


z1_ = Z()
z1_.m1()
z1_.m2()
z1_.m3()
