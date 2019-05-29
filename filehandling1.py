f1=open('data.txt')
f2=open('data1.txt','w')
for i in f1.readlines():
    f2.write(i)
f2.close()
    

        

