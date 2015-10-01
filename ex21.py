def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract (a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#-------------simplified------------
#print age + height - weight * iq / 2

#------------brute force raw_input------------
# a = int(raw_input())
# b = int(raw_input())
# c = int(raw_input())
# d = int(raw_input())
# e = int(raw_input())
# f = int(raw_input())
# g = int(raw_input())
# h = int(raw_input())

# brute_age = add(a, b)
# brute_height = subtract(c, d)
# brute_weight = multiply(e, f)
# brute_iq = divide(g, h)

# print brute_age
# print brute_height
# print brute_weight
# print brute_iq

# total = add(brute_age, subtract(brute_height, multiply(brute_weight, divide(brute_iq, 2))))
# print "the total is: ", total

#----------------double raw_input no total---------------
# print "enter 1st and 2nd"
# test_input = map(int,raw_input().split())
# def new_age():
# 	test_age = map(int, raw_input().split())
# 	return
def new_age(): 
	test_input = map(int, raw_input().split())
	a, b = test_input
	test_output = add(a, b)
	print test_output
	return test_output

def new_height():
	test_input = map(int,raw_input().split())
	a, b = test_input
	test_output = subtract(a, b)
	print test_output
	return test_output

def new_weight():
	test_input = map(int, raw_input().split())
	a, b = test_input
	test_output = multiply(a, b)
	print test_output
	return test_output

def new_iq():
	test_input = map(int, raw_input().split())
	a, b = test_input
	test_output = divide(a, b)
	print test_output
	return test_output

second_age = new_age()
second_height = new_height()
second_weight = new_weight()
second_iq = new_iq()

# test = new_age() + new_height()
# print test
new_total = add(second_age, subtract(second_height, multiply(second_weight, divide(second_iq, 2))))
# new_total = add(new_age(), new_height())
print new_total

# def best_age(a, b):
	# test_input = map(int, raw_input().split())
	# a, b = test_input
	# test_output = add(a, b)
	# print test_output
	# return a + b

# best_age(new_age(), new_height())