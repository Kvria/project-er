from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.home, name='home' ),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^post/new', views.post_new, name= 'new_post'),
    url(r'^search/', views.search_users, name='search_users'),
]