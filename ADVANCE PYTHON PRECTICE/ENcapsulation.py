class Cust:
    cname ="SBI"
    def __init__(self,cname,cadd,ccno,cbal):
        self.cname=cname
        self.cadd = cadd
        self.ccno = ccno
        self.cbal = cbal
    def deposit(self,damt):
        self.cbal = self.cbal+damt
    def withdraw(self,wamt):
        self.cbal = self.cbal-wamt
    def display(self):
        print(self.cname)
        print(self.cadd)
        print(self.ccno)
        print(self.cbal)
c1 = Cust("Akhilesh","Bihar",1001,2000)
c1.deposit(200)
c1.withdraw(100)
c1.display()
c2=Cust("KISHAN","NEPAL",1002,3000)
c2.deposit(4000)
c2.withdraw(300)
c2.display()

    
        
        
    
