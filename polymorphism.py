# # Operator overloading
# def add(a, b):
#     return a * b
#
#
# print(add(10, 30))
# print(add("Durga", 3))
#
#
# # Program to use operator for our class objects
#
# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#
# b1 = Book(10)
# b2 = Book(20)
#
#
# # print(b1 + b2)
# # print(b1*b2)
#
#
# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         return self.pages + other.pages
#
#     def __mul__(self, other):
#         return self.pages * other.pages
#
#
# b1 = Book(10)
# b2 = Book(20)
# print(b1 + b2)
# print(b1 * b2)


class Employee:
    def __int__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class Timesheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


e = Employee()
t = Timesheet('Durga', 25)
print("This month salary is:", e * t)
