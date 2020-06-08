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
        p_form = ProfileUpdateForm(request.POST,instance=request.user)


        if p_form.is_valid():
            p.save()
            
            return render(request,'registration/profile.html')

    else:
        p_form = ProfileUpdateForm(instance=request.user)

    context = {'p_form': p_form}

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

def post_new(request):
    current_user = request.user
    if request.method == 'POST':
        form = Uploads(request.POST, request.FILES)
        if form.is_valid():
            user_img = form.save(commit=False)
            user_img.profile = current_user
            user_img.save()
        return redirect('home')
    else:
        form = Uploads()
    return render(request, "new_post.html", {"form": form})