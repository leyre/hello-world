"""
Useful:
"""
https://realpython.com/python-enumerate/
# use enumerate(iterable) rather than range or whatever, where you need an index and a value.
# index starts at 0 like all usual, but you can override with start (see below, for human friendly index if desired.)
# syntax:
def enumerated_func(iterable):
  for counter, value in enumerate(iterable, start=1):
    print('counter is:', counter, 'value is: ', value)

"""
 enumerated_func('whoopee')
counter is: 1 value is:  w
counter is: 2 value is:  h
counter is: 3 value is:  o
counter is: 4 value is:  o
counter is: 5 value is:  p
counter is: 6 value is:  e
counter is: 7 value is:  e
"""

"""
Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you.
So, for example, if we define end to be 6, your code should print out the result:
21
which is 1 + 2 + 3 + 4 + 5 + 6.
"""
end = int(input("Please enter a  number: "))

i = 1
total = 0
while i <= end:
    total += i
    i += 1
print(total)

# Here is one of a few ways to solve this problem:
total = 0
for next in range(1, end+1):
    total += next
print(total)

# Here is another (elegant!):
total = end
for next in range(end):
    total += next
print(total)

# e.g. stepping backwards
print('Hello!')
for i in range(10, 1, -2):
  print(i)

# Problem set 1 problem 1: vowel checker
s = 'azcbobobegghakla'
totalVowels = 0
for char in s:
    if char in ('aeiou'):
        totalVowels += 1
print('Number of vowels:', totalVowels)

# Problem set 1 problem 2: bob checker
s = 'azcegghaklbobob'
"""
#num_bobs = s.count('bob') - doesn't work as it can't handle bobob etc.

# This doesn't work as this for is using the value and not the index
num_bobs = 0
for char in s:
  if char == 'b':
    if s[char:char+3] == 'bob':
      num_bobs += 1
"""
num_bobs = 0
for index in range(len(s)):
    if index < len(s) and s[index:index+3] == 'bob':
        num_bobs += 1
print('Number of times bob occurs is:', num_bobs)

"""
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

# pseudocode
loop through a string 
check in char is less than next char
 if true add to charstring
 if false don't add to charstring
   check if currentlongest >= charstring
     if true do nothing
     if false charstring = currentlongest
"""
s = 'azcbobobegghakl'
# s = 'abcbcd'

# Work in progress:
charstring = ""
longeststring = ""
counter = 0
for char in s:
    if counter == len(s)-1:
        break
    elif char <= s[counter+1]:
        charstring += char
    else:
        if char >= s[counter-1]:
            charstring += char
        if len(longeststring) < len(charstring):
            longeststring = charstring
            charstring = ""
    counter += 1
    print("char is", char)
    print("counter is", counter)
    print("charstring is", charstring)
    print("longeststring is", longeststring)
print("Longest substring in alphabetical order is:", longeststring)

'''
# This works, from previous attempt.
tempSubset = ''
longestSubset = ''
for char in range(len(s)):
    if (len(s) - 1) == char:
        if len(tempSubset) > len(longestSubset):
            longestSubset = tempSubset
            break
        else:
            break
    elif s[char] <= s[char+1]:
        if tempSubset == '':
            tempSubset = s[char] + s[char+1]
        else:
            tempSubset += s[char+1]
    else:
        if tempSubset == '':
            tempSubset = s[char]
        if len(tempSubset) > len(longestSubset):
            longestSubset = tempSubset
        tempSubset = ''
print('Longest substring in alphabetical order is:', longestSubset)

# This is Ian's solution; elegant!
count = 0
maxCount = 0
result = 0
for index in range(len(s)-1):
  if s[index] <= s[index+1]:
    count += 1
    if count > maxCount:
      maxCount = count
      result = index+1
  else:
    count = 0
longest = s[result-maxCount:result+1]
print ("Longest substring in alphabetical order is:", longest)
'''
