from django.urls import path
from. import views
urlpatterns = [
    path('', views.home, name="home"),
    path('home1', views.home1, name="home1"),
    path('contact',views.contact, name="contact"),
    path('loginn', views.handlelogin, name='handlelogin'),
    path('logoutt', views.handlelogin, name='handlelogout'),
    path('signupp', views.handlesignup, name='handlesignup'),
    path('upload', views.uploadimage, name="upload"),
]