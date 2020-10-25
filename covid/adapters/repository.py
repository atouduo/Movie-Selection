import abc
from typing import List
from datetime import date

from covid.domain.model_movie import User, Movie, Genre, Review, Actor, Director


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """" Adds a User to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        """ Returns the User named username from the repository.

        If there is no User with the given username, this method returns None.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, article: Movie):
        """ Adds an Article to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, id: int) -> Movie:
        """ Returns Article with id from the repository.

        If there is no Article with the given id, this method returns None.
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_articles_by_date(self, target_date: date) -> List[Movie]:
    #     """ Returns a list of Articles that were published on target_date.
    #
    #     If there are no Articles on the given date, this method returns an empty list.
    #     """
    #     raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of Articles in the repository. """
        raise NotImplementedError


    @abc.abstractmethod
    def get_movies_by_id(self, id_list):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_title(self, title: str):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_genre(self, genre: str):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_actor(self, actor: str):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    def get_movies_by_director(self, director: str):
        """ Returns a list of Articles, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.
        """
        raise NotImplementedError

    #
    @abc.abstractmethod
    def add_genre(self, tag: Genre):
        """ Adds a Tag to the repository. """
        raise NotImplementedError
    #

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Returns the Tags stored in the repository. """
        raise NotImplementedError
    #
    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a Comment to the repository.

        If the Comment doesn't have bidirectional links with an Article and a User, this method raises a
        RepositoryException and doesn't update the repository.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_comments(self):
        """ Returns the Comments stored in the repository. """
        raise NotImplementedError







