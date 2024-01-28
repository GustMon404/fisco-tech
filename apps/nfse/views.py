from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views
from rest_framework.response import Response
from rest_framework import viewsets

from apps.nfse.serializers.nse_serializers import NfseSerializer
from apps.nfse.models.nfse_model import NfseModel


# class NfseApiView(views.APIView):
#
#     def get(self, request):
#         teste = {
#             "teste": "asdasdasd"
#         }
#
#         return Response(teste)

def teste_view(request):
    pass


class NfseModelViewSet(viewsets.ModelViewSet):
    queryset = NfseModel.objects.all()
    serializer_class = NfseSerializer
