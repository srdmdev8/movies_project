import fresh_tomatoes
import media

#Create instances of the Movie class
fight_club = media.Movie("Fight Club",
                         "A story about a man with insomnia who creates a fight club",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMzFjMWNhYzQtYTIxNC00ZWQ1LThiOTItNWQyZmMxNDYyMjA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

little_big_league = media.Movie("Little Big League",
                                "A story about a boy who inherits the Minnesota Twins",
                                "http://www.gstatic.com/tv/thumb/movieposters/15783/p15783_p_v8_ab.jpg",
                                "https://www.youtube.com/watch?v=0ZC0nu_plIA&t=11s")

dark_tower = media.Movie("The Dark Tower",
                         "A story about a boy whos night terrors become real in an inter-dimensional fight for the safety of the Universe",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3MjUwMzQ3MF5BMl5BanBnXkFtZTgwMjcwNjkxMjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=qv1jg9mNr9E")

arrival = media.Movie("Arrival",
                      "A story about a linguist who is recruited by the military to communicate with alien lifeforms after twelve mysterious spacecrafts land around the world",
                      "http://cdn3-www.comingsoon.net/assets/uploads/gallery/arrival/arrivalposter.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

cloudy_meatballs = media.Movie("Cloudy With A Chance of Meatballs",
                               "A story about a local scientist who invents a machine that can make food fall from the sky",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0MjAwNDI5MV5BMl5BanBnXkFtZTcwODkyMzg2Mg@@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=pUaKcFI4BZY")

black_panther = media.Movie("Black Panther",
                            "A story about T'Challa, the King of Wakanda, who rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

#Create movies array and utilize fresh_tomatoes to open movies page
movies = [fight_club, little_big_league, dark_tower, arrival, cloudy_meatballs, black_panther]
fresh_tomatoes.open_movies_page(movies)
