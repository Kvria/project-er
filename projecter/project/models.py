from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length = 500)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
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

    @classmethod
    def search_by_user(cls,search_term):
        users = User.objects.filter(username__icontains=search_term)
        return users