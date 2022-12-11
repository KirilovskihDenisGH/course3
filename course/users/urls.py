from django.urls import path
from . import views

urlpatterns =[
    path('registration/', views.Signup.as_view(), name='registration'),
]