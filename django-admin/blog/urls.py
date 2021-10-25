from django.urls import path
from .views import *

urlpatterns = [
    path('posts', listar_posts, name='posts'),
    path('post/<int:id>',listar_post_id , name='post')
]