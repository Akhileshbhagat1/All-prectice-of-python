class X:
    __a = 1000
    def __m1(self):
        print("in m1 of x")
    def display(self):
        print(X.__a)
        self.__m1()
x1=X()
x1.display()
print(x1._X__a)
x1._X__m1()
