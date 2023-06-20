def f1():
    yield 123
    yield "Sai"
    yield "Bangalore"
    yield 3000
g = f1()

print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))