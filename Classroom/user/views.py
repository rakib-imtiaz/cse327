from django.shortcuts import render 
from django.http import HttpResponse

from .models import User 


# Create your views here.


def home(request):
    return render(request, 'home.html',{})

def about(request):
    return render(request, 'home.html',{})

def userProfile(request):
    return HttpResponse("this is the profile page ",{}) 

def user_detail_view(request):
    return render(request, 'user_detail.html')
    
