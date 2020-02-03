class Dog:
    def sound(self):
        print('bow bow')


class Cat:
    def sound(self):
        print('mewu')


def animal(animaltype):
    animaltype.sound()


d = Dog()
c = Cat()
animal(c)
animal(d)

# class parrot:
# 	def fly(self):
# 		print('can fly')

# class horse:
# 	def fly(self):
# 		print('can not fly')

# def typeof(animal):
# 	animal.fly()

# p = parrot()
# h = horse()

# typeof(p)
# typeof(h)
