import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                      "a story of a boy and his toys that come to life",
                      "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on an alien planet",
                    "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print(avatar.storyline)
# avatar.show_trailer()

sacred_games = media.Movie("sacred games","a crime thriller",
						 "https://en.wikipedia.org/wiki/Sacred_Games_(TV_series)#/media/File:Sacred_Games_Title.png",
						 "https://www.youtube.com/watch?v=RWpuZXhCEkQ")
# print(sacred_games.storyline)
# sacred_games.show_trailer()

mirzapur = media.Movie("mirzapur","a crime thriller",
						 "https://en.wikipedia.org/wiki/Mirzapur_(TV_series)#/media/File:Poster_of_Mirzapur_2018.jpg",
						 "https://www.youtube.com/watch?v=RWpuZXhCEkQ")

john_wick = media.Movie("john wick","a action thriller",
						 "https://en.wikipedia.org/wiki/John_Wick_(film)#/media/File:John_Wick_TeaserPoster.jpg",
						 "https://www.youtube.com/watch?v=RWpuZXhCEkQ")

inside_edge = media.Movie("inside_edge","a cricket movie",
						 "https://en.wikipedia.org/wiki/Inside_Edge_(TV_series)#/media/File:Inside_Edge.jpeg",
						 "https://www.youtube.com/watch?v=RWpuZXhCEkQ")


movies = [toy_story,avatar,sacred_games,mirzapur,john_wick,inside_edge]
fresh_tomatoes.open_movies_page(movies)