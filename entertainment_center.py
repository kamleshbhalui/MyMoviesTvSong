import media
import fresh_tomatoes
toy_story=media.Movie("Toy Story","A Story f a boy and toy which comes into life","http://www.impawards.com/1995/posters/toy_story_ver1.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

ghajini=media.Movie("Ghajini","A story of business men turned short term memory loss patient after his girl freind murderd by gundas","http://img.moviepostershop.com/ghajini-movie-poster-2008-1010490017.jpg","https://www.youtube.com/watch?v=j_DshRUOm-o")

threeidiots=media.Movie("Three Idiots","A story of three friends","http://www.media.glamsham.com/download/poster/images/3_idiots/3-idiots-02.jpg","https://www.youtube.com/watch?v=xvszmNXdM4w")

a=[toy_story,ghajini,threeidiots]

fresh_tomatoes.open_movies_page(a)
