def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    sml = 0
    if a <= b:
        sml = a
    else:
        sml = b
    while sml > 0:
        if a%sml == 0 and b%sml == 0:
            break
        else:
            sml-=1
    return sml


print(gcdIter(2, 12)) # = 2

print(gcdIter(6, 12)) # = 6

print(gcdIter(9, 12)) # = 3

print(gcdIter(17, 12)) # = 1
