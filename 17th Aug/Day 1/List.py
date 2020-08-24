Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ### Lists
>>> a = [] ## empty list
>>> type(a)
<class 'list'>
>>> a = [56,78.5,"Hello",45+6j,True]
>>> a
[56, 78.5, 'Hello', (45+6j), True]
>>> b = [54,76.5,"Hii",5+6j,False]
>>> b
[54, 76.5, 'Hii', (5+6j), False]
>>> a + b
[56, 78.5, 'Hello', (45+6j), True, 54, 76.5, 'Hii', (5+6j), False]
>>> c = a+b
>>> c
[56, 78.5, 'Hello', (45+6j), True, 54, 76.5, 'Hii', (5+6j), False]
>>> c[5]
54
>>> c[:]
[56, 78.5, 'Hello', (45+6j), True, 54, 76.5, 'Hii', (5+6j), False]
>>> c[4:]
[True, 54, 76.5, 'Hii', (5+6j), False]
>>> c[:4]
[56, 78.5, 'Hello', (45+6j)]
>>> len(c)
10
>>> c.append("Umang")
>>> c
[56, 78.5, 'Hello', (45+6j), True, 54, 76.5, 'Hii', (5+6j), False, 'Umang']
>>> c.insert(3,True)
>>> c
[56, 78.5, 'Hello', True, (45+6j), True, 54, 76.5, 'Hii', (5+6j), False, 'Umang']
>>> c.count("Hello")
1
>>> c.count("True")
0
>>> c.count(True)
2
>>> c.count(1)
2
>>> c.count(0)
1
>>> type(c)
<class 'list'>
>>> d = c.copy()
>>> d
[56, 78.5, 'Hello', True, (45+6j), True, 54, 76.5, 'Hii', (5+6j), False, 'Umang']
>>> c.clear()
>>> c
[]
>>> del(c)
>>> c
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> d.remove("Hello")
>>> d
[56, 78.5, True, (45+6j), True, 54, 76.5, 'Hii', (5+6j), False, 'Umang']
>>> e = d.pop(54)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    e = d.pop(54)
IndexError: pop index out of range
>>> e = d.pop(5)
>>> e
54
>>> d
[56, 78.5, True, (45+6j), True, 76.5, 'Hii', (5+6j), False, 'Umang']
>>> f = d.pop()
>>> f
'Umang'
>>> d.index("Hii")
6
>>> g = d.pop(index(76.5))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    g = d.pop(index(76.5))
NameError: name 'index' is not defined
>>> g = d.pop(d.index(76.5))
>>> g
76.5
>>> d
[56, 78.5, True, (45+6j), True, 'Hii', (5+6j), False]
>>> d.index("True")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d.index("True")
ValueError: 'True' is not in list
>>> d.index(True)
2
>>> d.index(True,2)
2
>>> d.index(True,3)
4
>>> ### Sorting of list
>>> a = [243,65,555,89,22,57,10,567,23]
>>> a
[243, 65, 555, 89, 22, 57, 10, 567, 23]
>>> a.sort()
>>> a
[10, 22, 23, 57, 65, 89, 243, 555, 567]
>>> a.sort(reverse=True)
>>> a
[567, 555, 243, 89, 65, 57, 23, 22, 10]
>>> b = ["Umang","A","X","Y","B","P"]
>>> b.sort()
>>> b
['A', 'B', 'P', 'Umang', 'X', 'Y']
>>> b = ["Umang","A",'a',"X","Y","B","P"]
>>> b.sort()
>>> b
['A', 'B', 'P', 'Umang', 'X', 'Y', 'a']
>>> b = ["UMANG","umang"]
>>> b.sort()
>>> b
['UMANG', 'umang']
>>> 