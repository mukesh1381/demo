'''
class Student:
    def __init__(self, ID, name, age):
        self.Id = ID
        self.sname = name
        self.age = age

    def display(self):
        print("Student id is :", self.Id)
        print("Student name is :", self.sname)
        print("Student age is :", self.age)


s = Student(101, "John", "634")
s1 = Student(102, "Wick", "635")
s.display()
s1.display()



class Student:
    """This is student class for display
student display"""


s = Student()
print(s.__doc__)


class Student:
    def getdata(self):
        self.sid = int(input("Enter the ID: "))
        self.sname = input("Enter the name: ")
        self.saddress = input("Enter the address: ")

    def display(self):
        print("Student ID is :", self.sid)
        print("Student name is :", self.sname)
        print("Student address is :", self.saddress)


s = Student()
s.getdata()
s.display()




class Student:
    def __init__(self, x, y, z):
        self.sid = x
        self.sname = y
        self.saddress = z


s1 = Student(101, "Ahmed", "Pakistan")
s2 = Student(101,'Raman',"Naynital")
print(s1.__slots__)
print(s2.__dict__)

'''


class Student:
    """This is Student class for display
    student display"""


s = Student()
print(s.__doc__)
print(s.__dict__)
