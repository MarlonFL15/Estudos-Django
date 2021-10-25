from django.shortcuts import render
from .services import post_service

# Create your views here.
def listar_posts(request):
    posts = post_service.listar_posts()
    return render(request, 'posts.html', {
        'posts':posts
    })

def listar_post_id(request, id):
    post = post_service.listar_post_id(id)
    return render(request, 'post.html', {
        'post':post
    })