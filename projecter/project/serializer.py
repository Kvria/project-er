from rest_framework import serializers
from .models import Post

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('project_name', 'project_description', 'project_image')