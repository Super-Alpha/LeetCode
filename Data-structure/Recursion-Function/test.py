# Time：2020/3/3017:21
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
obj=pd.Series([6,2,-2,0],index=["小明","小王","小强","小红"])
data={'name':[' Diego','Anna','Eugene '],'gender':['M','F','M'],'age':[12,23,34]}
df=pd.DataFrame(data)

df1=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','c','d'],columns=['one','two','four'])
a=df1.reindex(index=["a","b","c","d"],columns=["one","two","three","four"],fill_value="NaN")

d=pd.DataFrame(np.arange(12).reshape(3,4))
plt.plot(d)
plt.show()"""

str = ["flower","low","lowight"]
prefix_len = []
for num, s in enumerate(zip(*str)):
    if len(set(s)) == 1:
        prefix_len.append(num)
    else:
        break
print(str[0][:len(prefix_len)] if prefix_len else "")