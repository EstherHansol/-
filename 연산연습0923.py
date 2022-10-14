Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1=3
>>> num2=2/5
>>> letter1='상명대학교'
>>> letter2='서울캠퍼스'
>>> 
>>> num1+num2
3.4
>>> num2-num2
0.0
>>> num1*num2
1.2000000000000002
>>> num1/num2
7.5
>>> letter1+letter2
'상명대학교서울캠퍼스'
>>> letter1-letter2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    letter1-letter2
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> num1-letter2
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    num1-letter2
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> 