class Song(object):
    
    def __init__(self, lyrics):

        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy Birthday to you..",
                   "I will stop here...."])

bulls_on_parade = Song(["They rally around the house",
                        "With something"])

happy_bday.sing_me_a_song()


bulls_on_parade.sing_me_a_song()
