from django.urls import path     
from . import views
urlpatterns = [
    path('main_page/', views.main),   
    path('favorite/', views.favorite),
    path('movie/', views.movie),   
    path('watch_list/', views.watch_list),
    path('adding_form', views.adding_form),
    path('add_movie', views.add_movie),
]