import webbrowser

class Movie():
    """different movie attributes:
       title,storyline,rating of the movie,url of movie poster,url of movie trailer
    """
    def __init__(self, movie_title, movie_storyline, movie_rating, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#plays the trailer of the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
