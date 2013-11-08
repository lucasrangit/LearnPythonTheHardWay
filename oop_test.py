# Exercise 41: Learning To Speak Object Oriented
# OOP Study Drill

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function names *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill the phrases first
PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True

## load up the words from the website
#for word in urlopen(WORD_URL).readlines():
#	WORDS.append(word.strip())
## use a for loop and local cached copy of the word list
#for word in open('words.txt', 'r'):
#	WORDS.append(word.strip())
# same thing except using list comprehension
WORDS = [word.strip() for word in 
			open('words.txt', 'r')]

def convert(snippet, phrase):
	# List Comprehension
	# return a list of random words for each %%% pattern in snippet string
	# for each word in list capitalize word
	# return resulting list 
	class_names = [w.capitalize() for w in 
					random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	# for each parameter placement
	for i in range(0, snippet.count("@@@")):
		# insert a 1-2 random words
		param_count = random.randint(1,3)
		# seperated by a comma
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentance in snippet, phrase:
		# python list splicing to effectively create a shallow copy
		# (a new list with a copy of the reference to the contained objects)
		# list[start:step:end] is the general syntax
		result = sentance[:]

		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASES_FIRST:
				question, answer = answer, question

			print question

			raw_input('> ')
			print "ANSWER:  %s\n\n" % answer
except EOFError:
	print "\nBye" 
