class Song(object):
    def __init__(self, lyrics, artist):
        self.lyrics = lyrics
        self.artist = artist

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

        print(f"\n-- Sung by {self.artist}\n\n")

    def how_long_am_I(self):
        print(f"this song is {len(self.lyrics)} lines long.")

    def add_line(self, line):
        self.lyrics.append(line)



happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right here"
], 'Time Warner')

bulls_on_parade = Song([
    "They rally around the family",
    "With pockets full of shells"
], 'Rage Against the Machine')

happy_bday.sing_me_a_song()
#happy_bday.how_long_am_I()

happy_bday.add_line("You smell like a monkey")
happy_bday.sing_me_a_song()

