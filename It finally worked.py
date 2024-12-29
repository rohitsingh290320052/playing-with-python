>>> import pandas a pd
SyntaxError: invalid syntax
>>> import pandasas pd
SyntaxError: invalid syntax
>>> import pandas as pd
>>> marks=pd.read_csv("aaa.csv")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    marks=pd.read_csv("aaa.csv")
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\pandas\io\parsers\readers.py", line 586, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\pandas\io\parsers\readers.py", line 482, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\pandas\io\parsers\readers.py", line 811, in __init__
    self._engine = self._make_engine(self.engine)
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\pandas\io\parsers\readers.py", line 1040, in _make_engine
    return mapping[engine](self.f, **self.options)  # type: ignore[call-arg]
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 51, in __init__
    self._open_handles(src, kwds)
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\pandas\io\parsers\base_parser.py", line 222, in _open_handles
    self.handles = get_handle(
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\pandas\io\common.py", line 701, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'aaa.csv'
>>>  marks=pd.read_csv("D:\permssion.csv")
 
SyntaxError: unexpected indent
>>> marks=pd.read_csv("D:\permssion.csv")
>>> marks
      name   number  percent
0       ram     455       70
1  abhishek     112       80
2    sooraj     333       50
>>> 
