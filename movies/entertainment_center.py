import fresh_tomatoes
import media

groundhog_day = media.Movie("Groundhog Day",
                        "A reporter repeats the same day in a small town, forever.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
                        "https://www.youtube.com/watch?v=tSVeDx9fk60")

what_we_do = media.Movie("What We Do In The Shadows",
                     "A documentary crew follows around a group of vampires that live in a flat",
                     "https://upload.wikimedia.org/wikipedia/en/7/70/What_We_Do_in_the_Shadows_poster.jpg",
                     "https://www.youtube.com/watch?v=IAZEWtyhpes")                    

ex_machina = media.Movie("Ex Machina",
                         "A man falls in love with an intelligent humanoid robot. Chaos ensues.",
                         "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
                         "https://www.youtube.com/watch?v=bggUmgeMCdc")

goodfellas = media.Movie("GoodFellas",
                         "A Brooklyn kid is adopted by neighborhood gangsters.",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

mistaken_for_strangers = media.Movie("Mistaken For Stangers",
                                     "An aspiring filmmaker documents his succesful older brother's band while he's a roadie.",
                                     "http://www.audiofemme.com/wp-content/uploads/2014/04/mistaken-for-strangers.jpg",
                                     "https://www.youtube.com/watch?v=FNmprL3SOlM")

no_country = media.Movie("No Country For Old Men",
                         "A working man is on the run after finding $2 million dollars",
                         "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
                         "https://www.youtube.com/watch?v=38A__WT3-o0")

movies = [groundhog_day, what_we_do, ex_machina, goodfellas, mistaken_for_strangers, no_country]
fresh_tomatoes.open_movies_page(movies)

