from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.reviews_index, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/edit/', views.update_profile, name='update_profile'),

    # path('profile_pic/<int:profile_pic_id>/edit/', views.update_profile_pic, name='update_profile_pic'),
    
    path('products/', views.products_index, name='index'),
    path('products/<int:product_id>/', views.products_detail, name='detail'),

    path('reviews/', views.reviews_index, name='index'),
    path('reviews/<int:review_id>/', views.reviews_detail, name='detail'),

    path('accounts/signup/', views.signup, name='signup'),
]
