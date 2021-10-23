from django.urls import path, include
from .views import tecnologia_view, vaga_view

urlpatterns = [
    path('tecnologias', tecnologia_view.TecnologiaList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>', tecnologia_view.TecnologiaDetail.as_view(), name='tecnologia-detail'),
    path('vagas', vaga_view.VagaList.as_view(), name='vaga-list'),
    path('vagas/<int:id>', vaga_view.VagaDetail.as_view(), name='vaga-detail'),
]
