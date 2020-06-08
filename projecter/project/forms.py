from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post,Profile,Rate,User

class SignupForm(UserCreationForm):
   email = forms.EmailField(max_length=200, help_text = 'Required')
   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic','bio']

class Uploads(forms.ModelForm):
    class Meta:
        model= Post
        exclude = ['profile','post_date']