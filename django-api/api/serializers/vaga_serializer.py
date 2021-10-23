from rest_framework import serializers
from rest_framework.reverse import reverse

from ..models import Vaga

#Determina como as classes serão exibidas e valida os dados enviados

class VagaSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Vaga
        fields = ('id', 'titulo', 'descricao', 'salario', 'local', 'quantidade', 'contato', 'tipo_contratacao',
                  'tecnologias', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('vaga-detail', kwargs={'id': obj.pk}, request=request),
            'delete': reverse('vaga-detail', kwargs={'id': obj.pk}, request=request),
            'update': reverse('vaga-detail', kwargs={'id': obj.pk}, request=request)
        }