def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

n=6
f=1
for a in range(1,n+1):
    f=f*a
print(f)
