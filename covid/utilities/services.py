from typing import Iterable
import random

from covid.adapters.repository import AbstractRepository
from covid.domain.model import Movie


# def get_tag_names(repo: AbstractRepository):
#     tags = repo.get_tags()
#     tag_names = [tag.tag_name for tag in tags]
#
#     return tag_names


def get_genres_names(repo: AbstractRepository):
    genres = repo.get_genres()
    genre_names = [genre.genre_name for genre in genres]
    return genre_names

# def get_random_articles(quantity, repo: AbstractRepository):
#     movies_count = repo.get_number_of_articles()
#
#     if quantity >= article_count:
#         # Reduce the quantity of ids to generate if the repository has an insufficient number of articles.
#         quantity = article_count - 1
#
#     # Pick distinct and random articles.
#     random_ids = random.sample(range(1, article_count), quantity)
#     articles = repo.get_articles_by_id(random_ids)
#
#     return articles_to_dict(articles)

def get_random_movies(quantity, repo: AbstractRepository):
    movie_cout = repo.get_number_of_movies()
    if quantity >= movie_cout:
        quantity = movie_cout - 1

    random_ids = random.sample(range(1, movie_cout), quantity)
    movies = repo.get_movies_by_id(random_ids)
    return movies_to_dict(movies)


# Reduce the quantity of ids to generate if the repository has an insufficient number of articles.
#         quantity = article_count - 1




# ============================================
# Functions to convert dicts to model entities
# ============================================

def movie_to_dict(movie: Movie):
    article_dict = {
        'description': movie.description,
        'title': movie.title,
        'image_hyperlink': movie.image_hyperlink,
        'date': movie.release_year
    }
    return article_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]
