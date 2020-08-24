Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## Dictionary (Key - Value Pairs)
>>> a = {}  ## empty dict
>>> type(a)
<class 'dict'>
>>> a = {"Fruit":"Apple","Mobile":"Android","Sweets":"Jalebi"}
>>> a
{'Fruit': 'Apple', 'Mobile': 'Android', 'Sweets': 'Jalebi'}
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[1]
KeyError: 1
>>> a = {"Fruit":"Apple","Mobile":"Android","Fruit":"Jalebi"}
>>> a
{'Fruit': 'Jalebi', 'Mobile': 'Android'}
>>> a['Mobile']
'Android'
>>> a.keys()
dict_keys(['Fruit', 'Mobile'])
>>> a.values()
dict_values(['Jalebi', 'Android'])
>>> a.items()
dict_items([('Fruit', 'Jalebi'), ('Mobile', 'Android')])
>>> a['Veg'] = "Potato"
>>> a
{'Fruit': 'Jalebi', 'Mobile': 'Android', 'Veg': 'Potato'}
>>> a['Veg'] = "Tomato"
>>> a
{'Fruit': 'Jalebi', 'Mobile': 'Android', 'Veg': 'Tomato'}
>>> a['veg'] = "Tomato"
>>> a
{'Fruit': 'Jalebi', 'Mobile': 'Android', 'Veg': 'Tomato', 'veg': 'Tomato'}
>>> del(a['veg'])
>>> a
{'Fruit': 'Jalebi', 'Mobile': 'Android', 'Veg': 'Tomato'}
>>> b = a.pop('Mobile')
>>> b
'Android'
>>> a
{'Fruit': 'Jalebi', 'Veg': 'Tomato'}
>>> 