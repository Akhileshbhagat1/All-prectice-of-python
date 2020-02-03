from threading import *
from time import sleep

class A(Thread):
	def run(self):
		for i in range(5):
			print('hello')
			sleep(1)

class B(Thread):
	def run(self):
		for i in range(5):
			print('hi')
			sleep(1)

a = A()
b = B()


a.start()
sleep(0.2)
b.start()

a.join()
b.join()
print('bye')

		