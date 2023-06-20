class A:
    def f1(self):
        print("F1 function of class A")


class B:
    def f1(self):
        print("F1 function of class B")


class C(A, B):
    def f3(self):
        B.f1(self)  # through this method we can access B class function
        print("F3 function of class C")


# c = C()
# c.f1()
# c.f3()

class D(C):
    def f4(self):
        print("F4 function of class D")


class E(C):
    def f5(self):
        print("F5 function of class E")


e = E()
e.f1()
e.f3()
e.f5()

d = D()
d.f1()
d.f3()
d.f4()
