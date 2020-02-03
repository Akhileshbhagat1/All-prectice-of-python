class X:
    def __init__(self):
        print("in constructor of X")
    def __del__(self):
        print("in constructor of X")
x1=X()
print(x1)
x2=x1
print(x3)

