# Exercise 15: Reading FIles

# load argv module
from sys import argv

# unpack parameters (2)
script, filename = argv

# open a file and create an object of type file
txt = open(filename)

# print contents of filename using file object method read()
print "Here's your file %r:" % filename
print txt.read()

# get a new file handle 
print "Type the filename again:"
file_again = raw_input('> ')

txt_again = open(file_again)
# print its contents with formatting and special characters
print txt_again.read()
