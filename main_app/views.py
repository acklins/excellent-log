from django.conf import settings
from django.contrib import messages
from email_info import *
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import User, Product, Review, Profile
from .forms import ProfileForm, UserForm, ProfilePicForm

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'user/profile.html')

@login_required
def update_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user) 
    profile_pic_form = ProfilePicForm(request.POST or None, instance=profile)
    profile_form = ProfileForm(request.POST or None, instance=user)
    if request.POST and  profile_form.is_valid():
        profile_form.save()
        profile_pic_form.save()
        return redirect('profile')
    else:
        context = {
            'profile_form': profile_form,
            'profile_pic_form': profile_pic_form
            }
        return render(request, 'user/edit.html', context)

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product': product})

def reviews_index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.html', {'reviews': reviews})

def reviews_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'reviews/detail.html', {'review': review})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print('is valid')
            user = form.save()
            profile = Profile(user=user)
            profile.save()
            subject = 'Thank you for your request from La Boutique Log./n感谢您对La Boutique Log的要求 '
            message = 'Welcome to LBL! We appreciate your business./n欢迎来到LBL！我们感谢您的业务'
            from_email = 'belugadel6@gmail.com'
            to_list = [user.email]
            send_mail(subject, message, from_email,  to_list, fail_silently=True)
            login(request, user)
            return redirect('home') 
        else:
            print('is not valid')
            error_message = 'Invalid sign up - try again'
    form = UserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
