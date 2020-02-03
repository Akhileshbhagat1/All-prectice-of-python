class X:
    def __init__(self):
        self.a = 1000
        self.b = 2000
class Y(X):
    def __init__(self):
        super().__init__()
        self.c=3000
        self.d = 4000
y1=Y()
print(y1.a)
print(y1.b)
print(y1.c)
print(y1.d)
