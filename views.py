from django.shortcuts import render, redirect

# Create your views here.
from .models import Player_Male


def index(request):
    return render(request, 'main1.html')

def main1(request):
    return render(request, 'main1.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def announce(request):
    return render(request, 'announce.html')

def contactus(request):
    return render(request, 'contactus.html')

def register(request):
    return render(request, 'register.html')


def male(request):
    if request.method=='POST':
        first_name=request.POST['name1']
        last_name=request.POST['name2']
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['password']
        sports = request.POST['sports']

        ins=Player_Male(first_name=first_name,last_name=last_name,dob=dob,email=email,password=password,sports=sports)
        ins.save()
        print("user created")
        return redirect('/')








    else:
        return render(request, 'male.html')



def female(request):
    return render(request, 'female.html')