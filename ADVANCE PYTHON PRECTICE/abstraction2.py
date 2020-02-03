class X:
    __a = 1000
    def __m1(self):
        print("in m1 of x")
class Y(X):
    __b = 2000
    def __m2(self):
        print("in m2 of y")
    def display(self):
        print(Y.__b)
        self.__m2()
        print(self._X__a)
        self._X__m1()
        
y1=Y()
y1.display()
