'''
You create a collection with it's specific syntax, separating the values with a comma and a space after the comma for style purposes
to help other developers read your code more easily. We can check the type of this value using type().

Python Collections (Arrays)
There are four collection data types in the Python programming language:

Immutable:
Tuples () Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set {} Set is a collection which is unordered and unindexed. No duplicate members.

Mutable:
Lists [] List is a collection which is ordered and changeable. Allows duplicate members.
Dictionary {k:v} Dictionary is a collection which is unordered and changeable. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type.
Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase
in efficiency or security.
'''
list1 = [1, 2, 3, 4]
type(list1)  #<class 'list'>

# We can do the same with tuples:

tuple1 = (1, 2, 3, 4)
type(tuple1)  # <class 'tuple'>

# To access a value contained within a list or tuple, we use an index, exactly like we did with strings:

list1[2]  # 3
tuple1[0] # 1

#We can also extract a portion of the list or tuple using the same logic and notation that we used with string slicing: <list_or_tuple>[start:end:step] and we will obtain a list or tuple as a result (the resulting type, list or tuple, is determined by the original value, if it's a list, the slice will be a list and if it's a tuple, the slice will be a tuple).

list1[1:3]    # [2, 3]
tuple1[::-1]  #(4, 3, 2, 1)
list1[::2]    #[1, 3]

'''
>>> list2 = ["a", "b", "c"]
>>> list2[1] = "e"    # Specify the index and the new value
>>> list2
['a', 'e', 'c']    # The value was updated!
Now, if we try to do this with a tuple, we get an error:

>>> tuple2 = ("a", "b", "c")
>>> tuple2[1] = "e"  # This throws an error
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple2[1] = "e"
TypeError: 'tuple' object does not support item assignment
>>> tuple2
('a', 'b', 'c')  # The value was not changed
👍 Alternative Approach
To replace this value at index 1, we would need to slice the tuple and concatenate the slice with the new value 
contained within a new tuple, like this:

>>> tuple2 = tuple2[:1] + ("e",) + tuple2[2:]
This concatenates three tuples: a tuple that goes from index 0 to index 1 (not inclusive), a new tuple with a single 
element (the new element that we want to include) and a third tuple that goes from index 2 to the end of the tuple. 
The resulting value is a tuple.

>>> tuple2
('a', 'e', 'c')
Note: In this case, we could have concatenated three tuples with the three elements because the tuple was very simple, 
but in a more realistic scenario we could use this slicing technique.

We see that it’s changed. Notice that this is NOT the original tuple, it is a new tuple that we created and then 
assigned to this variable, replacing the old value. Imagine how much time and computations it would take to do this on 
a very large tuple. This is why we use tuples when we know that the data will not change during the program and we use 
lists when it’s possible that the values might change.
'''

# Iterating over lists and tuples is slicing, same as with strings
c  = [(1, 2, 3), "Week 3", 6.453, [[1, 2, 3, 4], 5], 678, [True, False]]

print(c[0]) # 1, 2, 3)
print(c[3:]) # [[[1, 2, 3, 4], 5], 678, [True, False]]
print(c[3][0][2]) # 3
# (Try this and analyze why you get this result, it’s really cool! 😁) Nested list, x3.
print(c[3][1]) # 5
print(c[::-2]) # [[True, False], [[1, 2, 3, 4], 5], 'Week 3']
print(c[:3]) # [(1, 2, 3), 'Week 3', 6.453]
print(c[:1:-2]) # [[True, False], [[1, 2, 3, 4], 5]]


# Operations on collections:

'''
Lists. 

https://docs.python.org/3.9/tutorial/datastructures.html
'''
# Adding things/concatenation:

L1 = [1, 2, 3]
print(L1)
L1.append(4)
print(L1)
# L1.append(5, 6) # Illegal
# L1.extend(7) # Illegal, arg must be iterable
L1.extend([8, 9])
print(L1)
L1.extend({7}) # added set here, legal as iterable
print(L1)
# L2 = L1 + {45, 78} # Illegal, can only concat list.
# L2 = L1 + 45 # Illegal, can only concat list.
L2 = L1 + [45, 78]
print(L2)
print(L1)


# Deleting/Removing things
del(L2[-1]) # static method, not belong to List Obj
print(L2)
L2.pop() # removes last element AND returns it.
print(L2)
L2.remove(1) # removes element of value 1, first one from left if multiples, returns error if not found.
print(L2)

# convert strings to lists and vice versa
L = list('abc')
print(L) # ['a', 'b', 'c']
s = 'I <3 cs'
print(list(s)) # ['I', ' ', '<', '3', ' ', 'c', 's']
print(s.split('<')) # ['I ', '3 cs'] - splits on empty string if blank
print(s.split()) # ['I', '<3', 'cs']
print(''.join(L)) # abc
print(' '.join(L)) # a b c
print(L) # ['a', 'b', 'c']

# sorting and reversing
L = [9, 1, 3, 7]
print(sorted(L)) # sorts [1, 3, 7, 9] but doesn't change L
print(L) # [9, 1, 3, 7]
print(L.sort()) # mutates L. prints None as printing NoneType func call
print(L) # [1, 3, 7, 9]
L.reverse()
print(L) # [9, 7, 3, 1] also mutates L.

# Aliasing and cloning
# Care when binding and creating and so on of mutables. If you only alias e.g. L1 = L2, changing one changes both
# Create a copy with L1 = L2[:] - gives 2 separate objects with copy of contents of the one being cloned.


