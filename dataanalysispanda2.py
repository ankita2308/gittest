import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

rng=pd.date_range('1/1/2017',periods=100,freq='D')
print(rng)
data=np.random.randn(100,4)
cols=list("ABCD")
df1=pd.DataFrame(data,rng,cols)
df2=pd.DataFrame(data,rng,cols)
df3=pd.DataFrame(data,rng,cols)
pf=pd.Panel({'df1':df1,'df2':df2,'df3':df3})
print(pf)

