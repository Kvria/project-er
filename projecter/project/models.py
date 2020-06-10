from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    project_name = models.CharField(max_length = 500)
    description = models.CharField(max_length = 500)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    project_url = models.URLField()
    objects = models.Manager()
    
    def __str__(self):
       return self.project_name

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search_by_project_name(cls,search_term):
        projects = Post.objects.filter(project_name__icontains=search_term)
        return projects

    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)

    @classmethod
    def get_project(cls,id):
        return cls.objects.get(id=id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length = 300)
    contacts = models.CharField(max_length = 250)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_by_user(cls,search_term):
        users = User.objects.filter(username__icontains=search_term)
        return users

@receiver(post_save, sender = User)
def create_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_profile( sender, instance, **kwargs):
    instance.profile.save()

class Rate(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    design = models.IntegerField()
    usability =models.IntegerField()
    content = models.IntegerField()
    objects = models.Manager()

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def get_ratings_on_image(cls, id):
        the_ratings = Rate.objects.filter(image__pk=id)
        return the_ratings
    
    