from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def index(request):
    # return HttpResponse('<h1>Nice job</h1>')
    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #Profile object for new user
                user_model = User.objects.get(username=username)
                new_user = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_user.save()
                return redirect('signup')
                
        
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')
