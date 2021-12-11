from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'home.html')

def userProfile(request):
    return HttpResponse("this is the profile page ") 