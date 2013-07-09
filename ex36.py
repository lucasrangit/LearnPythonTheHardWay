# Exercise 36: Designing and Debugging
# Rachel's Commute Text Adventure

from sys import exit

def start():
	print """
You wake up on the subway in an unknown world.
The subway shakes and rattles your body around.
You look to your left and the seat has a paper bag.
You look to your right and there is a crazy bum with puss in his eyes. 
"""
	
	while True:
		next = raw_input("Do you choose the bag of the bum? ")

		if "bag" == next:
			bag()
		elif "bum" == next:
			bum()
		else:
			print "Quoi?"
	
	
def bag():
	print """
You open the bag and there is a bum poo poo. 
You touch the poo and it gives you magical powers. 
"""

	while True:
		next = raw_input("What do you use your powers for? Good or evil? ")

		if "good" == next:
			good()
		elif "evil" == next:
			evil()
		else:
			print "There are no other options."

def good():
	print """
You turn the bum into a sexy beast and ride him into the sunset. 
You win Love! THE END.
"""
	exit(0)

def evil(): 
	print """
You kill the bum and his soul escapes and eats you alive. YOU DIE.
"""
	exit(0) 

def bum():
	print """
You ask the bum for help and he takes off his puss mask. 
He is a beautiful prince, and he gives you LSD.
"""


	while True:
		next = raw_input("Do you take the LSD? ")

		if "no" == next:
			print """
You get off the train and run, and you escape into the beautiful forest. 
Too bad there was poisonous roaches there. YOU DIE.
"""
		elif "yes" == next:
			print """
You take the Bum's LSD and you go out of your mind and become the crazy bum on the train. THE END.
"""
		else:
			print "Are you high?"			
 

# Main Entry
start()
