class Student:
    clg = "Durgasoft"

    def __init__(self, rno, name):
        self.rollno = rno
        self.name = name

    def display(self):
        print('method exicution ..')
        print('Rollno is  ..', self.rollno)
        print('name is ..', self.name)

    @classmethod
    def getCollege(self):
        print('college name : ', self.clg)

    @staticmethod
    def findAverage(x, y):
        print("Average :", (x+y)/2)


s = Student(101, "ram")
# print(Student.clg)
# s.display()
# Student.getCollege()
s.findAverage(10, 20)



