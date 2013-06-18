# Exercise 17: More files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# this entire script in one line: (python will close the file for one-line like this)
open(to_file, 'w').write(open(from_file).read())

# long form:
in_file = open(from_file)
indata = in_file.read()
# This could be donein one line as follows
#indata = open(from_file).read()

if exists(to_file):
	print "Target file %s exists." % (to_file)
	print "Hit RETURN to continue, CTRL-C to abort.",
	raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Copied %d bytes from %s to %s." % (len(indata), from_file, to_file)

out_file.close()
in_file.close()
