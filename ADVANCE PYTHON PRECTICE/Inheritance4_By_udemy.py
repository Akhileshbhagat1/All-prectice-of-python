# how to use super within the inheritance
class BMW:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def start(self):
		print("starting the car")

	

class Threeserise(BMW):
	def __init__(self, price, make, model, year):
		super().__init__( make, model, year)
		self.price = price

	def start(self):
		print("overriding this method", self.price)

class Fiveseries(BMW):
	def __init__(self, color, make, model, year):
		super().__init__( make, model, year)
		self.color = color

three = Threeserise(1250000, 'ironSteel', 'Q5', 2019)
print(three.price)
print(three.make)
print(three.model)
print(three.year)

three.start()

five = Fiveseries('red', 'ironfiber', 'Q7', 2019)
print(five.color)
print(five.make)
print(five.model)
print(five.year)


