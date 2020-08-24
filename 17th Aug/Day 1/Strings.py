Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # String Operations
>>> a = "We are learnig Python right now !!"
>>> len(a)
34
>>> # string slicing
>>> a[:]
'We are learnig Python right now !!'
>>> a
'We are learnig Python right now !!'
>>> print(a)
We are learnig Python right now !!
>>> a[3:]
'are learnig Python right now !!'
>>> a[:8]
'We are l'
>>> a[-6]
'n'
>>> a[-6:]
'now !!'
>>> a.lower()
'we are learnig python right now !!'
>>> a
'We are learnig Python right now !!'
>>> b = a.lower()
>>> b
'we are learnig python right now !!'
>>> a.upper()
'WE ARE LEARNIG PYTHON RIGHT NOW !!'
>>> a.capatilize()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.capatilize()
AttributeError: 'str' object has no attribute 'capatilize'
>>> a.capitalize()
'We are learnig python right now !!'
>>> a
'We are learnig Python right now !!'
>>> a.replace('a','A')
'We Are leArnig Python right now !!'
>>> a.replace(' ','_')
'We_are_learnig_Python_right_now_!!'
>>> a.replace('Python','Data Science')
'We are learnig Data Science right now !!'
>>> a = a.replace('learnig','learning')
>>> a
'We are learning Python right now !!'
>>> a.count('a')
2
>>> a.count("Python")
1
>>> a.count('A')
0
>>> b = "Hekhjhvjfhxnzbdjgfsdmvnfdjkghsdbvfgfdbgdf"
>>> b.count("s")
2
>>> a.count("a", 5,10)
1
>>> 