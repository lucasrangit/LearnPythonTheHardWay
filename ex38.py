# Exercise 38: Doing Things To Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
print stuff
stuff = str.split(ten_things, ' ')
print stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

	next_one = list.pop(more_stuff) 	
	print "Adding: ", next_one
	list.append(stuff, next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy

print stuff.pop()
print list.pop(stuff)

print ' '.join(stuff) # what? cool!
print str.join(' ', stuff)

print '#'.join(stuff[3:5]) # supper stellar!
print str.join('#', stuff[3:5])

# Print the symbols in the current namespace
print dir()

