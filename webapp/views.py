from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    return render(request,'webapp/home.html')
def about(request):
    return render(request,'webapp/about.html')