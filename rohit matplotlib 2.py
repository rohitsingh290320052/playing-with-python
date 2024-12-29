Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> import pandas as pd
>>> df=pd.DataFrame({'age':[12,14,16,18].'weight':[40,46,50,56]})
SyntaxError: invalid syntax
>>> df=pd.DataFrame({'age':[12,14,16,18],'weight':[40,46,50,56]})
>>> df
   age  weight
0   12      40
1   14      46
2   16      50
3   18      56
>>> plt.xlabel('age in years')
Text(0.5, 0, 'age in years')
>>> plt.ylsables('weioght in kilogrames')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    plt.ylsables('weioght in kilogrames')
AttributeError: module 'matplotlib.pyplot' has no attribute 'ylsables'
>>> plt.ylables('weioght in kilogrames')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    plt.ylables('weioght in kilogrames')
AttributeError: module 'matplotlib.pyplot' has no attribute 'ylables'
>>> plt.ylable('weioght in kilogrames')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    plt.ylable('weioght in kilogrames')
AttributeError: module 'matplotlib.pyplot' has no attribute 'ylable'
>>> plt.ylabel('weioght in kilogrames')
Text(0, 0.5, 'weioght in kilogrames')
>>> plt.title('age ke anusaar weight')
Text(0.5, 1.0, 'age ke anusaar weight')
>>> plt.plot(df.age,df.weight,marker='+',markerseze=5,color='blue',linewidth=3,linestyle='dotted')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    plt.plot(df.age,df.weight,marker='+',markerseze=5,color='blue',linewidth=3,linestyle='dotted')
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\pyplot.py", line 3019, in plot
    return gca().plot(
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\axes\_axes.py", line 1605, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\axes\_base.py", line 315, in __call__
    yield from self._plot_args(this, kwargs)
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\axes\_base.py", line 539, in _plot_args
    return [l[0] for l in result]
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\axes\_base.py", line 539, in <listcomp>
    return [l[0] for l in result]
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\axes\_base.py", line 532, in <genexpr>
    result = (make_artist(x[:, j % ncx], y[:, j % ncy], kw,
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\axes\_base.py", line 354, in _makeline
    seg = mlines.Line2D(x, y, **kw)
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\lines.py", line 397, in __init__
    self.update(kwargs)
  File "C:\Users\Pradeep Kumar\Desktop\ROHIT IP\ROHIT SINGH\lib\site-packages\matplotlib\artist.py", line 1062, in update
    raise AttributeError(f"{type(self).__name__!r} object "
AttributeError: 'Line2D' object has no property 'markerseze'
>>> plt.plot(df.age,df.weight,marker='+',markersize=5,color='blue',linewidth=3,linestyle='dotted')
[<matplotlib.lines.Line2D object at 0x000002C967012370>]
>>> plt.show()
>>> plt.show()
>>> plt.show()
>>> plt.plot(df.age,df.weight,marker='+',markersize=5,color='blue',linewidth=3,linestyle='dotted')
[<matplotlib.lines.Line2D object at 0x000002C964946E20>]
>>> plt.show()
>>> df.plot()
<AxesSubplot:>
>>> plt.show()
>>> plt.show()
>>> 
KeyboardInterrupt
>>> df.plot()
<AxesSubplot:>
>>> plt.show()
>>> 