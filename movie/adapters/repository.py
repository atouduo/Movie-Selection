import abc
from typing import List
from datetime import date

from movie.domain.model import Director, Genre, Actor, Movie, User


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_director(self, director: Director):
        """" Adds a User to the repository. """
        raise NotImplementedError

    def get_director(self) -> list:
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self) -> list:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds an Article to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self) -> list:
        """ Returns movie from the repository.

        If there is no Movie with the given name, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """ Adds a Tag to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self) -> list:
        """ Returns the Tags stored in the repository. """
        raise NotImplementedError








