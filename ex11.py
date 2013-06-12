print "How old are you?", 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)

# Prompt for a number (without int() it will print x multiple times)
x = int(raw_input('--> '))
print "x * 10 = %s" % (x * 10)

