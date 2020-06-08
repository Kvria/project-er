from django.shortcuts import render
from .models import Post,Profile,User
from django.contrib.auth.decorators import login_required.

# Create your views here.
@login_required(login_url = "accounts/login")
def home(request):
    posts = Post.objects.all()
    return render(request,'index.html',{"images":images})

