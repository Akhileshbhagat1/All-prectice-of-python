class Test:
	def __init__(self, msg):
		self.msg = msg
	def __add__(self, other):
		return self.msg + other.msg

t1 = Test('pyhton')
t2 = Test('world')
p = t1 + t2
print(p)