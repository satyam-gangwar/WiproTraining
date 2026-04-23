Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s1='hello'
>>> s1
'hello'
>>> dict1{1:10,2:20,3:30}
SyntaxError: invalid syntax
>>> dict1={1:10,2:20,3:30}
>>> dict1
{1: 10, 2: 20, 3: 30}
>>> dict1[2]
20
>>> dict2={'a':10,'b':20,'c':30}
>>> dict2
{'a': 10, 'b': 20, 'c': 30}
>>> dict2['c']
30
>>> stud={'rno':101,'name':'AAA','city':'BBB'}
>>> stud['name']
'AAA'
>>> stud['name']='XXX'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB'}
>>> stud['fname']='yyy'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB', 'fname': 'yyy'}
>>> stud.get('name)
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> stud.get('name')
...          
'XXX'
>>> stud.keys()
...          
dict_keys(['rno', 'name', 'city', 'fname'])
>>> stud.values()
...          
dict_values([101, 'XXX', 'BBB', 'yyy'])
