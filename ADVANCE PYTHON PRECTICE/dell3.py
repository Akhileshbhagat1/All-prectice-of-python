class X:
    def __init__(self):
        print("in constructor of x")
    def __del__(self):
        print("in destructor of X")
p= [X(),X(),X()]
del p[2]
del p
