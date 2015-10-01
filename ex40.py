class Song(object):
	"""docstring for Song"""
	def __init__(self, lyrics):
		self.lyrics = lyrics
		pass

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
		pass

happy_bday = Song([
	"Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop rith there."])

bulls_on_parade = Song([
	"The rally around the family",
	"With pockets full of shells."])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
# class Song(object):
# 	"""docstring for Song"""
# 	test = ""	

# 	def __init__(self, lyrics):
# 		self.lyrics = lyrics
# 		Song.test = "mic test, mic test, 1, 2, 3"
# 		print Song.test

# 	def sing_me_a_song(self):
# 		for line in self.lyrics:
# 			print line
# 			# print Song.test

# happy_bday = Song(["Happy birthday to you",
# 					"I don't want to get sued",
# 					"So i'll stop right there"])

# bulls_on_parade = Song(["They rally arount tha family",
# 						"With pockets full of shells"])

# mic_test = Song(["mic test, mic test, 1, 2, 3"])

# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()
# mic_test.sing_me_a_song()