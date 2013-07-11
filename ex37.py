# Keywords Review #2
#
# Most explanations came form PyDoc but some came from http://zetcode.com/lang/python/keywords/ as well.

# and
# a boolean operator that evaluates to True is both LHS and RHS are True
print "True and True == True? %r" % (True and True)
print "True and False == False? %r" % (True and False)

# del
# deletes a variable from the namespace
name = "exists"
print "before del"
if 'name' in locals():
	print "name exists"
else:
	print "name does not exist"
del name
print "after del"
if 'name' in locals():
	print "name exists"
else:
	print "name does not exist"

# from
# import _from_ a module
from sys import argv

# not
# boolean operator to negate
print "True is %r" % True
print "not(True) is %r" % (not(True))
print "False is %r" % False
print "not(False) is %r" % (not(False))

# while
# a loop that evaluates the statements within if the statement is True
while_loop = True
while_loop_count = 0
print "Will loop 10 times until loop count is 10 or user says cancel."
while while_loop:
	if while_loop_count < 10:
		while_loop_prompt = "Loop #%d Contunue? [Y/n] " % (while_loop_count + 1)
		while_loop_input = raw_input(while_loop_prompt)
		if while_loop_input == 'n':
			while_loop = False
	else:
		while_loop = False
	while_loop_count += 1

if while_loop_count == 1:
	print "Looped 1 time."
else:
	print "Looped %d times." % while_loop_count 

# as 
# defines an alias for an imported module
import random as rnd
print "rnd.randint(1, 10) = %r" % rnd.randint(1,10)

# elif
# multiple if-statement

# global
# required in order to modify variables outside of a function
x = 10
def test_no_global():
#	global x
	x = 0
	print "inside: x = %r" % x
print "Without \"global\""
test_no_global()
def test_global():
	global x
	x = 0
	print "inside: x = %r" % x
print "outside: x = %r" % x
print "With \"global\""
test_global()
print "outside: x = %r" % x

# or
# boolean operator that evaluates to true if either LHS or RHS is True
print "True or False = %r" % (True or False)

# with
# http://docs.python.org/whatsnew/2.6.html#pep-343-the-with-statement
# groups commands that normally execute together and have a cleanup section
# with open('output.txt', 'w') as f:
#     f.write('Hi there!')

# assert
# ? a convenient way to insert debug assertions

# else
# the catch all statement for an if-statement

# if
# a conditional test that executes the statements within if True

# pass
# ?

# yield
# ?

# break
# ?

# except
# ?

# import
# find a module and import the symbols

# print
# print a string to stdout

# class
# a definition of a logical grouping of variables and functions

# exec
# ?

# in 
# ?

# raise
# ?

# continue
# ?

# finally
# ?

# is
# ?

# return
# return execution to the calling function and optionally return an object from the callee

# def
# define a function

# for
# loop a specified number of times

# lambda
# ?

# try
# ?

## Data Types

# True
# False
# boolean

# None
# ? the null object

# strings
# ASCII 

# numbers
# 1, 2, 3, 4, ...

# floats
# 1.0, 1.1, ... 
# lists

## String Escape Sequences

# %d
# %i
# %u
# signed integer decimal

# %o
# signed octal value

# %x
# signed hexidecimal (lowercase)

# %X
# signed hexidecimal (uppercase)

# %e
# floating point exponential (lowercase)

# %E
# floating point exponential (uppercase) 

# %f

# %F

# %g

# %G

# %c

# %r

# %s

# %%

## Operators

# +

# -

# *

# **

# /

# //

# %

# <

# >

# <=

# >=

# ==

# !=

# <>

# ()

# []

# {}

# @

# ,

# :

# .

# .

# ;

# +=

# -=

# *=

# /=

# //=

# %=

# **=


