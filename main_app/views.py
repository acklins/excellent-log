from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User, Product, Review, Profile
from .forms import ProfileForm, UserForm, ProfilePicForm
# import Photo


def home(request):
    return render(request, 'home.html')#can I delete since review page is splash page

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'user/profile.html')

@login_required
def update_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile_form = ProfileForm(request.POST or None, instance=user)
    if request.POST and  profile_form.is_valid():
        profile_form.save()
        return redirect('profile')
    else:
        return render(request, 'user/edit.html', {'profile_form': profile_form})

    


#uploading the profile photo via Upload Care below from Upload Care documentation
# def profile_pic(request, profile_pic.id):
#     if request.method == "POST":
#         form = ProfilePicForm(request.POST) #PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#     else:
#         form = ProfilePicForm()

#     try:
#         posts = Post.objects.all()
#     except Post.DoesNotExist:
#         posts = None
#     return render(request, 'profile.html', {'posts': posts, 'form': form})
    

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product': product})

# below are the review functions
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
            #send_mail(subject, message, from_email, to_list, fail_silently=True)
            login(request, user)
            return redirect('home') 
        else:
            print('is not valid')
            error_message = 'Invalid sign up - try again'
    form = UserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# def send_email(request):
#     subject = request.POST.get('subject')