import math
class Circle:
	def __init__(self, radius):
		self.__radius = radius
	def setRadius(self, radius):
		self.__radius = radius
	def getRedius(self):
		return self.__radius
	def area(self):
		return math.pi * self.__radius **2
	def __add__(self, another_circle):
		return Circle(self.__radius + another_circle.__radius)

c1 = Circle(4)
print(c1.getRedius())

c1 = Circle(4)
print(c1.area())

c1 = Circle(4)
print(c1.area())


