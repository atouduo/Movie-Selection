from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import covid.adapters.repository as repo
import covid.utilities.utilities as utilities
import covid.news.services as services

from covid.authentication.authentication import login_required


# Configure Blueprint.
news_blueprint = Blueprint(
    'news_bp', __name__)

@news_blueprint.route('/articles_by_tag', methods=['GET'])
def articles_by_tag():
    articles_per_page = 3

    # Read query parameters.
    tag_name = request.args.get('tag')
    cursor = request.args.get('cursor')
    article_to_show_comments = request.args.get('view_comments_for')

    if article_to_show_comments is None:
        # No view-comments query parameter, so set to a non-existent article id.
        article_to_show_comments = -1
    else:
        # Convert article_to_show_comments from string to int.
        # article_to_show_comments = article_to_show_comments
        pass

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    # Retrieve article ids for articles that are tagged with tag_name.
    movies = services.get_movie_for_genre(tag_name, repo.repo_instance)
    movies = services.movies_to_dict(movies)

    articles = movies[cursor:cursor + articles_per_page]

    first_article_url = None
    last_article_url = None
    next_article_url = None
    prev_article_url = None

    if cursor > 0:
        # There are preceding articles, so generate URLs for the 'previous' and 'first' navigation buttons.
        prev_article_url = url_for('news_bp.articles_by_tag', tag=tag_name, cursor=cursor - articles_per_page)
        first_article_url = url_for('news_bp.articles_by_tag', tag=tag_name)

    if cursor + articles_per_page < len(movies):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_article_url = url_for('news_bp.articles_by_tag', tag=tag_name, cursor=cursor + articles_per_page)

        last_cursor = articles_per_page * int(len(movies) / articles_per_page)
        if len(movies) % articles_per_page == 0:
            last_cursor -= articles_per_page
        last_article_url = url_for('news_bp.articles_by_tag', tag=tag_name, cursor=last_cursor)

    for article in articles:
        article['view_comment_url'] = url_for('news_bp.articles_by_tag', tag=tag_name, cursor=cursor, view_comments_for=article['title'])
        article['add_comment_url'] = url_for('news_bp.comment_on_article', article=article['title'])

    # Generate the webpage to display the articles.
    return render_template(
        'news/articles.html',
        title='Articles',
        articles_title='Movies genred by ' + tag_name,
        articles=articles,
        selected_articles=utilities.get_selected_movies(len(articles) * 2),
        tag_urls=utilities.get_genres_and_urls(),
        first_article_url=first_article_url,
        last_article_url=last_article_url,
        prev_article_url=prev_article_url,
        next_article_url=next_article_url,
        show_comments_for_article=article_to_show_comments
    )


@news_blueprint.route('/comment', methods=['GET', 'POST'])
@login_required
def comment_on_article():
    # Obtain the username of the currently logged in user.
    username = session['username']

    # Create form. The form maintains state, e.g. when this method is called with a HTTP GET request and populates
    # the form with an article id, when subsequently called with a HTTP POST request, the article id remains in the
    # form.
    form = CommentForm()

    if form.validate_on_submit():
        # Successful POST, i.e. the comment text has passed data validation.
        # Extract the article id, representing the commented article, from the form.
        title = form.title.data

        # Use the service layer to store the new comment.
        services.add_comment(title, form.comment.data, username, repo.repo_instance)
        print(form.comment.data)


        # Retrieve the article in dict form.
        article = services.get_movie(title, repo.repo_instance)
        article["comments"].append(form.comment.data)
        tag_name = article['genres'][0].genre_name

        # Cause the web browser to display the page of all articles that have the same date as the commented article,
        # and display all comments, including the new comment.
        return redirect(url_for('news_bp.articles_by_tag', tag=tag_name, tagview_comments_for=title))

    if request.method == 'GET':
        # Request is a HTTP GET to display the form.
        # Extract the article id, representing the article to comment, from a query parameter of the GET request.
        title = request.args.get('article')

        # Store the article id in the form.
        form.title.data = title
    else:
        # Request is a HTTP POST where form validation has failed.
        # Extract the article id of the article being commented from the form.
        title = form.title.data

    # For a GET or an unsuccessful POST, retrieve the article to comment in dict form, and return a Web page that allows
    # the user to enter a comment. The generated Web page includes a form object.
    article = services.get_movie(title, repo.repo_instance)
    return render_template(
        'news/comment_on_article.html',
        title='Edit article',
        article=article,
        form=form,
        handler_url=url_for('news_bp.comment_on_article'),
        selected_articles=utilities.get_selected_movies(),
        tag_urls=utilities.get_genres_and_urls()
    )


@news_blueprint.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    movies = []
    movie_title = services.get_movie(keyword, repo.repo_instance)
    movie_director = services.get_movies_by_actor(keyword, repo.repo_instance)
    movie_actor = services.get_movies_by_actor(keyword, repo.repo_instance)
    if movie_title:
        movies.append(movie_title)
    if movie_director:
        movies.extend(movie_director)
    if movie_actor:
        movies.extend(movie_actor)

    articles_per_page = 3

    # Read query parameters.
    tag_name = request.args.get('tag')
    cursor = request.args.get('cursor')
    article_to_show_comments = request.args.get('view_comments_for')

    if article_to_show_comments is None:
        # No view-comments query parameter, so set to a non-existent article id.
        article_to_show_comments = -1
    else:
        # Convert article_to_show_comments from string to int.
        # article_to_show_comments = article_to_show_comments
        pass

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    # Retrieve article ids for articles that are tagged with tag_name.

    articles = movies[cursor:cursor + articles_per_page]
    print(articles)

    first_article_url = None
    last_article_url = None
    next_article_url = None
    prev_article_url = None

    if cursor > 0:
        # There are preceding articles, so generate URLs for the 'previous' and 'first' navigation buttons.
        prev_article_url = url_for('news_bp.articles_by_tag', tag=tag_name, cursor=cursor - articles_per_page)
        first_article_url = url_for('news_bp.articles_by_tag', tag=tag_name)

    if cursor + articles_per_page < len(movies):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_article_url = url_for('news_bp.articles_by_tag', tag=tag_name, cursor=cursor + articles_per_page)

        last_cursor = articles_per_page * int(len(movies) / articles_per_page)
        if len(movies) % articles_per_page == 0:
            last_cursor -= articles_per_page
        last_article_url = url_for('news_bp.articles_by_tag', tag=tag_name, cursor=last_cursor)

    for article in articles:
        article['view_comment_url'] = url_for('news_bp.articles_by_tag', tag=tag_name, cursor=cursor,
                                              view_comments_for=article['title'])
        article['add_comment_url'] = url_for('news_bp.comment_on_article', article=article['title'])

    # Generate the webpage to display the articles.

    if movies:
        return render_template(
            'news/article_search.html',
            articles=articles,
        )

    return render_template(
        'home/home.html',
        selected_articles=utilities.get_selected_movies(),
        tag_urls=utilities.get_genres_and_urls()
    )


class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short'),
        ProfanityFree(message='Your comment must not contain profanity')])
    title = HiddenField("movie title")
    submit = SubmitField('Submit')