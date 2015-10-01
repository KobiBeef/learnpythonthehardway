from sys import exit

def dead(end):
	print end, "its over"
	exit(0)

def room_two(arg1):
	print """
             _________            
            |         |          [*]
            |    X    |          [ ]
            |         |          [_]
            |___" "___|
            |   "/"   |
            |         |
            |         |
            |___"/"___|
            |   " "   |
            |         |
            |         |
            |_________|
	"""
	print "HORAY! natapos din"
	dead("its officially over")

def room_one(arg1):
	print """
             ___" "___                
            |   "/"   |          [*]
            |    V    |          [_]
            |    X    |
            |___"/"___|
            |   " "   |
            |         |
            |         |
            |_________|
       Only door is behind you
         you are at room_one
 a wild pikachu is blocking the way
         What should you do?:
      >"fight"    >"throw pokeball"
      >"run"      >"ignore"
        """
   	check = False

	while True:
		choice = raw_input("> ")

		if choice == "fight":
			print "pikachu used thunderbolt!"
			dead("you died")
		elif choice == "throw pokeball":
			print "pikachu dodged the pokeball, pikachu used thunderbolt"
			dead("you died")
		elif choice == "run":
			print "you went back to room_zero"
			room_zero("you are at room_zero")
		elif choice == "ignore" and not check:
			print "pikachu ran away"
			print """the room is no empty what shoud you do?
>"forward" >"go back room_zero"
			"""
			check = True
		elif choice == "forward":
			print "going to room_two"
			room_two("entering room_two")
		elif choice == "room_zero" and check:
			print "going back to room_zero"
			room_zero("entering room_zero")
		else:
			print "try input again"

def room_zero(arg1):
	print """
             ___" "___
            |   "/"   |          [_]
            |         |
            |    X    |
            |_________|
        You are at room_zero
       Only one door in front
         What should you do?:
           >"forward?"
           >"quit here?"
		  """
	check = False

	while True:
		choice = raw_input("> ")

		if choice == "forward" and not check:
			print "Going inside new room"
			room_one("entering room one")
		elif choice == "quit":
			dead("its over")
		else:
			print "try input again"

room_zero("start")