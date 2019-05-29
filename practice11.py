'''
l=[['f','a','c'],
   ['o','b','q'],
   ['a','n','o']]
l1=[]
def concat(strg):
    for i in range(len(strg)):
        s=''
        for j in range(len(strg[i])):
            s=s+strg[j][i]
        l1.append(s)
    return l1
print(concat(l))
'''
s='The quick brown fox jumps over a lazy dog'
'''u=0
l=0
w=0
d=0
for i in s:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
    elif i.isdigit():
        d=d+1
    elif i.isspace():
        w=w+1
    else:
        print(i)
print(u,l,d,w)
'''
s1=s.split()
print(s1)
s2=s1[::-1]
print(s2)
s3=''.join(s2)
print(s1)
print(s[::-1])
for i in range(len(s1)):
    s1[i]=s[i][::-1]
s4=''.join(s1)
print(s4)

#L='The quick brown fox jumps over a lazy dog'
'''L1=''
for i in L:
    if i=='':
        continue
    elif i not in L1:
        L1+=i
    else:
        print(i)
        print('Reoccured string is:')'''
'''c=0
for i in L:
    if L.count(i)>c and i!='':
        c=L.count(i)
        s1=i
print('max occurance for',s1,'is',c)'''

'''L=[['a','b','c'],
   ['d','e','f'],
   ['g','h','i']]
L1=[]
for i in range(len(L)):
    s=''
    for j in range(3):
        s=s+L[j][i]
        L1.append(s)
    print(L1)
'''

'''def is_isogram(strg):
    for i in strg.lower():
        if strg.count(i)<1:
            print('string is not isogramstring')
            break
        return('string is isogramstring')
#print(is_isogram('python'))
print(is_isogram('PYTHON'))'''


'''s1='abcdefghijklmnopqrstuvwxyz'
s='The quick brown fox jumps over a lazy dog'
flag=True
for i in s1:
    if i not in s:
        flag=False
if flag==True:
    print('string in anagramstring')
else:
    print('string in not anagramstring')'''








    
    


        
 
        







