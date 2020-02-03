class Cust:
    """Customer App"""
    cbname = "SBI"
    def __init__(self,cname,cadd,ccno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.ccno=ccno
        self.cbal=cbal
    def __str__(self):
        
        return (self.cname+" "+self.cadd+" "+str(self.ccno)+" "+str(self.cbal)+" "+Cust.cbname)
                
    def deposit(self,damt):
               self.cbal=self.bal+damt
    def withdraw(self,wamt):
                self.cbal=self.bal-wamt
    def display (self):
                print(self.cname)
                print(self.cadd)
                print(self.ccno)
                print(self.cbal)

c1=Cust("akhilesh","bpl",1001,10000.00)
c2=Cust("Kishan","nepal",10002,3000.00)
c3=Cust("Anand","patna",1003,5000.00)
X=[c1,c2,c3]
print("Before Sorting")
for p in X:
                print(p)
X.sort(key=lambda c:c.cbal, reverse=True)
print("Aftter Sorting")
for q in X:
     print(q)
        
