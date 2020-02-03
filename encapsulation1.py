class car:
    __maxspeed = 0
    __name = ''

    def __init__(self):
        self.__maxspeed = 200
        self.__name = 'supercar'

    def drive(self):
        print('driving a car')
        print(self.__maxspeed)

    def setspeed(self, speed):
        self.__maxspeed = speed
        print('car name is bmw')
        print(self.__maxspeed)


c = car()
c.drive()
c.setspeed(100)
