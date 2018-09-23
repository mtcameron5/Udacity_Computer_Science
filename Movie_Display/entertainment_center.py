import fresh_tomatoes
import media 

avatar = media.Movie("Avatar",
						"A Good Movie",
						"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=6ziBFh3V1aM")	

hunger_games = media.Movie("The Hunger Games", "A quality reality show in a sci-fi environment", 
						   "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
						   "https://www.youtube.com/watch?v=mfmrPu43DF8")

blind_side = media.Movie("The Blind Side", "football", "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
	"https://www.youtube.com/watch?v=gvqj_Tk_kuM")

inception = media.Movie("Inception", "Meta game", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", 
	"https://www.youtube.com/watch?v=8hP9D6kZseM")

print(avatar.title, avatar.storyline, avatar.poster_image_url)

movies = [avatar, hunger_games, inception, blind_side]
fresh_tomatoes.open_movies_page(movies)
						

print(media.Movie.valid_ratings)
print(media.Movie.__doc__)
print(media.Movie.__module__)
print(media.Movie.__name__)