def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


print(gcdRecur(2, 12)) # = 2

print(gcdRecur(6, 12)) # = 6

print(gcdRecur(9, 12)) # = 3

print(gcdRecur(17, 12)) # = 1

'''
A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.
https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
'''
