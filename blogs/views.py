from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from .models import *
from django.contrib import messages


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def blogdetail(request):
    return render(request, "blog-detail.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def privacypolicy(request):
    return render(request, "privacypolicy.html")

def termsofconditions(request):
    return render(request, "termsofconditions.html")

def faq(request):
    return render(request, "faqs.html")

def dashboard(request):
    
    return render(request, "dashboard.html")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('signin')
        else:
            messages.error(request, 'Username or Pasword not Correct')
            return render(request, "signup.html", {"form": form})
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})
    

def signin(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not CustomUser.objects.filter(username = username).exists():
            messages.error(request, 'Username or Pasword not Correct')
            return render(request , 'signin.html', {'form':form})
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return render(request , 'signin.html', {'form':form})
        
        else:
            login(request, user)
            return render(request, "dashboard.html")
    form = CustomAuthenticationForm()
    return render(request , 'signin.html', {'form':form})
    
def signout(request):
    logout(request)
    return redirect('signin')    