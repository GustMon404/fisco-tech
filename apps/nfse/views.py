from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views
from rest_framework.response import Response
from rest_framework import viewsets, serializers, status
from rest_framework.decorators import action

from apps.nfse.serializers.nse_serializers import NfseSerializer
from apps.nfse.models.nfse_model import NfseModel
from apps.nfse.services.nfse_service import autorizar


class NfseModelViewSet(viewsets.ModelViewSet):
    queryset = NfseModel.objects.all()
    serializer_class = NfseSerializer

    @action(detail=True, methods=['post'])
    def autorizar(self, request, pk):
        autorizar(pk)
        return Response({'message': 'ALGO'})
