from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    return render(request, 'advanced_tactics/index.html')