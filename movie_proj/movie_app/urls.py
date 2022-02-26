from django.urls import path     
from . import views
urlpatterns = [
    path('', views.main),   
    path('favorite/', views.favorite),
    path('movie/<movie_id>', views.movie),   
    path('watch_list/', views.watch_list),
    path('adding_form', views.adding_form),
    path('add_movie', views.add_movie),
    path('rate/<movie_id>', views.rate)
]