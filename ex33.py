# Exercise 33: While Loops

numbers = []

def list_append_num(num, inc):
	i = 0
	#while i < num:
	for i in range(0,num):
		print "At the top i is %d" % i
		numbers.append(i)

		#i = i + inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

num_max = int(raw_input('Max: '))
num_inc = int(raw_input('Increment: '))
list_append_num(num_max, num_inc)
print "The numbers: "

for num in numbers:
	print num
