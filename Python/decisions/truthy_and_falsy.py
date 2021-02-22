#More on truthy and falsy.

"""
Python doc on same: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

Truthy and falsy can be applied to strings and ints.to
## Falsy:
number of 0
empty string e.g. '' or ""

## Truthy:
number that is not 0 (literally any other number than 0)
and string with a length > 0 (literally anything that is not an empty string)

"""
# None is a falsy value.
if None:
  print("None is a Truthy value")
else:
  print("None is a Falsy value")

# None is a Falsy value

# String
if '123':
  print('123 is Truthy')
else:
  print('123 is Falsy')

# 123 is Truthy

# Number
if 123:
  print('123 is Truthy')
else:
  print('123 is Falsy')

# 123 is Truthy

num = 5
while num: # Note this line is taking advantage of truthy val
    if num > 10: # dont need this, it would catch going other way
      break
    print('Hi', num)
    num -= 1 # when this gets to 0 the while loop stops as 0 is falsy

#Hi 5
#Hi 4
#Hi 3
#Hi 2
#Hi 1
