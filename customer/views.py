from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from management.models import *
from .models import *
import requests
import json
# Create your views here.

def Total(usr):
    products = Add_To_Cart.objects.filter(user=usr)
    total = 0
    for i in products:
        total += i.cloth.price * i.quantity
    return products,total    

def Home(request):
    if request.user.is_staff:
        return redirect('adminhome')
    latestArrival = Products.objects.filter(availability=True,latestArrival=True)
    bestSeller = Products.objects.filter(availability=True,bestSeller=True)
    d = {'latestArrival':latestArrival,'bestSeller':bestSeller}
    if request.user.is_authenticated:
        products,total = Total(request.user)
        d = {'latestArrival':latestArrival,'bestSeller':bestSeller,'products':products,'total':total}
    return render(request,'layout.html',d)

def Contact(request):
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('login')
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message'] 
        ContactUs.objects.create(name=name,email=email,subject=subject,message=message)
    return render(request,'contact.html')    

def Login(request):
    errorLogin = False
    if request.method == 'POST':
        un = request.POST['un']
        pwd = request.POST['pwd']
        user = authenticate(username=un,password=pwd)
        if user:
            login(request,user)
            return redirect('home')
        else:
            errorLogin = True
    d = {'errorLogin':errorLogin}        
    return render(request,'login.html',d)

def Logout(request):
    logout(request)
    return redirect('home')    

def Signup(request):
    errorPass = False
    errorUser = False
    errorEmail = False
    if request.method == 'POST':
        e = request.POST['email']
        ev = json.loads(requests.get('https://api.trumail.io/v2/lookups/json?email='+e).text)
        un = request.POST['un']
        pwd1 = request.POST['pwd']
        pwd2 = request.POST['pwd2']
        check = User.objects.filter(username = un)
        if (ev['validFormat'] is not True) or (ev['deliverable'] is not True):
            errorEmail = True
        elif pwd1 != pwd2:
            errorPass = True
        elif check:
            errorUser = True
        else:
            User.objects.create_user(username=un,email=e,password=pwd1,is_staff=False)
            user = authenticate(username=un,password=pwd1)
            login(request,user)
            return redirect('home')
    d = {'errorPass':errorPass,'errorUser':errorUser,'errorEmail':errorEmail}                
    return render(request,'signup.html',d)        

def Cart(request):
    products,total = Total(request.user)
    d = {'products':products,'total':total}
    return render(request,'cart.html',d)

def DeleteOrder(request,Oid):
    Add_To_Cart.objects.filter(id=Oid).delete()
    return redirect('cart')
