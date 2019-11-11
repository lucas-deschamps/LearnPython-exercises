class Song(object):
    def __init__(self, lyrics):
        self.whatever = lyrics

#    for line in self.lyrics:
# AttributeError: 'Song' object has no attribute 'lyrics'
# se tirar self de self.lyrics = lyrics

    def sing_me_a_song(arg):
        for line in arg.whatever:
            print(line)

#    def sing_me_a_song(arg):
#        for line in arg.lyrics:
#            print(line)

# Traceback (most recent call last):
#  File "ex40.py", line 30, in <module>
#    happy_bday.sing_me_a_song()
#  File "ex40.py", line 10, in sing_me_a_song
#    for line in arg.lyrics:
# AttributeError: 'Song' object has no attribute 'lyrics'

# def sing_me_a_song(arg):

# Traceback (most recent call last):
#  File "ex40.py", line 19, in <module>
#    happy_bday.sing_me_a_song()
#  File "ex40.py", line 9, in sing_me_a_s
#    for line in self.lyrics:
# NameError: name 'self' is not defined


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right here!\n"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Write some more songs using this and make sure you understand
# that you're passing a list of strings as the lyrics.

# Put the lyrics in a separate variable,
# then pass that variable to the class to use instead.

# See if you can hack on this and make it do more things.
# Don't worry if you have no idea how, just give it a try, see what happens.
# Break it, trash it, thrash it, you can't hurt it.

# Search online for "object-oriented programming",
# and try to overflow your brain with what you read.
# Don't worry if it makes absolutely no sense to you.
# Half of that stuff makes no sense to me too.
