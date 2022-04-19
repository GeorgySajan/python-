Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#factorial
num=int(input("enter a number"))
enter a numberfact=1
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    num=int(input("enter a number"))
ValueError: invalid literal for int() with base 10: 'fact=1'
if num==0:
   print("factorial of",num,"is",fact)
   for i in range(1,num+1):
    fact=fact*i
    print("factorial of",num,"is",fact)