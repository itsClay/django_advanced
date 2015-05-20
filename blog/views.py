from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm (normally this is used before we customize this)
from blog.forms import EmailUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'base_template.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {})

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {'form': form})

def angular(request):
    return render(request, 'angular/angular.html', {})