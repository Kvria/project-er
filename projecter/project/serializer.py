from rest_framework import serializers
from .models import Post

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'project_name', 'project_description', 'image')