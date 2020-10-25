from typing import List, Iterable

from covid.adapters.repository import AbstractRepository
from covid.domain.model import Movie, Genre, make_review


class NonExistentArticleException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def add_comment(title: str, comment_text: str, username: str, repo: AbstractRepository):
    # Check that the article exists.
    movie = repo.get_movies_by_title(title)
    if movie is None:
        raise NonExistentArticleException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    # Create comment.
    comment = make_review(movie, comment_text)

    # Update the repository.
    repo.add_review(comment)


def get_movie(title: str, repo: AbstractRepository):
    movie = repo.get_movies_by_title(title)

    if movie is None:
        raise NonExistentArticleException

    return movie_to_dict(movie)


def get_movie_for_genre(genre_name, repo: AbstractRepository):
    movies = repo.get_movies_by_genre(genre_name)

    return movies


def get_movies_by_id(id_list, repo: AbstractRepository):
    movies = repo.get_movies_by_id(id_list)

    # Convert Articles to dictionary form.
    movies_as_dict = movies_to_dict(movies)

    return movies_as_dict


def get_movies_by_director(director_name: str, repo: AbstractRepository):
    movies = repo.get_movies_by_director(director_name)
    movies_as_dict = movies_to_dict(movies)
    return movies_as_dict


def get_movies_by_actor(actor_name: str, repo: AbstractRepository):
    movies = repo.get_movies_by_actor(actor_name)
    movies_as_dict = movies_to_dict(movies)
    return movies_as_dict


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'date': movie.release_year,
        'title': movie.title,
        # 'hyperlink': article.hyperlink,
        'image_hyperlink': movie.image_hyperlink,
        'comments': movie.comments,
        'genres': movie.genres,
        'description': movie.description
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]

