class X:
    __a=1000
    def __m1(self):
        print("in m1 of x")
    def display(self):
        print(X.__a)
        self.__m1()
x1 = X()
x1.display()
# print(_X__m1())
x1._X__m1()
