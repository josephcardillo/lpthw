# Classes
# https://docs.python.org/3/tutorial/classes.html

# class Song():

#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# happy_bday = Song(["Happy birthday to you",
#                     "I don't want to get sued",
#                     "So I'll stop right there"])

# bulls_on_parade = Song(["They rally around tha family",
#                         "With pockets full of shells"])

# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()

class Song(object):

    def __init__(self, lyrics, surprise):
        self.lyrics = lyrics
        self.ending = surprise

    def sing_the_song(self):
        for line in self.lyrics:
            print(line, self.ending)

say_it_aint_so = Song(["Say it ain't so",
                        "Your love is a heartbreaker",
                        "Your drug is a lifetaker"], "bruh")

say_it_aint_so.sing_the_song()

# class Weather(object):

#     def __init__(self, today, tomorrow):
#         self.today = today
#         self.tomorrow = tomorrow

#     def hi_low(self):
#         print(f"Today's weather is: {self.today}")
#         print(f"Tamarya's weather is: {self.tomorrow}")

# two_day_forecast = Weather("High of 30, low of 7", "High of 32, low of 16")

# two_day_forecast.hi_low()

class Weather:

    def __init__(self, today, tomorrow):
        self.today = today
        self.tomorrow = tomorrow

    def hi_low(self):
        print(f"Today's weather is: {self.today}")
        print(f"Tamarya's weather is: {self.tomorrow}")

two_day_forecast = Weather("High of 30, low of 7", "High of 32, low of 16")

two_day_forecast.hi_low()
