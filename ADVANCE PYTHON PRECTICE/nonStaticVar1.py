class X:
    def display(self):
        print(self.a)
        print(self.b)
    def insert(self):
        self.a= 1000
        self.b= 2000

x1=X()
x1.insert()
x1.display()
print(x1.a)
print(x1.b)
