from datetime import date

from covid.domain.model import User, Movie, Genre

import pytest


@pytest.fixture()
def article():
    return Movie(
        title='The Equalizer',
        release_year = 2019

    )


@pytest.fixture()
def user():
    return User('dbowie', '1234567890')


@pytest.fixture()
def genre():
    return Genre(genre_name='Action')


def test_user_construction(user):
    assert user.username == 'dbowie'
    assert user.password == '1234567890'
    assert repr(user) == '<User dbowie 1234567890>'

    for comment in user.comments:
        # User should have an empty list of Comments after construction.
        assert False

