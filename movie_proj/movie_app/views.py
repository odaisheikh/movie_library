from multiprocessing import context
from platform import release
from django.shortcuts import render, redirect
from login_app.models import *
from movie_app.models import *
from django.contrib import messages


def main(request):
        context = {
            'all_movies' : Movie.objects.all().order_by('-release_date')
        }
        return render(request,"main_page.html" , context)

def favorite(request):
    return render(request,"favorites.html")

def movie(request,movie_id):
    this_movie = Movie.objects.get(id=movie_id)
    x= this_movie.rates.all()
    sum = 0
    avg = 0
    for i in x:
        sum=sum+i.rate
    if len(x) == 0 :
        avg == 'no ranks yet'
    else :
        avg = sum / len(x)
    context = {
        'avg' : avg,
        'this_movie' : this_movie,
        'this_user' : User.objects.get(id=request.session['userid'])
    }
    return render(request,"movie.html",context)

def watch_list(request):
    context = {
        'movies' : Movie.objects.all()
    }
    return render(request,"watch_list.html",context)

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
    return redirect("/")

def rate(request,movie_id):
    this_user=User.objects.get(id= request.session['userid'])
    this_movie=Movie.objects.get(id=movie_id)
    Rate.objects.create(rate=request.POST['star'],movie=this_movie,user=this_user)
    return redirect(f'/movie/{movie_id}')
