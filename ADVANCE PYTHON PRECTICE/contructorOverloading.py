class X:
    def __init__(self):
        print("in const of x")
class Y(X):
    def __init__(self):
        print("in const of y")
y1=Y()
x1=X()
