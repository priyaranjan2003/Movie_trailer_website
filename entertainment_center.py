import fresh_tomatoes
import media

#creating and initialising movies objects with their title,storyline,link of movie's poster and trailer

prestige = media.Movie("The Prestige",
                        "Two stage magicians engage in a battle to create the ultimate illusion ",
                        "Rated: PG-13",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Prestige_poster.jpg/220px-Prestige_poster.jpg",
                        "https://www.youtube.com/watch?v=ijXruSzfGEc")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival",
                           "Rated: PG-13",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through the use of dream-sharing technology",
                        "Rated: PG-13",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

batman_begins = media.Movie("Batman Begins",
                            "Batman begins his fight to free crime-ridden Gotham City from the corruption that Scarecrow and the League of Shadows have cast upon it",
                            "Rated: PG-13",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg",
                            "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham",
                              "Rated: PG-13",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=NMz0X-0Ldjg")

dunkirk = media.Movie("Dunkirk",
                      "Allied soldiers from Belgium, the British Empire and France are surrounded by the German Army, and evacuated during a fierce battle in World War II",
                      "Rated: PG-13",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

#movie objects stored in a list
movies = [prestige, interstellar, inception, batman_begins, the_dark_knight, dunkirk]

#open the specified movie page browser
fresh_tomatoes.open_movies_page(movies)
