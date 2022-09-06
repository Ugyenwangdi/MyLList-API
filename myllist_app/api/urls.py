from django.urls import path, include 
from rest_framework.routers import DefaultRouter


from myllist_app.api import views

router = DefaultRouter()
router.register('streams', views.StreamingPlatformVS, basename='streamplatform')
router.register('producers', views.ProductionCompanyVS, basename='productioncompany')
router.register('directors', views.DirectorVS, basename='director')
router.register('writers', views.WriterVS, basename='writer')
router.register('actors', views.ActorVS, basename='actor')
router.register('genres', views.GenreVS, basename='genre')
router.register('types', views.TypeVS, basename='type')
router.register('alternative_titles', views.TypeVS, basename='alternative_title')
router.register('showcharacters', views.ShowCharacterVS, basename='showcharacter')



urlpatterns = [
    path('', views.ShowAV.as_view(), name = 'show-list'),
    # path('<str:name>/', views.ShowAV.as_view(), name = 'show-list'),
    path('<int:pk>/', views.ShowDetailAV.as_view(), name='show-detail'),
    path('list2/', views.ShowGV.as_view(), name='movie-list'),

    path('', include(router.urls)),
    
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
  
    path('<int:pk>/reviews/create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    
    path('user-reviews/', views.UserReview.as_view(), name='user-review-detail'),
    
    
    # path('home/', views.Home, name='home'),
]