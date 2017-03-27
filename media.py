import webbrowser


class Movie():
    ''' This class provides a way to store movie related info '''

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Google style guide recommends
    # an all caps var name when the var is likely to be
    # constant / unchanged.

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
