# Exercise 19: Functions and variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# pass literals
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# pass integer objects?
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# pass arithmetic literals
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# variables and literals combined using math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# another function
def jello_shots(cup_count, bottle_count, alcohol):
	print "You can make %d %s jello shots." % (bottle_count * 10 / cup_count, alcohol)


jello_shots(int(raw_input('Cups: ')), int(raw_input('Bottles: ')), raw_input("Alcohol: "))

