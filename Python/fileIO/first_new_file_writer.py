# Creates a filehandler with a writable file named 'kids', opens it.
# Loops through it asking for input, writes the input and newlines each time.
# Closes file.
# Saves it in place where you are; TODO - how save to particular path?
nameHandle = open('kids', 'w')
for i in range(2):
    name = input("Enter a name: ")
    nameHandle.write(name + '\n')
nameHandle.close()

# To read it:
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()
'''
output:
Joe

Steve

'''
# Odd that it has lines afterwards... Doesn't show when opening the file.
# TODO - experiment. The stripping of '\n' gives all on one line no spaces.
