from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('UserProfile/',views.userProfile),
    path('about/',views.about),
    
  
] 
