# multiple base cases recursive example; fibonnacci.
def fib(n):
    """
    input: any positive input
    return: sum of fib(n-1)+fib(n-2)
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

'''
Results
 fib(1)
1
 fib(0)
1
 fib(2)
2
 fib(3)
3
 fib(4)
5
 fib(5)
8
 fib(6)
13
 fib(7)
21
...
'''
