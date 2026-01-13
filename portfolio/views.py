from django.shortcuts import render

# Create your views here.from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def gallery(request):
    return render(request, 'portfolio/gallery.html')

