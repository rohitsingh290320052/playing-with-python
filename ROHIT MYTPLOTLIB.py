Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> taareek=['16-09-2021','17-09-2021','18-09-2021']
>>> taomaan=[28.5,32.4,20.8]
>>> plt.plot(taareek,taomaan)
[<matplotlib.lines.Line2D object at 0x0000021493023E20>]
>>> plt.show()
>>> plt.savefig('graph matplotlib')
>>> 