class Emp:
    ecount=0;
    def __init__(self,ename,eadd,eid,esal):
        self.ename=ename
        self.eadd=eadd
        self.eid=eid
        self.esal=esal
        Emp.ecount=Emp.ecount+1
def __del__(self):
      EMp.ecount = Emp.ecount-1
e1=Emp("AKHILESH","BHOPAL",7777,5000.00)
e2=Emp("KISHAN","BIHAR",7778,4000.00)
e3=Emp("DEEPAK","BIHAR",7779,3000.00)
del e3
print("total no of employee :",Emp.ecount)
  
        
    
