from django.urls import path     
from . import views
urlpatterns = [
    path('main_page/', views.main),   
    path('favorite/', views.favorit),   
    path('movie/', views.movie),   
    path('watch_list/', views.watch_list),  
]