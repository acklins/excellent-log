from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews_index, name='reviews'),
    path('accounts/signup/', views.signup, name='signup'),
]
