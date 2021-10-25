from ..models import *
from django.db import connection

def listar_posts():
    posts = Post.objects.all()
    return posts

def listar_post_id(id):
    post = Post.objects.get(id=id)
    return post
