from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .models import User, Product
from .forms import ProfileForm, UserForm


def home(request):
    return render(request, 'home.html')

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

def products_index(request):
    products = Product.objects.all()
    return render(request, 'reviews/index.html', {'products': products})

def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product': product})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        print(request.POST)
        
        form = UserForm(request.POST)
        print(form.errors)
        print(form)
        if form.is_valid():
          
            print('is valid')
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            print('is not valid')
            error_message = 'Invalid sign up - try again'
    form = UserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

#     class Product:
#     def __init__(self, name, photo, rating, editorial_review):
#         self.name = name
#         self.photo = photo
#         self.rating = rating
#         self.editorial_review = editorial_review

# product = [
#     Product('Xbox Wireless Headset', 'photo', 10, 'Able to play xbox while chatting'),
#     Product('Lexus LX Car', 'photo', 10, ' This car has a comfortable ride with a quiet,lavish & well-assembled cabin.'),
#     Product('DJI FPV drone', 'photo', 10, 'It is all about tight curves and speedy coverage'),
#     Product('Whoop Strap 3.0 fitness band', 'photo', 10, 'It has two LEDs that track sleep data, respiratory rate  & heart rate to measure strain and recovery.'),
#     Product('UV Phone Sanitizers', 'photo', 10, 'It fits your phone & other small items and eliminates up to 99.99 percent of bacteria.')
# ]

