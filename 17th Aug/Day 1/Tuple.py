Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ### Tuple
>>> a = () ## empty tuple
>>> type(a)
<class 'tuple'>
>>> a = (34,56.6,True,5+7j,"Hello")
>>> a
(34, 56.6, True, (5+7j), 'Hello')
>>> a[4]
'Hello'
>>> a[3:5]
((5+7j), 'Hello')
>>> b = (45,56.6,False,5+7j,"Hello")
>>> c = a+b
>>> c
(34, 56.6, True, (5+7j), 'Hello', 45, 56.6, False, (5+7j), 'Hello')
>>> c*2
(34, 56.6, True, (5+7j), 'Hello', 45, 56.6, False, (5+7j), 'Hello', 34, 56.6, True, (5+7j), 'Hello', 45, 56.6, False, (5+7j), 'Hello')
>>> c.index("Hello")
4
>>> len(c)
10
>>> c.count("Hello")
2
>>> del(a)
>>> a
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> e = c.copy()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    e = c.copy()
AttributeError: 'tuple' object has no attribute 'copy'
>>> c.clear()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    c.clear()
AttributeError: 'tuple' object has no attribute 'clear'
>>> c.count()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    c.count()
TypeError: count() takes exactly one argument (0 given)
>>> 