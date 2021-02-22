def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x % 2 == 1
    #return bool(x % 2) # less efficient than above opt.
    # return x % 2 # truthy vs falsy - wrong, returns int!
