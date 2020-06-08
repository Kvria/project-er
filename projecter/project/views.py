from django.shortcuts import render
from .models import Post,Profile,User
from django.contrib.auth.decorators import login_required.

# Create your views here.
@login_required(login_url = "accounts/login")
def home(request):
    posts = Post.objects.all()
    return render(request,'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    posts = Post.objects.all()
    profile = Profile.objects.all()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)


        if u_form.is_valid():
            u_form.save()
            
            return render(request,'registration/profile.html')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {'u_form': u_form}

    return render(request, 'registration/profile.html',locals())

