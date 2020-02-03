class Car:
    __max_speed = 0
    __name = ''

    def __init__(self):
        self.__max_speed = 200
        self.__name = 'supercar'

    def drive(self):
        print('driving a car')
        print(self.__max_speed)
        print(self.__name)

    def setspeed(self, speed):
        self.__max_speed = speed
        print('car name is bmw')
        print(self.__max_speed)


c = Car()
c.drive()
# c.setspeed(100)


# class computer:
# 	def __init__(self):
# 		self.__maxprice = 500
# 	def sell(self):
# 		print('selling price is : {}'.format(self.__maxprice))
# 	def setprice(self, price):
# 		self.__maxprice = price
# c = computer()
# c.sell()
# c.setprice(300)
# c.sell()

		

