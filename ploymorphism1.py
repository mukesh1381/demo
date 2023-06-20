# Method overloading
class Test:
    def m1(self):
        print("No arg method")

    def m1(self, a):
        print('One arg method')

    def m1(self, a, b):
        print("Two arg method")


t = Test()


# t.m1()
# t.m1(10)
# t.m1(10,20)

# ***************************

class Test:
    def __init__(self):
        print("No arg method")

    def __init__(self, a):
        print('One arg method')

    def __init__(self, a, b):
        print("Two arg method")


# t.m1()
# t.m1(10)
# t.m1(10, 20)


# Method overriding

class Parent:
    def propert(self):
        print("Cash+Gold+Lands")

    def car(self):
        print("Alto car")


class Child(Parent):
    def car(self):
#        super().car()
        print("Benz car")


c = Child()
c.propert()
c.car()


# Constructor overriding
class Parent:
    def __init__(self):
        print('Parent class constructor')


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class Constructor")


#C = Child()
