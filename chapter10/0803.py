# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# 8.3 重塑和轴向旋转


df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                    'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())



means =  df['data1'].groupby([df['key1'],df['key2']]).mean()
print(means)


df.groupby(df['key1']).mean()
df.groupby([df['key1'],df['key2']]).mean()



for name, group in df.groupby('key1'):
    
    print(name)
    print(group)

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)
































