Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
vovels=pd.Series([
>>> vovels=pd.Series([0,0,0,0,0] , index=['a','b','c','d','e'])
>>> vovels
a    0
b    0
c    0
d    0
e    0
dtype: int64
>>> vovels[:]=10
>>> vovels
a    10
b    10
c    10
d    10
e    10
dtype: int64
>>> vovels[0:5]=50
>>> vovels
a    50
b    50
c    50
d    50
e    50
dtype: int64
>>> vovels['c']=0
>>> vovels
a    50
b    50
c     0
d    50
e    50
dtype: int64
>>> vovels=vovels/2
>>> vovels
a    25.0
b    25.0
c     0.0
d    25.0
e    25.0
dtype: float64
>>> vovels[2]=vovels[3]/2
>>> vovels
a    25.0
b    25.0
c    12.5
d    25.0
e    25.0
dtype: float64
>>> 