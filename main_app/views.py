from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('We made it homey :-)')

def profile(request):
    return render(request, 'profile.html')
