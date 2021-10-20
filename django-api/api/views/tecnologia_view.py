from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import tecnologia_service
from ..serializers import tecnlogia_serializer
from rest_framework import status

#Cria os métodos que NÃO precisam de parâmetro nenhum (listar tecnologias e cadastrar)
class TecnologiaList(APIView):
    def get(self, request, format=None):
        tecnologias = tecnologia_service.listar_tecnologias()
        serializer = tecnlogia_serializer.TecnologiaSerializer(tecnologias,many=True) #converte a lista de tecnologias com o serializer
        return Response(serializer.data, status.HTTP_200_OK)