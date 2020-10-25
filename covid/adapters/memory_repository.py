import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from covid.adapters.repository import AbstractRepository, RepositoryException
from covid.domain.model import Movie, Director, Actor, Review, Genre, User, make_review
import json

class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self._movies = list()
        self._movies_index = dict()
        self._genres = list()
        self._users = list()
        self._reviews = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.user_name == username), None)

    def add_movie(self, movie: Movie):
        insort_left(self._movies, movie)
        self._movies_index[movie.title] = movie

    def get_movie(self, id: int) -> Movie:
        movie = None

        try:
            movie = self._movies[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return movie

    def get_movies_by_title(self, title: str):
        movie = None
        try:
            movie = self._movies_index[title]
        except KeyError:
            pass
        return movie

    def get_number_of_movies(self):
        return len(self._movies)

    def get_movies_by_id(self, id_list):
        # Strip out any ids in id_list that don't represent Article ids in the repository.


        # Fetch the Articles.
        movies = [self._movies[id] for id in id_list]
        return movies

    def get_movies_by_genre(self, genre: str):
        genre_cls = Genre(genre)
        movies = [movie for movie in self._movies if genre_cls in movie.genres]
        return movies

    def get_movies_by_actor(self, actor: str):
        movies = [movie for movie in self._movies if actor in movie.actors]
        return movies

    def get_movies_by_director(self, director: str):
        movies = [movie for movie in self._movies if director in movie.director]
        return movies

    #
    def add_genre(self, genre: Genre):
        self._genres.append(genre)
    #
    def get_genres(self) -> List[Genre]:
        return self._genres
    #
    def add_review(self, review: Review):
        self._reviews.append(review)

    def get_comments(self):
        return self._reviews
    #

def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_movies_and_genres(data_path: str, repo: MemoryRepository):
    genres_list = []
    file_path = os.path.join(data_path, 'image_link.json')
    f = open(file_path, 'r')
    image_link = json.load(f)
    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):
        movie_title = data_row[1]
        movie_year = int(data_row[6])
        geners = data_row[2].split(',')
        director = data_row[4]
        actors = data_row[5].split(',')
        description = data_row[3]
        runtime_minutes = int(data_row[7])
        genres_list.extend(geners)
        genres_list = list(set(genres_list))

        # Add any new tags; associate the current article with tags.

        # Create Article object.
        movie = Movie(
            title=movie_title,
            release_year=movie_year
        )
        if movie_title in image_link.keys():
            movie.image_hyperlink = image_link[movie_title]
        else:
            movie.image_hyperlink ='https://m.media-amazon.com/images/M/MV5BNTY3NTY3ODAzOF5BMl5BanBnXkFtZTcwMTI4MDQyOA@@._V1_SX300.jpg'
        if movie.image_hyperlink == None:
            movie.image_hyperlink ='https://m.media-amazon.com/images/M/MV5BNTY3NTY3ODAzOF5BMl5BanBnXkFtZTcwMTI4MDQyOA@@._V1_SX300.jpg'

        movie.director = Director(director)
        movie.runtime_minutes = runtime_minutes
        movie.description = description
        movie.comments.append("This is first comments")
        for actor in actors:
            movie.add_actor(Actor(actor))
        for gener in geners:
            movie.add_genre(Genre(gener))

        # Add the Article to the repository.
        repo.add_movie(movie)

    for gener_name in genres_list:
        repo.add_genre(Genre(gener_name))


#
#
def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(
            user_name=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def load_reviews(data_path: str, repo: MemoryRepository):
    for data_row in read_csv_file(os.path.join(data_path, 'comments.csv')):
        movie = repo.get_movie(int(data_row[2]))
        review = make_review(movie=movie, review_text=data_row[3], rating=8)
        repo.add_review(review)
#
#
def populate(data_path: str, repo: MemoryRepository):
    # Load articles and tags into the repository.
    load_movies_and_genres(data_path, repo)

    # Load users into the repository.
    users = load_users(data_path, repo)

    # Load comments into the repository.
    load_reviews(data_path, repo)


# if __name__ == '__main__':
#     d = {}
#     for data_row in read_csv_file(os.path.join('./data', 'Data100Movies.csv')):
#         d[data_row[1]] = get_image_hyperlink(title=data_row[1])
#     print(d)
#     with open("./test4.json", 'w') as f:
#         json.dump(d, f)



