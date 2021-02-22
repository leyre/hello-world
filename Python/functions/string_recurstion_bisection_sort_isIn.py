# string recursion with bisection sort
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr
    else:
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[:len(aStr)//2])
        else:
            return isIn(char, aStr[len(aStr)//2:])

print(isIn('a', 'bc'))
# False
print(isIn('a', 'abc'))
# True
print(isIn('d', 'abcdef'))
# True
print(isIn('c', 'abcdef'))
# True
print(isIn('c', 'abcde'))
# True
