import urllib

def read_text():
	movie_quotes = open("/Users/cameron/Documents/Python_Algorithms/Udacity_Python/movie_quotes.txt")
	contents = movie_quotes.read()
	print(contents)
	movie_quotes.close()
	check_profanity(contents)


def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	print(output)
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly.")

read_text()
