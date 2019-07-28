from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def logout(request):

    auth.logout(request)
    return redirect('/')

def login(request):

    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
                       
            return redirect('register')

    else:
        return render(request,'login.html')

def register(request):

    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("######  Username Taken  #########")
                return redirect('register')
            elif User.objects.filter(email=email).exists():

                print("######  Email Taken  #########")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print("######  User Created!!!  #########")
                return redirect('/')
        else:

            print("######  Password not matching  #########")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
