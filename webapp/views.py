from django.shortcuts import render
from .models import Post
from django.utils import timezone
# from django.shortcuts import render
from .forms import PostForm

def index(request):
    return render(request,'webapp/home.html')
def about(request):
    return render(request,'webapp/about.html')
def insights(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'webapp/insights.html',{'posts':posts})
# def post_list(request):
# def post_new(request):
