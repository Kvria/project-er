from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import RatingField


# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length = 500)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.image

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length = 300)
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

class Rate(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='rate')
    design = models.RatingField(range=10)
    usability =models.RatingField(range=10)
    content = models.RatingField(range=10)
    objects = models.Manager()

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def get_comments_on_image(cls, id):
        the_comments = Comment.objects.filter(image__pk=id)
        return the_comments
   