from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from home.models import Category, Item
# Create your views here.

def home(request):
    return render(request,"home.html")

def feed(request):
    return render(request,"Feed_de_Produtos.html")

def perfil(request):
    return render(request, "perfil.html")

def test(request):
    number = 0
    namels=["bebel","caio","diogo"]
    return render(request, "test.html", {"namels":namels, "number": number})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error Loggin In, Try Again..."))
            return redirect('login')
    else:
        return render(request, "login.html")

def index(request):
    items = home.objects.filter(check_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'categories' : categories,
        'items': items,
    })