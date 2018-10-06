# from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

def index(request):
    return render(request,'webapp/home.html')
def about(request):
    return render(request,'webapp/about.html')
def insights(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'webapp/insights.html',{'posts':posts})

def insights_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'webapp/insights_detail.html',{'post':post})

def insights_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('insights_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'webapp/insights_edit.html',{'form':form})