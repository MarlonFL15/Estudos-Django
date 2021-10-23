from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import usuario_serializer

class UsuarioList(APIView):
    #permission_classes = [IsAuthenticated] #notação que define que esse método precisa de autenticação
    permission_classes = [AllowAny] #qualquer usuário pode acessar esse método, independente de ter token de acesso ou não
    def post(self, request, format=None):
        serializer = usuario_serializer.UsuarioSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

