def f1():
    yield 124
    yield "Sai"
    yield "Bangalore"
    yield 3000
g = f1()

print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
