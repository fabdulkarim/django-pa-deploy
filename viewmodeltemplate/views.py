from django.shortcuts import render, redirect
from .models import Blog, Mentor, Mentee 
# Create your views here.

def blog(request):
    blog_object = Blog.objects.all()
    return render(request, 'viewmodeltemplate/blog.html', {
        'blog_object': blog_object
    })

def mentor(request):
    mentor_obj = Mentor.objects.all()
    return render(request, 'viewmodeltemplate/mentor.html', {
        'mentor_obj': mentor_obj,
    })

def mentee(request):
    print("akumasuk")
    mentees = Mentee.objects.all()
    return render(request, 'viewmodeltemplate/mentee.html', {
        'mentees': mentees,
    })

def blogpost(request, blog_id):
    blogpost_obj = Blog.objects.get(pk=blog_id)
    return render(request, 'viewmodeltemplate/blogpost.html',{
        'blogpost_obj': blogpost_obj,
    })

def blog_input(request):
    return render(request, 'viewmodeltemplate/blog_input.html',{})

def blogsubmit(request):
    image = request.POST['image']
    title = request.POST['title']
    content = request.POST['content']

    Blog(image=image,title=title,content=content).save()

    blog_object = Blog.objects.all()
    return redirect('/blog')



