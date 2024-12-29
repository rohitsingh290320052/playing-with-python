Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy
>>> rsheet=
SyntaxError: invalid syntax
>>> 


>>> rsheet={'saloni':pd.Series([100,200,400,500] , index=['ip','english','maths','eco']) , 'kshma':pd.Series([250,100,30,50] , index=['english','eco','hindi','physics'])}
>>> rsheet
{'saloni': ip         100
english    200
maths      400
eco        500
dtype: int64, 'kshma': english    250
eco        100
hindi       30
physics     50
dtype: int64}
>>> ram ram=pd.DataFrame(rsheet)
SyntaxError: invalid syntax
>>> ram=pd.DataFrame(rsheet)
>>> ram
         saloni  kshma
eco       500.0  100.0
english   200.0  250.0
hindi       NaN   30.0
ip        100.0    NaN
maths     400.0    NaN
physics     NaN   50.0
>>> ram['arjun']=[10,20.30.40.50.60]
SyntaxError: invalid syntax
>>>  ram['arjun']=[10,20,30,40,50,60]
 
SyntaxError: unexpected indent
>>> ram['arjun']=[10,20,30,40,50,60]
>>> ram
         saloni  kshma  arjun
eco       500.0  100.0     10
english   200.0  250.0     20
hindi       NaN   30.0     30
ip        100.0    NaN     40
maths     400.0    NaN     50
physics     NaN   50.0     60
>>> ram.loc['arts']=[50,40,30]
>>> ram
         saloni  kshma  arjun
eco       500.0  100.0     10
english   200.0  250.0     20
hindi       NaN   30.0     30
ip        100.0    NaN     40
maths     400.0    NaN     50
physics     NaN   50.0     60
arts       50.0   40.0     30
>>> 