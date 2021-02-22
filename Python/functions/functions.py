"""
Info on functions
"""
# access docstring info with  `functionName.__doc__` note the double underscores like init func

# you can return multiple values from a func with a tuple or other collection like a list
# you can assign these to multiple variables in one line by comma separating variable names
# types will be of elements from collection rather than collection type

def returnTuple(a, b, c):
    return (a, b, c)

var1, var2, var3 = returnTuple("3", 2, True)

print(var1, type(var1), var2, type(var2), var3, type(var3)) # 3 <class 'str'> 2 <class 'int'> True <class 'bool'>



# you can create a tuple from individual params in a function by adding asterisk; looks like you only need 1 param name then.
def returnArgsAsTuple (*inputTuple):
    print(inputTuple)
    print(type(inputTuple[0]))

returnArgsAsTuple(1, 2, 3, 4, 5)        # (1, 2, 3, 4, 5, 6)
                                        # <class 'int'>
returnArgsAsTuple(1, 2, 'four', 4, 5)   # 1, 2, 'four', 4, 5)
                                        # <class 'int'>
returnArgsAsTuple(1)                    # (1,)
                                        # <class 'int'>

# Default params, just bind the formal param to the default value in the def to default it:
def name_orderer(first_name, last_name, reverse = True):
    '''
    :param first_name: any string, intended to be a forename
    :param last_name: any string, intended to be a last name
    :param reverse: optional; boolean, defaults to True. Use to specify print format of full name.
    :return: None, prints out first_name and last_name in order specified by reverse parameter.
    '''
    if reverse:
        print(last_name, end=', ') # this is way to get print to run to same line, end param default = '\n' overwrite.
        print(first_name)
    else:
        print(first_name, last_name)
name_orderer('lisa', 'eyre')
# prints: eyre, lisa
"""
Fun with scopes
"""
def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z() # if you remove the () it returns the func location and name, if you put () in the func call line 17 it calls a before c
               # in order as is it calls c print func and then runs func a and you see a then c.
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))

'''
Building on functions
'''
def square(x):
    '''
    x: int or float.
    :return int or float of x raised to the power 2 (multiplied by itself twice eg square(2) = 4)
    '''
    return x**2

def fourthPower(x):
    '''
    x: int or float.
    requires square(x) above.
    :return int or float of x raised to the power 4 (multiplied by itself four times eg fourthPower(4) = 256)
    '''
    return square(square(x))
