from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def lol(request):
    return render(request, 'main/lol.html')

def about(request):
    return render(request, 'main/about.html')