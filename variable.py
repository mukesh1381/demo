# Declare instance variable
'''
class Test:
    def __init__(self):
        self.a = 10  # instance variable

    def m1(self):
        self.b = 20  # instance variable


t = Test()
t.m1()
t.c = 30  # instance variable
print(t.__dict__)


# Access instance variable

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        print("Within the class")
        print(self.a)
        print(self.b)


t = Test()
t.m1()
print("Outside of the class")
print(t.a)
print(t.b)



# Delete the instance variables

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def m1(self):
        del self.a


t1 = Test()
t2 = Test()
print(t1.__dict__)
print(t2.__dict__)
t1.m1()
del t2.b
t1.c=44
print(t1.__dict__)
print(t2.__dict__)

'''


# Static varibles

class Test():
    a = 10

    def __init__(self):
        self.b = 20


t1 = Test()
t2 = Test()
t3 = Test()
print("t1: ", t1.a, t1.b)
print("t2: ", t2.a, t2.b)
print("t3: ", t3.a, t3.b)
Test.a = 99
t2.b = 45
t3.b = 78
print("t1: ", t1.a, t1.b)
print("t2: ", t2.a, t2.b)
print("t3: ", t3.a, t3.b)
