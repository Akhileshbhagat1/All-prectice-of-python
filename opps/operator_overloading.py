import math


class Circle:
    def __init__(self, redius):
        self.__redius = redius

    def set_redius(self, redius):
        self.__redius = redius

    def get_redius(self):
        return self.__redius

    def area(self):
        return math.pi * self.__redius **2

    def __add__(self, another_circle):
        return Circle(self.__redius + another_circle.__redius)


c1 = Circle(5)
c1.set_redius(4)
print(c1.get_redius())


# # print(c1.get_redius())
# c2 = Circle(5)
# print(c2.get_redius())
# # c3 = c1+c2
# # print(c3.get_redius())
# print(c2.area())
