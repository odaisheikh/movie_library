from django.db import models
from login_app.models import *
import datetime


class MovieManager(models.Manager):
    def movie_validator(self, postData):
        errors = {}
    # Title Validation
        if len(postData['title']) == 0:
            errors["title"] = "Title is required!"
    # Release_date Validation
        today = datetime.date.today()
        rel_date = datetime.datetime.strptime(postData['rel_date'], "%Y-%m-%d")
        if rel_date.date() > today:
            errors["rel_date"] = "The release date must be in the past!"
    # Description validation
        if len(postData['desc']) < 5:
            errors["desc"] = "description should be at least 5 characters"
        return errors
    


class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # movies = a list of movies are in the given category


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(null = True)
    desc = models.TextField()
    trailer_url = models.URLField(max_length=300)
    # relation-ships with the User class:
    added_by = models.ForeignKey(User, related_name="added_movies", on_delete = models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="favorites")
    to_watch_by = models.ManyToManyField(User, related_name="movies_to_watch")
    # relation-ship with the Category class:
    categories = models.ManyToManyField(Category, related_name="movies")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovieManager()
    # comments = list of comments on the given movie


class Comment(models.Model):
    comment = models.TextField()
    # relation-ship with the Movie class:
    movie = models.ForeignKey(Movie, related_name="comments", on_delete = models.CASCADE)
    # relation-ship with the User class:
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






