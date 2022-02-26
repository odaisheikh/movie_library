from multiprocessing import context
from turtle import title
from unicodedata import category
from django.shortcuts import render, redirect
from login_app.models import *
from movie_app.models import *
from django.contrib import messages


def main(request):
    return render(request,"main_page.html")

def favorite(request):
    return render(request,"favorites.html")

def movie(request):
    return render(request,"movie.html")

def watch_list(request):
    return render(request,"watch_list.html")

def adding_form(request):
    return render(request, "add_movie.html")

def add_movie(request):
    errors = Movie.objects.movie_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/adding_form')
    
    user_id = request.session['userid']
    this_user = User.objects.get(id = user_id)
    this_movie = Movie.objects.create(
                                    title = request.POST['title'],
                                    release_date = request.POST['rel_date'],
                                    desc = request.POST['desc'],
                                    trailer_url = request.POST['trailer_url'],
                                    added_by = this_user,
                                    )
    categories = request.POST.getlist('categ')
    for categ in categories:
        this_categ = Category.objects.get(name = categ)
        this_movie.categories.add(this_categ)
    
    return redirect("/added_movies")

def classify(request, categ):
    this_user = User.objects.get(id = request.session['userid'])
    this_category = Category.objects.get(name = categ)
    categ_movies = this_category.movies.all()
    context={
            "user": this_user,
            "movies": categ_movies
            }
    return render(request, "categ_movies.html", context)

def search(request):
    request.session["search"] = request.POST["search"]
    print(request.session["search"])
    return redirect("/movies/search_result")

def search_result(request):
    result = Movie.objects.filter(title__contains = request.session["search"])
    print(result)
    context={
            "result": result
            }
    return render(request,"search_result.html", context)

