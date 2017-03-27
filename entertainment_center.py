import media
import fresh_tomatoes

# info provided for each movie below is title,
# plot, poster image and trailer

the_dark_knight = media.Movie("The Dark Knight",
                              "A gang of criminals rob a"
                              "Gotham City mob bank, double-crossing and"
                              "murdering each other until there is only one"
                              "left: The Joker, who escapes with the money.",
                              "https://upload.wikimedia.org/wikipedia/en/8/8"
                              "a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

the_great_gatsby = media.Movie("The Great Gatsby",
                               "Midwest native Nick Carraway arrives in 1922"
                               "New York in search of the American dream."
                               "Nick, a would-be writer, moves in next-door"
                               "to millionaire Jay Gatsby and across the"
                               "bay from his cousin Daisy and her"
                               "philandering husband, Tom. Thus, Nick"
                               "becomes drawn into the captivating world"
                               "of the wealthy and -- as he bears witness"
                               "to their illusions and deceits -- pens a"
                               "tale of impossible love, dreams, and"
                               "tragedy.",
                               "https://upload.wikimedia.org/wikipedia/en/"
                               "thumb/c/c2/TheGreatGatsby2013Poster.jpg/"
                               "220px-TheGreatGatsby2013Poster.jpg",
                               "https://www.youtube.com/watch?v=AnUHtjqEKjU")

iron_man = media.Movie("Iron Man",
                       "A billionaire industrialist and genius inventor,"
                       "Tony Stark, is conducting weapons tests overseas"
                       ", but terrorists kidnap him to force him to "
                       "build a devastating weapon. Instead, he builds"
                       "an armored suit and upends his captors. Returning"
                       "to America, Stark refines the suit and uses it to"
                       "combat crime and terrorism.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb"
                       "/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")


the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street",
                                      "A recount of Jordan Belfort's "
                                      "perspective on his career as a"
                                      "stockbroker in New York City "
                                      "and how his firm Stratton Oakmont"
                                      "engaged in rampant corruption and"
                                      "fraud on Wall Street that ultimately"
                                      "led to his downfall.",
                                      "https://upload.wikimedia.org/wiki"
                                      "pedia/en/1/1f/WallStreet2013poster."
                                      "jpg",
                                      "https://www.youtube.com/watch?v=iszwu"
                                      "X1AK6A")
                  
harry_potter = media.Movie("Harry Potter",
                           "The life of a young wizard, Harry Potter,"
                           "and his friends Hermione Granger and Ron"
                           "Weasley, all of whom are students at"
                           "Hogwarts School of Witchcraft and "
                           "Wizardry. The main story arc concerns"
                           "Harry's struggle against Lord Voldemort"
                           ", a dark wizard who intends to become"
                           "immortal, overthrow the wizard governing"
                           "body known as the Ministry of Magic, and"
                           "subjugate all wizards and non-wizards",
                           "https://s-media-cache-ak0.pinimg.com/"
                           "236x/c5/f8/de/c5f8de5f9a0717296f3041"
                           "65928eca27.jpg",
                           "https://www.youtube.com/watch?v=LYKxhbcZr"
                           "N8")

step_brothers = media.Movie("Step Brothers",
                            "Two 40 year old men become step brothers and "
                            "a forced to live together",
                            "https://upload.wikimedia.org/wikipedia/en/"
                            "thumb/d/d9/StepbrothersMP08."
                            "jpg/220px-StepbrothersMP08.jpg",
                            "https://www.youtube.com/watch?v=CewglxElBK0")

movies = [the_dark_knight, the_great_gatsby, iron_man, the_wolf_of_wall_street, harry_potter, step_brothers]

fresh_tomatoes.open_movies_page(movies)
