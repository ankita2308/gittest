def outer(x):
    return x+1
s=outer(3)
print(s)

del outer
print(s)
print(outer(3))
