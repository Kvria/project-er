from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.home, name='home' ),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^post/new', views.post_new, name= 'new_post'),
    url(r'^search/', views.search_users, name='search_users'),
    url(r'^search_project/', views.search_by_project_name, name='search_project'),
    # url(r'^api/project/$', views.ProjectList.as_view()),
    # url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
    #     views.ProjectDescription.as_view()),

]