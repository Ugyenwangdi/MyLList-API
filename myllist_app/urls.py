from django.urls import path
from myllist_app import views

app_name = 'myllist'

urlpatterns = [  
    path('', views.Home, name='home'),
    path('movies/', views.Movies, name='movies'),
    path('tvs/', views.TV, name='tvs'),
    path('shows/<str:pk>/', views.MovieDetail, name='movie-detail'),    
    path('about/', views.About, name='about'),
    
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('changepw/', views.changePW, name="changepw"),
    path('logout', views.logout, name='logout'),
    
]