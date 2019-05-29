import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

'''df3=pd.DataFrame({'AAA':[4,5,6,7],
                  'BBB':[10,20,30,40],
                  'CCC':[100,50,10,-50]})

#df3.loc[df3.AAA>=5,'BBB']=-1
#df3.loc[df3.AAA>=5,'BBB','CCC']=555
df3['logic']=np.where(df3['AAA']>5,'High','Low')
print(df3)
'''

df=pd.read_csv('ign.csv')
'''
#print(df.head())
#print(df.tail())
#print(df.shape)
#print(df.iloc[:10,:])
#print(df.iloc[:,2:])
#print(df.iloc[:,2:6])
#print(df.loc[:5,['score','release_year']])

#print(df[['score','release_year']])       
score_filter=df['score']>7
#print(score_filter)
filtered=df[score_filter]
#print(filtered)
xbox_one_filter=(df['score']>7)&(df['platform']=="Xbox One")
filtered_review=df[xbox_one_filter]
print(filtered_review)
'''
df[df['platform']=='Xbox One']['score'].plot(kind='hist')
plt.show()


