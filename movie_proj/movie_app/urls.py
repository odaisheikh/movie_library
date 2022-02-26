from django.urls import path     
from . import views
urlpatterns = [
    path('main_page/', views.main),   
    path('favorite/', views.favorite),
    path('movie/<movie_id>', views.movie),   
    path('watch_list/', views.watch_list),
    path('adding_form', views.adding_form),
    path('add_movie', views.add_movie),
    path('rate/<movie_id>', views.rate),
    path('add_to_watchlist/<movie_id>', views.add_to_watchlist),
    path('add_to_favorites/<movie_id>', views.add_to_favorites),
    path('remove_from_watchlist/<movie_id>', views.remove_from_watchlist),
    path('remove_from_favorites/<movie_id>', views.remove_from_favorites)
]