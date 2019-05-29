def outer(x):
    def inner(m):
        return m*x
    return inner
obj=outer(8)
print(type(obj))
print(obj(5))
