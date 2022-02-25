from django.shortcuts import render


def main(request):
    return render(request,"main_page.html")

def favorit(request):
    return render(request,"favorites.html")

def movie(request):
    return render(request,"movie.html")

def watch_list(request):
    return render(request,"watch_list.html")
