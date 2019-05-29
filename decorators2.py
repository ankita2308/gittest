def outer(x):
    def inner(a,b,c):
        return (a*x**2+b*x+c)
    return inner
p=outer(3)
print(p(4,-2,5))
