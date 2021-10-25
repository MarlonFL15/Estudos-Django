from django.contrib import admin
from .models import *
# Register your models here.

#Define que quando ele mostrar a tela do autor, embaixo ele vai mostrar os posts do autor (em formato de tabela)
#class PostInline(admin.TabularInline):
#    model = Post

#Define que quando ele mostrar a tela do autor, embaixo ele vai mostrar os posts do autor (em formato de pilha)
class PostStacked(admin.StackedInline):
    model = Post

class AutorAdmin(admin.ModelAdmin):
    inlines = (PostStacked, )

class PostAdmin(admin.ModelAdmin):
    list_filter = ['autor', 'data_cadastro']

admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AutorAdmin)