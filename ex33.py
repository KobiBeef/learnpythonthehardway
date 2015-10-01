i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num

# function while-loop
def test_loop():
	i = 0
	while i < num_input:
		print "at the top i is %d" % i
		new_number.append(i)

		i = i + increment
		print "Numbers now: ", new_number
		print "At the bottom i is %d" % i

def test_loop2():
	print "The numbers:"
	for num in new_number:
		print num

new_number = []
print "Input range of list:"
num_input = int(raw_input("> "))

print "Input increment of list: "
increment = int(raw_input("> "))

test_loop()
test_loop2()