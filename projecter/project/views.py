from django.shortcuts import render, redirect
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

def search_users(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_users = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, '/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
