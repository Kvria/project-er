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