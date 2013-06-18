# Exercise 21: Functions Can Return Something

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"
a = float(raw_input('a? '))
b = float(raw_input('b? '))

age = add(a, b)
height = subtract(a, b)
weight = multiply(a, b)
iq = divide(a, b)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (
	age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "This is equivalent to the operation:"
print "age + (height - weight * iq / 2) = ",
print age + (height - weight * iq / 2)
