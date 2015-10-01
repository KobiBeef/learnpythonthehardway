class Other(object):
	"""docstring for Other"""
	def overide(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):
	"""docstring for Child"""
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()