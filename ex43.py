from sys import exit
from random import randint

class Scene(object):
	"""docstring for Scene
	creates a CLASS Scene() which is-an object which has a function enter() and takes its-'self' as a parameter
	"""
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		# exit(1)
	 	pass

# a_game = Engine(a_map)
class Engine(object):
	"""docstring for Engine
	creates a CLASS Engine() which is-an object which has __init__ that takes its-'self' and scene_map as a parameter
	also has the function play() which takes its-'self' as a parameter
	"""
	# scene_map <= a_game <= Enigine(a_map) <= a_map <= Map('central_corridor') <= CentralCorridor()
	def __init__(self, scene_map):
		#self.scene_map <= scene_map <= Enigine(a_map) <= a_map <= Map('central_corridor') <= CentralCorridor()
		#self.scene_map <= 'central_corridor' <= CentralCorridor()
		self.scene_map = scene_map
		pass

	#a_game.play()
	def play(self):
		# current_scene <= self.scene_map <= calls opening_scene() which requires 1 parameter(self) | opening_scene() <= self.scene_map <= scene_map <= a_game <=Engine(a_map) <= a_map <= Map('central_corridor') <= 'central_corridor' <= CentralCorridor()
		# current_scene <= 'central_corridor' <= CentralCorridor()
		current_scene = self.scene_map.opening_scene()
		
		# last_scene <= self.next_scene('finished') <= 'finished' <= Finished()
		# last_scene <= 'finished' <= Finished()
		last_scene = self.scene_map.next_scene('finished')

		# current_scene <= 'central_corridor' <= CentralCorridor() != last_scene <= 'finished' <= Finished() ? True
		while current_scene != last_scene:
			# next_scene_name <= current_scene <= enter('central_corridor') <= self.scene_map('central_corridor') <= opening_scene()
			# next_scene_name = 'central_corridor'
			# runs 'central_corridor'.enter() then returns 'central_corridor', 'laser_weapon_armory' OR 'death' to next_scene_name
			next_scene_name = current_scene.enter()
			
			# example| returns next_scene_name <= 'central_corridor' <= CentralCorridor()
			
			# current_scene <= next_scene_name(next_scene_name) <=  next_scene_name <='central_corridor'
			# current_scene <= 'central corridor'
			current_scene = self.scene_map.next_scene(next_scene_name)
			# exit(while-loop)
			pass

		#current_scene <= 'central_corridor <= .enter()
		current_scene.enter()
		pass

class Death(Scene):
	"""docstring for Death
	creates a CLASS Death() that is-a Scene() which has-a function enter() that takes its-'self' as a parameter 
	"""
	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... is she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this"
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		pass

class CentralCorridor(Scene):
	"""docstring for CentralCorridor
	creates a CLASS CentralCorridor() that is-a Scene() which has-a function enter() that takes its-'self' as a parameter
	returns 'death', 'central_corridor', OR 'laser_weapon_armory'
	"""
	
	def enter(self):
		print "The Gothons of the Planet Percal #25 have inavaded your ship and destroyed"
		print " your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb fom the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."

		action = raw_input("> ")

		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insan rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'
		elif action == "dodge!":
			print "LIke a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head up on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts our laughing and can't move."
			print "While he's laughing you run up and shoot him square in his head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'
		else:
			print "DOES NOT COMPUTE"
			return 'central_corridor'
			pass
		pass
		
class LaserWeaponArmory(Scene):
	"""docstring for LaserWeaponArmory
	creates a CLASS LaserWeaponArmory() which is-a Scene() which has-a function enter() that takes its-'self' as a parameter
	returns 'death' OR 'the_bridge'
	"""
	def enter(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in tis container. There's a keypad lock on the box"
		print "and you need the code to get the bombo out. If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb. the code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != code and guessess < 10:
			print "BZZZEDDD!"
			guessess += 1
			guess = raw_input("[keypad]> ")
			pass

		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'
			pass
		pass

class TheBridge(Scene):
	"""docstring for TheBridge
	creates a CLASS TheBridge() which is-a Scene() which has-a function enter() that takes its-'self' as a parameter
	returns 'death', 'the_bridge' OR 'escape_pod'
	"""
	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
		print "under your arm and suprises 5 Gothons who are trying to"
		print "take control of the ship. Each of them has an even uglier"
		print "clown costume than the last. they haven't pulled thier"
		print "weapins out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."

		action = raw_input("> ")

		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door. Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowng they will probably blow up when"
			print "it goes off."
			return 'death'
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put thier hainds up and start to sweat"
			print "You inch backward to the door , open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jmp back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return 'the_bridge'
			pass
		pass

class EscapePod(Scene):
	"""docstring for EscapePod
	creates a CLASS TheBridge() which is-a Scene() which has-a function enter() that takes its-'self' as a parameter
	returns 'death', 'the_bridge' OR 'escape_pod'
	"""
	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes. It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference. You get the chamber with the escape pods, and"
		print "now need to pick one to take. Some of them could be damaged"
		print "but you don't have time to look. There's 5 pods, which one"
		print "do you take?"

		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")

		if int(guess) != good_pod:
			print "You jump into pod %s and hit the enject button." % guess
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly"
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planete below. As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time. You won!"
			return 'finished'
			pass
		pass

class Finished(Scene):
	"""docstring for Finished
	creates a CLASS Finished() which is-a Scene() which has-a function enter() that takes its-'self' as a parameter
	returns 'finished'
	"""
	def enter(self):
		print "You won! Good job"
		return 'finished'

# a_map = Map('central_corridor')
class Map(object):
	"""docstring for Map
	creates a CLASS Map which is-an object which has-a __init__ that takes its-'self' and start_scene as parameters
	also has-a function next_scene() which takes its-'self' and scene_name as parameters
	also has-a function opening_scene which takes its-'self' as a parameter
	also has-a dict.scene
	"""
	scene = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}

	def __init__(self, start_scene):
		#start_scene <= a_map <= Map('central_corridor') <= CentralCorridor()
		#self.start_scene <= 'central_corridor' <= CentralCorridor() 
		self.start_scene = start_scene
		pass

	def next_scene(self, scene_name):
		# is called by function opening_scene from CLASS Map()
		# next_scene now has 2 parameters(self, scene_name|<= self.start_scene() <= 'central_corridor' <= CentralCorridor())
		# creates a variable var <= looks at the varaible 'scene' from Class Map() and gets the scene_name key which is 'central_corridor' with the value CentralCorridor()
		val = Map.scene.get(scene_name)
		# returns val <= {'central_corridor': CentralCorridor()}
		return val

	def opening_scene(self):
		# is called by function play() from CLASS Engine()
		# returns and calls self.next_scene() which requires 2 parameters(self, scene_name|<= self.start_scene() <= 'central_corridor' <= CentralCorridor())
		return self.next_scene(self.start_scene)

#trying to test Class Scene()
test = Scene()
test.enter()
print  "\n"

# instantiate an object a_map that is-a CLASS Map() has-an object 'central_corridor' <= CentralCorridor()
a_map = Map('central_corridor')

# instantiate a_game that is-a CLASS Engine(), has-an object a_map <= 'central_corridor' <= CentralCorridor()
a_game = Engine(a_map)

# object a_game gets the function of play() of the CLASS Engine()
a_game.play()