import json
from dataclasses import field
from http.client import HTTPResponse

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core import models, serializers
from core.models import Lista, Mercado, Produto, Usuario
from core.serializers import ListaSerializer, MercadoSerializer, ProdutoSerializer


@method_decorator(csrf_exempt, name="dispatch")
class ListaViewSet(ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

    def get(self, request, id=None):
        if id: 
            qs= Lista.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
            data = list(Lista.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HTTPResponse(formatted_data, content_type="application/json")

    def post(self, request): 
        json_data = json.loads(request.data)
        nova_lista = Lista.objects.create(**json_data)
        data = {"id": nova_lista.id, "descricao": nova_lista.descricao}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Lista.objects.get(id=id)
        qs.descricao = json_data['descricao'] #if 'descricao' in json_data else qs.descricao#
        qs.save()
        data = {}
        data ['id'] = qs.id
        data['descricao']= qs.descricao
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Lista.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item excluido com sucesso"}

class ListaSerializer(ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'
        

class ListaList(APIView):
    def get(self, request):
        listas= Lista.objects.all
        serializer = ListaSerializer(listas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ListaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class ListaDetail(APIView):
    def get(self, request, id):
        lista = get_object_or_404(Lista.objects.all(), id=id)
        serializer = ListaSerializer(lista)
        return Response(serializer.data)

    def put(self, request, id):
        Lista = get_object_or_404(Lista.objects.all(), id=id)
        serializer = ListaSerializer(Lista, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        lista = get_object_or_404(Lista.objects.all(), id=id)
        lista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListasListGeneric(ListCreateAPIView):
    queryset= Lista.objects.all()
    serializer_class = ListaSerializer

class ListaDetailGeneric(RetrieveDestroyAPIView):
    lookup_field = 'id'
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

class MercadoViewSet(ModelViewSet):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer
  

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
   

@method_decorator(csrf_exempt, name="dispatch")
class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get(self, request, id=None):
        if id: 
            qs= Produto.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
            data = list(Produto.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HTTPResponse(formatted_data, content_type="application/json")

    def post(self, request): 
        json_data = json.loads(request.data)
        novo_produto = Produto.objects.create(**json_data)
        data = {"id": novo_produto.id, "nome": novo_produto.nome}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Produto.objects.get(id=id)
        qs.nome = json_data['nome'] #if 'descricao' in json_data else qs.descricao#
        qs.save()
        data = {}
        data ['id'] = qs.id
        data['nome']= qs.nome
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Produto.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item excluido com sucesso"}