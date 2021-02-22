# animals = {}
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

'''
https://docs.python.org/3.9/library/stdtypes.html#typesmapping

https://www.w3schools.com/python/python_ref_dictionary.asp
'''

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        result += len(value)
    return result

print(how_many(animals))
# 6

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    most = 0
    biggest = None
    for k, v in aDict.items():
        if len(v) > most:
            most = len(v)
            biggest = k
    return biggest

print(biggest(animals))
