ten_things = "Apples Oranges Crows Telephone Light Sugar" # creates a variable ten_things with the assigned value of "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that." # prints "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # splits the contents of variable ten_things every time there is a white space and then assigns it to variable stuff which is now a list bacause of the split function
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] # creates list more_stuff with the contents of "["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]"

while len(stuff) != 10: # creates a while loop. where in checks the length or contents of list stuff. if its contents is not equal to 10 do the following procedures
	next_one = more_stuff.pop() # creates a variable (at this point on a list) next_one where in we pop or remove the last item on the list of more_stuff and assign or store it to next_one
	print "Adding:", next_one # prints "Adding" and the item which was popped from more_stuff which is assigned to next_one
	stuff.append(next_one) # appends or adds the item which was popped from more_stuff which is assigned to next_one to the end of the list of stuff
	print "There are %d items now." % len(stuff) # prints "There are %d items now." where in %d is the number of items in the list stuff

print "There we go: ", stuff # prints "There we go: " and the contents of the list stuff

print "Let's do some things with stuff." # prints "Let's do some things with stuff."

print stuff[1] # prints the 2nd item on the list stuff
print stuff[-1] # whoa! fancy # prints the -1 value of the list which is corn
print stuff.pop() # pops the last item on the list of stuff which is corn
print ' '.join(stuff) # what? cool! # joins the list stuff with a white space inbetween every item
print '#'.join(stuff[3:5]) # super stellar # joins the 4th to the 5th list of the list and adds "#" inbetween