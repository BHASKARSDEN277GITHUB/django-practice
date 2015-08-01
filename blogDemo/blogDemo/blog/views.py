from django.shortcuts import render , get_object_or_404
from blogDemo.blog.models import Post
# Create your views here.

def index(request): #for index page
	#get the blog posts that are published
	posts=Post.objects.filter(published=True)

	context={}
	#context['count']=count
	#now return the rendered template
	return render(request,'blog/index.html',{'posts':posts})

def post(request,slug):
	#get the Post object
	post=get_object_or_404(Post,slug=slug)
	#now return the rencered template
	return render(request,'blog/post.html',{'post':post})
