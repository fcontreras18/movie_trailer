import fresh_tomatoes
import media
import omdb

groundhog_omdb = omdb.get(title='Groundhog Day',
                          year=1993, fullplot=True, tomatoes=True)
what_we_do_omdb = omdb.get(title='What We Do In The Shadows',
                           year=2014, fullplot=True, tomatoes=True)
ex_machina_omdb = omdb.get(title='Ex Machina',
                           year=2015, fullplot=True, tomatoes=True)
goodfellas_omdb = omdb.get(title='Goodfellas',
                           year=1990, fullplot=True, tomatoes=True)
mistaken_for_strangers_omdb = omdb.get(title='Mistaken For Strangers',
                                       year=2013, fullplot=True, tomatoes=True)
no_country_omdb = omdb.get(title="No Country For Old Men",
                           year=2007, fullplot=True, tomatoes=True)
    
groundhog_day = media.Movie("Groundhog Day",
                        groundhog_omdb.plot,
                        groundhog_omdb.genre,
                        groundhog_omdb.tomato_meter,
                        groundhog_omdb.poster,
                        "https://www.youtube.com/watch?v=tSVeDx9fk60")

what_we_do = media.Movie("What We Do In The Shadows",
                     what_we_do_omdb.plot,
                     what_we_do_omdb.genre,
                     what_we_do_omdb.tomato_meter,
                     what_we_do_omdb.poster,
                     "https://www.youtube.com/watch?v=IAZEWtyhpes")                    

ex_machina = media.Movie("Ex Machina",
                         ex_machina_omdb.plot,
                         ex_machina_omdb.genre,
                         ex_machina_omdb.tomato_meter,
                         ex_machina_omdb.poster,
                         "https://www.youtube.com/watch?v=bggUmgeMCdc")

goodfellas = media.Movie("GoodFellas",
                         goodfellas_omdb.plot,
                         goodfellas_omdb.genre,
                         goodfellas_omdb.tomato_meter,
                         goodfellas_omdb.poster,
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

mistaken_for_strangers = media.Movie("Mistaken For Stangers",
                                     mistaken_for_strangers_omdb.plot,
                                     mistaken_for_strangers_omdb.genre,
                                     mistaken_for_strangers_omdb.tomato_meter,
                                     mistaken_for_strangers_omdb.poster,
                                     "https://www.youtube.com/watch?v=FNmprL3SOlM")

no_country = media.Movie("No Country For Old Men",
                         no_country_omdb.plot,
                         no_country_omdb.genre,
                         no_country_omdb.tomato_meter,
                         no_country_omdb.poster,
                         "https://www.youtube.com/watch?v=38A__WT3-o0")

movies = [groundhog_day, what_we_do, ex_machina, goodfellas, mistaken_for_strangers, no_country]
fresh_tomatoes.open_movies_page(movies)
