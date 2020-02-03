class X:
    def __init__(self):
        print("AKHILESH")
    def m1(self):
        print("m1 method")
    def __del__(self):
        print("in destructor")
x1=X()
x1.m1()
x1=X()
x1.m1()
