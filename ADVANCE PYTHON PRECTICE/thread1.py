from threading import Thread
from time import sleep

class My(Thread):
	def  run(self):
		while range(5):
			msg = input('please give a msg')
			print('you entered :: %s ' % msg)

class Your(Thread):
	def run(self):
		while range(5):
			sleep(5)
			print('you said to me :: how are you')

m = My()
y = Your()
m.start()
sleep(0.2)
y.start()
# m.join()
# y.join()
# print('bye')

			
			
		