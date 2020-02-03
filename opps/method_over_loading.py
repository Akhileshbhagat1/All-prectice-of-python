class X:

    def m1(self):
        print('in m1 of no parameters')

    def m1(self, a, b):
        print('in m1 of two parameter')

    def m1(self, a):
        print('in m1 of one parameter')


x1_ = X()

# x1_.m1(100)

x1_.m1(10)
x1_.m1()


