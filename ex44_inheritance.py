class Parent(object):
	"""docstring for Parent"""
	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	"""docstring for Child"""

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER altered()"

	# def __init__(self, stuff):
	# 	self.stuff = stuff
	# 	super(Child, self).__init__()
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()