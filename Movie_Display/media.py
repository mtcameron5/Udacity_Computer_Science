import webbrowser

class Movie():
	""" This class provides a way to store movie related information"""

	valid_ratings = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

list = "good", "job", "nice", "work", "thanks"
for a in list:
	print(a)

def divide(dividend, divisor):
	quotient = dividend / divisor
	remainder = dividend % divisor 
	return quotient, remainder 

print(divide(10, 10))
z = divide(5, 3)
x,y = divide(5, 2)
print(x,y)
print z

	