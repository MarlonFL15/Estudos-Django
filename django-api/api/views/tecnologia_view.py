from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import tecnologia_service
from ..entidades import tecnologia
from ..serializers import tecnlogia_serializer
from rest_framework import status

#Cria os métodos que NÃO precisam de parâmetro nenhum (listar tecnologias e cadastrar)
class TecnologiaList(APIView):
    def get(self, request, format=None):
        tecnologias = tecnologia_service.listar_tecnologias()
        serializer = tecnlogia_serializer.TecnologiaSerializer(tecnologias,many=True) #converte a lista de tecnologias com o serializer
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = tecnlogia_serializer.TecnologiaSerializer(data=request.data)

        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            novo_tecnologia = tecnologia.Tecnologia(nome = nome)
            tecnologia_bd = tecnologia_service.cadastrar_tecnologia(novo_tecnologia)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

class TecnologiaDetail(APIView):
    def get(self, request, id, format=None):
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        serializer = tecnlogia_serializer.TecnologiaSerializer(tecnologia)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        tecnologia_antiga = tecnologia_service.listar_tecnologia_id(id)
        serializer = tecnlogia_serializer.TecnologiaSerializer(tecnologia_antiga, data=request.data)

        if serializer.is_valid():

            nome = serializer.validated_data["nome"]
            tecnologia_novo = tecnologia.Tecnologia(nome = nome)
            tecnologia_service.editar_tecnologia(tecnologia_antiga, tecnologia_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        tecnologia_service.remover_tecnologia(tecnologia)
        return Response(status=status.HTTP_204_NO_CONTENT)
