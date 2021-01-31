# Got this from https://realpython.com/lessons/python-none-overview/
#               https://realpython.com/lessons/none-how-to-test/
# Todo1 - replace this comment header with proper python comment when remember how :)

"""
 Null doesn't exist in Python, but is similar to Python None. Don't assume it is the same though!

The Null and None types have diff specificities.

In python you don't have None type variables to start, because it's so spare you only create vars by assignment.

Testing for None in python:
"""

y
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'y' is not defined
y = 1
y
# 1
print(print("hi"))
# hi
# None
y = None
y
#
print(y)
# None
type(y)
# <class 'NoneType'>
type(print())
#
#<class 'NoneType'>


# import regular expressions module
import re

# use re to check for matching string with identity operator 'is' to demonstrate return is None.
match = re.match(r"goodbye", "hello")
if match is None:
  print("No match")

# Note identity operator 'is' is different to equality operator '==', '==' checks the value, 'is' checks instance.
# Also notice there is only one None instance in Python - all None types point to the same object (it is a constant
# which you can tell because it is capitalised, 'None'):
x = [1]
y = [1]
x == y # True
x is y # False
x = None
y = None
x == y # True
x is y # True
id(x)
# 140692271398080 (replit ref, may differ in other shells? Differed to vid e.g. 4361750632)
id(y)
# 140692271398080 (replit ref, may differ in other shells? Differed to vid e.g. 4361750632)

"""
You can assign None to things, but you can’t assign anything to it, and you can’t subclass from it.

It is an object, (it’s a full citizen of Python) but has particularities.
Key things to remember:
 1. None is the return value of functions that don’t have a return value,
 2. It’s an object, a constant, and a singleton.
 3. This last one, None being a singleton, is particularly important because it means that if you want to check
    if something is None, you should use the 'is' keyword and not simply the equality operator.

None is falsy, so if you’re using it in decision structures or anything like that, you can often assume that it will
behave the way False does. But if you want to be absolutely sure that something is None, then you do need to use the
is keyword.
"""