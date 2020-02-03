class A:
	def __init__(self):
		print('instance of A')
	def m1(self):
		print('it is m1')

class B(A):
	def __init__(self):
		super().__init__()
		print('instance of B')
	def m2(self):
		print('it is m2')


b = B()
b.m2()

