# Exercise 32: Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# the first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we canalso build lists, first start with an empty one
# can also use [] to make an empty list
elements = list()

# thenuse the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	## append is a function that lists understand
	#elements.append(i)
	# insert(index, object) will insert at the head (index = 0) of the list
	elements.insert(0, i)
# reverse() will restore the behavior of append()
elements.reverse()

# for now we can print them out too
for i in elements:
	print "Element was: %d" % i


