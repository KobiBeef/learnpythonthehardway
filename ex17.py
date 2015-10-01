from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two in one line, how?
# in_file = open(from_file)
# indata = in_file.read()

test_in_file = open(from_file).read()

print "The input file is %d bytes long" % len(test_in_file)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(test_in_file)

print "Alright, all done."

out_file.close()
# in_file.close()