from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'solarsprint/game.html', {})

def login(request):
    return render(request, 'solarsprint/login.html', {})
