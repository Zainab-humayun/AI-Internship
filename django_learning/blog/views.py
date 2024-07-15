from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts =[
    {
        'author':'CoreyMS',
        'title':'Blog post 1',
        'content':'First post content',
        'date':'august 27 2023'
    },
    {
        'author':'jane',
        'title':'Blog post 2',
        'content':'Second post content',
        'date':'august 28 2023'
    },
]
def home(request):
    context ={
        'posts':posts
    }
    return render(request, 'blog/home.html',context) #way to pass info into template

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})