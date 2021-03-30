from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, Imageform
from .models import Imageloader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def home(request):
    return render(request,'img/home.html')
def contact(request):
    return render(request, 'img/contact.html')
def handlelogin(request):
    Imageloader.objects.all().delete()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'img/home1.html')
        else:
            messages.info(request, 'username or passowrd is incorrect')
            return render(request, 'img/loginn.html')

    return render(request, 'img/loginn.html')
def home1(request):
    Imageloader.objects.all().delete()
    content = {}
    return render(request,'img/home1.html' ,content)
def handlelogout(request):
    Imageloader.objects.all().delete()
    logout(request)
    return redirect('handlelogin')
def handlesignup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username') 
            messages.success(request,'Account has been created for ' + user)
            return redirect('handlelogin')
    content = { 'form':form } 
    # next_page = redirect('home1')
    return render(request, 'img/signupp.html', content) 
def uploadimage(request):
    if request.method == "POST":
        f = Imageform(request.POST, request.FILES)
        if f.is_valid():
            f.save()    
    f = Imageform()
    i = Imageloader.objects.all()
    return render(request, 'img/upload.html', {'i':i,'f':f})
