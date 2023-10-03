"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    """Home VIEW"""
    return render(request,"users/index.html")

   
def  signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try whit other Username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")

        if  pass1 != pass2:
            messages.error(request,"Password didn't match!")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")       
            return redirect('home')
        

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Yoour account has been succesfully created.")

        return redirect('signin')

    return render(request, "users/signup.html")


def  signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username , password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "users/index.html", {'fname':fname})
        
        else:
            messages.error(request,"Bad credentials")
            return redirect('home')
        
        


    return render(request, "users/signin.html")

def  signout(request):
    logout(request)
    messages.success(request, "Logged Out Succesfully")
    return redirect('home')