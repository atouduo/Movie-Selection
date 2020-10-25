# from datetime import date, datetime
# from typing import List, Iterable
#
#
# class User:
#     def __init__(
#             self, username: str, password: str
#     ):
#         self._username: str = username
#         self._password: str = password
#         self._comments: List[Comment] = list()
#
#     @property
#     def username(self) -> str:
#         return self._username
#
#     @property
#     def password(self) -> str:
#         return self._password
#
#     @property
#     def comments(self) -> Iterable['Comment']:
#         return iter(self._comments)
#
#     def add_comment(self, comment: 'Comment'):
#         self._comments.append(comment)
#
#     def __repr__(self) -> str:
#         return f'<User {self._username} {self._password}>'
#
#     def __eq__(self, other) -> bool:
#         if not isinstance(other, User):
#             return False
#         return other._username == self._username
#
#
# class Comment:
#     def __init__(
#             self, user: User, article: 'Article', comment: str, timestamp: datetime
#     ):
#         self._user: User = user
#         self._article: Article = article
#         self._comment: Comment = comment
#         self._timestamp: datetime = timestamp
#
#     @property
#     def user(self) -> User:
#         return self._user
#
#     @property
#     def article(self) -> 'Article':
#         return self._article
#
#     @property
#     def comment(self) -> str:
#         return self._comment
#
#     @property
#     def timestamp(self) -> datetime:
#         return self._timestamp
#
#     def __eq__(self, other):
#         if not isinstance(other, Comment):
#             return False
#         return other._user == self._user and other._article == self._article and other._comment == self._comment and other._timestamp == self._timestamp
#
#
# class Article:
#     def __init__(
#             self, date: date, title: str, first_para: str, hyperlink: str, image_hyperlink: str, id: int = None
#     ):
#         self._id: int = id
#         self._date: date = date
#         self._title: str = title
#         self._first_para: str = first_para
#         self._hyperlink: str = hyperlink
#         self._image_hyperlink: str = image_hyperlink
#         self._comments: List[Comment] = list()
#         self._tags: List[Tag] = list()
#
#     @property
#     def id(self) -> int:
#         return self._id
#
#     @property
#     def date(self) -> date:
#         return self._date
#
#     @property
#     def title(self) -> str:
#         return self._title
#
#     @property
#     def first_para(self) -> str:
#         return self._first_para
#
#     @property
#     def hyperlink(self) -> str:
#         return self._hyperlink
#
#     @property
#     def image_hyperlink(self) -> str:
#         return self._image_hyperlink
#
#     @property
#     def comments(self) -> Iterable[Comment]:
#         return iter(self._comments)
#
#     @property
#     def number_of_comments(self) -> int:
#         return len(self._comments)
#
#     @property
#     def number_of_tags(self) -> int:
#         return len(self._tags)
#
#     @property
#     def tags(self) -> Iterable['Tag']:
#         return iter(self._tags)
#
#     def is_tagged_by(self, tag: 'Tag'):
#         return tag in self._tags
#
#     def is_tagged(self) -> bool:
#         return len(self._tags) > 0
#
#     def add_comment(self, comment: Comment):
#         self._comments.append(comment)
#
#     def add_tag(self, tag: 'Tag'):
#         self._tags.append(tag)
#
#     def __repr__(self):
#         return f'<Article {self._date.isoformat()} {self._title}>'
#
#     def __eq__(self, other):
#         if not isinstance(other, Article):
#             return False
#         return (
#                 other._date == self._date and
#                 other._title == self._title and
#                 other._first_para == self._first_para and
#                 other._hyperlink == self._hyperlink and
#                 other._image_hyperlink == self._image_hyperlink
#         )
#
#     def __lt__(self, other):
#         return self._date < other._date
#
#
# class Tag:
#     def __init__(
#             self, tag_name: str
#     ):
#         self._tag_name: str = tag_name
#         self._tagged_articles: List[Article] = list()
#
#     @property
#     def tag_name(self) -> str:
#         return self._tag_name
#
#     @property
#     def tagged_articles(self) -> Iterable[Article]:
#         return iter(self._tagged_articles)
#
#     @property
#     def number_of_tagged_articles(self) -> int:
#         return len(self._tagged_articles)
#
#     def is_applied_to(self, article: Article) -> bool:
#         return article in self._tagged_articles
#
#     def add_article(self, article: Article):
#         self._tagged_articles.append(article)
#
#     def __eq__(self, other):
#         if not isinstance(other, Tag):
#             return False
#         return other._tag_name == self._tag_name
#
#
# class ModelException(Exception):
#     pass
#
#
# def make_comment(comment_text: str, user: User, article: Article, timestamp: datetime = datetime.today()):
#     comment = Comment(user, article, comment_text, timestamp)
#     user.add_comment(comment)
#     article.add_comment(comment)
#
#     return comment
#
#
# def make_tag_association(article: Article, tag: Tag):
#     if tag.is_applied_to(article):
#         raise ModelException(f'Tag {tag.tag_name} already applied to Article "{article.title}"')
#
#     article.add_tag(tag)
#     tag.add_article(article)

from datetime import date, datetime

from typing import List, Iterable
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f'<Director {self.__director_full_name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.director_full_name == self.director_full_name

    def __lt__(self, other):
        return self.director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f'<Genre {self.__genre_name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.genre_name == self.__genre_name

    def __lt__(self, other):
        return self.__genre_name < other.genre_name

    def __hash__(self):
        return hash(self.__genre_name)


class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        self.__actors_this_one_has_worked_with = set()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def add_actor_colleague(self, colleague):
        if isinstance(colleague, self.__class__):
            self.__actors_this_one_has_worked_with.add(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__actors_this_one_has_worked_with

    def __repr__(self):
        return f'<Actor {self.__actor_full_name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)


class Movie:

    def __set_title_internal(self, title: str):
        if title.strip() == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    def __set_release_year_internal(self, release_year: int):
        if release_year >= 1900 and type(release_year) is int:
            self.__release_year = release_year
        else:
            self.__release_year = None

    def __init__(self, title: str, release_year: int):

        self.__set_title_internal(title)
        self.__set_release_year_internal(release_year)

        self.__description = None
        self._image_hyperlink: str = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.comments = []

    # essential attributes

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__set_title_internal(title)

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year: int):
        self.__set_release_year_internal(release_year)

    # additional attributes

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if type(description) is str:
            self.__description = description.strip()
        else:
            self.__description = None

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director):
        if isinstance(director, Director):
            self.__director = director
        else:
            self.__director = None

    @property
    def actors(self) -> list:
        return self.__actors

    def add_actor(self, actor: Actor):
        if not isinstance(actor, Actor) or actor in self.__actors:
            return

        self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if not isinstance(actor, Actor):
            return

        try:
            self.__actors.remove(actor)
        except ValueError:
            # print(f"Movie.remove_actor: Could not find {actor} in list of actors.")
            pass

    @property
    def genres(self) -> list:
        return self.__genres

    def add_genre(self, genre: Genre):
        if not isinstance(genre, Genre) or genre in self.__genres:
            return

        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if not isinstance(genre, Genre):
            return

        try:
            self.__genres.remove(genre)
        except ValueError:
            # print(f"Movie.remove_genre: Could not find {genre} in list of genres.")
            pass

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, val: int):
        if val > 0:
            self.__runtime_minutes = val
        else:
            raise ValueError(f'Movie.runtime_minutes setter: Value out of range {val}')

    @property
    def image_hyperlink(self) -> str:
        return self._image_hyperlink

    @image_hyperlink.setter
    def image_hyperlink(self, link: str):
        self._image_hyperlink = link

    def __get_unique_string_rep(self):
        return f"{self.__title}, {self.__release_year}"

    def __repr__(self):
        return f'<Movie {self.__get_unique_string_rep()}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__get_unique_string_rep() == other.__get_unique_string_rep()

    def __lt__(self, other):
        if self.title == other.title:
            return self.release_year < other.release_year
        return self.title < other.title

    def __hash__(self):
        return hash(self.__get_unique_string_rep())


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        if isinstance(movie, Movie):
            self.__movie = movie
        else:
            self.__movie = None
        if type(review_text) is str:
            self.__review_text = review_text
        else:
            self.__review_text = None
        if type(rating) is int and rating >= 1 and rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.movie == self.__movie and other.review_text == self.__review_text and other.rating == self.__rating and other.timestamp == self.__timestamp

    def __repr__(self):
        return f'<Review of movie {self.__movie}, rating = {self.__rating}, timestamp = {self.__timestamp}>'

class User:

    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def watch_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        if isinstance(review, Review):
            self.__reviews.append(review)

    def __repr__(self):
        return f'<User {self.__user_name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.user_name == self.__user_name

    def __lt__(self, other):
        return self.__user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)


def make_review(movie: Movie, review_text: str, rating=5):
    review = Review(movie=movie, review_text=review_text, rating=rating)

    return review



