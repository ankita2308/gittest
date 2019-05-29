import pickle
f=open("data.txt",'wb')
d={'id':1,'name':'abc'}
p=pickle.dump(d,f)
print(p)
f.close()
f1=open("data.txt",'rb')
p1=pickle.load(f1)
print(p1)
f1.close()
