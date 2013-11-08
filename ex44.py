# Exercise 44: Inheritance vs. Composition

class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Parent(object):

	def __init__(self):
		print "PARENT __init__()"

	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	# parent __init__ is not inherited

	def __init__(self, stuff):
		print "CHILD stuff:", stuff
		super(Child, self).__init__()
		self.other = Other()

	def override(self):
		"override the parent class method"
		print "CHILD override()"
		self.other.implicit()

	def altered(self):
		"override thbe parent class method and call it explicitly"
		print "CHILD before PARENT altered()"
		# call super with arguments Child and self, then call the function altered on returned
		super(Child, self).altered()
		print "CHILD after PARENT altered()"
		print "CHILD before OTHER altered()"
		self.other.altered()
		print "CHILD after OTHER altered()"

dad = Parent()
# Child does not inherit the __init__ from Parent
#son = Child()
son = Child('toys')

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
