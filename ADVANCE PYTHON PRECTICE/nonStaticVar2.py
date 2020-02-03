class X:
    def insert(self):
        self.a= 1000
        self.b= 2000
    def modify(self):
        self.a=self.a+100
        self.b=self.b-100
    def display(self):
        print(self.a)
        print(self.b)

x1= X()
x1.insert()
x1.display()
x1.modify()
x1.display()

x2= X()
x2.insert()
x2.display()
x2.modify()
x2.display()
