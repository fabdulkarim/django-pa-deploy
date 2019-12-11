from django.urls import path
from . import views

app_name = 'viewmodeltemplate'
urlpatterns = [
    path('blog', views.blog , name='blog'),
    path('mentor', views.mentor , name='mentor'),
    path('mentee/', views.mentee , name='mentee'),
    path('blog/<int:blog_id>', views.blogpost , name='blogpost'),
    path('blog/input', views.blog_input , name='blog_input'),
    path('submit', views.blogsubmit , name='blogsubmit')
]
