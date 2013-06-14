# Exercise 13; Parameters, Unpacking Variables

from sys import argv

x = raw_input('How many input parameters? ')

script, first, second, third = argv

print "The script is called:", script
print "Your first variables is:", first
print "Your second variables is:", second
print "Your third variable is:", third
print "There are 4 input parameters, you guessed %r" % int(x)
