from django.shortcuts import render
from forms import UserProfileForm

# Create your views here.

def index(request):
    return render(request, 'advanced_tactics/index.html')

def user_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'advanced_tactics/index.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserProfileForm()

    return render(request, 'advanced_tactics/index.html', {'form': form})