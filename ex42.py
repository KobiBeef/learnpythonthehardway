## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	"""docstring for Animal"""
	pass

## ??
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		## ??
		self.name = name

class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self, name):
		## ??
		self.name = name
		
class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		## ??
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

class Employee(Person):
			"""docstring for Employee"""
			def __init__(self, name, salary):
				## ?? hmm what is this strange magic?
				super(Employee, self).__init__(name)
				self.salary = salary

## ??
class Fish(object):
	"""docstring for Fish"""
	pass

## ??
class Salmon(Fish):
	"""docstring for Salmon"""
	pass

## ??
class Halibut(Fish):
	"""docstring for Halibut"""
	pass

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
