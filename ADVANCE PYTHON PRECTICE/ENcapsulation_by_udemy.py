class Patient:

   

    def setId(self,id):

       self.__id=id



    def getId(self):

        return self.__id

    def setName(self, name):

        self.__name=name

       

    def getName(self):

        return self.__name

   

    def setSsn(self,ssn):

        self.__ssn=ssn



   

    def getSsn(self):



        return self.__ssn

   

p=Patient()

   

p.setId(456)

p.setName("Bobby")

p.setSsn(15216)

print(p.getId())

print(p.getName())

print(p.getSsn())