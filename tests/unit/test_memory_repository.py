from datetime import date, datetime
from typing import List

import pytest

from covid.domain.model import User, Movie, Genre
from covid.adapters.repository import RepositoryException


def test_repository_can_add_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('Dave') is user


def test_repository_can_retrieve_a_user(in_memory_repo):
    user = in_memory_repo.get_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_can_retrieve_article_count(in_memory_repo):
    number_of_articles = in_memory_repo.get_number_of_articles()

    # Check that the query returned 6 Articles.
    assert number_of_articles == 6


def test_repository_can_add_article(in_memory_repo):
    article = Movie(
        title='Lone Survivor',
        release_year=2019
    )
    in_memory_repo.add_article(article)

    assert in_memory_repo.get_movies_by_title('Lone Survivor') is article











