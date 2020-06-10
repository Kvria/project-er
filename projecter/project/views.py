from django.shortcuts import render, redirect
from .models import Post,Profile,User
from django.http import JsonResponse, HttpResponse,Http404,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer
from rest_framework import status
from django.contrib.auth.decorators import login_required
from .permissions import IsAdminOrReadOnly
from rest_framework import status
from .forms import ProfileUpdateForm, Uploads, Ratings


# Create your views here.
@login_required(login_url = "accounts/login")
def home(request):
    posts = Post.objects.all()
    return render(request,'index.html',{"posts":posts})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    posts = Post.objects.all()
    profile = Profile.objects.all()

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,instance=request.user)


        if p_form.is_valid():
            p_form.save()
            
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
        return redirect(home)
    else:
        form = Uploads()
    return render(request, "new_post.html", {"form": form})

def search_by_project_name(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_projects = Post.search_by_project_name(search_term)
        message = f"{search_term}"

        return render(request, '/search.html',{"message":message,"users": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def ratings(request,id):
    project = Post.get_project(id)
    current_user = request.user
    if request.method == 'POST':
        form = Ratings(request.POST)
        if form.is_valid():
            user_img = form.save(commit=False)
            user_img.profile = current_user.profile
            user_img.project = project
            user_img.save()
        return redirect (home)
    else:
        form = Ratings()
    return render(request, "ratings.html", {"form": form})

class Posts(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_project(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        all_projects = Post.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)