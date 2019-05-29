import pandas as pd 
import numpy as np
'''
s=pd.Series(np.random.randn(5))
print(s)
s1=pd.Series({'x':[10,20,30],'y':[40,50],'z':[60,70]})
print(s1)
s2=pd.Series(5,index=list('abcd'))
print(s2)

df=pd.DataFrame({'a':25,'b':35,'c':45,'d':55},index=[1])
print(df)
df1=pd.DataFrame(['a','b','c','d'],index=[10,20,30,40])
print(df1)
d={'Day':[1,2,3,4,5],
   'Visitors':[63,75,55,57,66],
   'Bounce Rate':[10,11,22,6,33]}
df=pd.DataFrame(d,index=list('abcde'))#required to assign index 
print(df)
print(df['Day'])
l=[{'a':10,'b':20},{'a':30,'b':40,'c':61}]
df1=pd.DataFrame(l,index=['first','second'])#not required to assign index
print(df1)
df1['d']=df1['a']+df1['b']#updating
print(df1)
df2=pd.DataFrame(np.random.randn(6,4),index=list(range(11,17)),columns=list('ABCD'))
print(df2)
print(df2[:3])
print(df2[11:14])
print(df2.loc[[12,14,15],:])
print(df2.loc[[12,14,15],['B','D']])
print(df2.loc[14:,'A':'C'])
print(df2.loc[13]>0)
print(df2.loc[:,df2.loc[13]>0])
print(df2.loc[11,'A'])

print(df2.iloc[:3])
df3=pd.DataFrame(np.random.rand(6,4),index=list(range(1,7)),columns=list(range(0,8,2)))
print(df3.iloc[:3])
print(df3.iloc[1:5,2:4])
print(df3.iloc[[1,3,5],[1,3]])
''''

df3=pd.DataFrame({'AAA':[4,5,6,7],
                  'BBB':[10,20,30,40],
                  'CCC':[100,50,10,-50]})

df3.loc[df3.AAA>=5,'BBB']=-1
print(df3)
