from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return HttpResponse('We made it homey :-)')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' from an object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A GET or a bad POST request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
