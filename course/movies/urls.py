from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPageView.as_view(), name='main'),
    path('movies/', views.moviePageView.as_view(), name='movies'),
    path('cartoons/', views.cartoonsPageView.as_view(), name='cartoons'),
    path('serials/', views.serialsPageView.as_view(), name='serials'),
    path('anime/', views.animePageView.as_view(), name='anime'),
    path('movie/<int:pk>/', views.movieDetailView.as_view(), name='detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('<int:pk>/edit', views.ReviewUpdateView.as_view(), name='review_edit'),
    path('<int:pk>/delete', views.ReviewDeleteView.as_view(), name='review_delete')
]