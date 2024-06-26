from rest_framework import serializers

from drf_writable_nested import serializers as serializers_drf

from apps.nfse.models.nfse_model import *


class EnderecoExteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoExteriorModel
        exclude = ['id']


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoModel
        exclude = ['id']


class ValoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValoresModel
        exclude = ['id']


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoModel
        exclude = ['id']


class IntermediarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntermediarioModel
        exclude = ['id']


class TomadorSerializer(serializers_drf.WritableNestedModelSerializer):
    class Meta:
        model = TomadorModel
        exclude = ['id']

    endereco = EnderecoSerializer()
    endereco_exterior = EnderecoExteriorSerializer(required=False, allow_null=True)


class PrestadorSerializer(serializers_drf.WritableNestedModelSerializer):
    class Meta:
        model = PrestadorModel
        exclude = ['id']

    # endereco = EnderecoSerializer()


class RpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RpsModel
        exclude = ['id']


class InfoNfseSerializer(serializers_drf.WritableNestedModelSerializer):
    class Meta:
        model = InfoNFseModel
        read_only_fields = ['numero', 'codigo_verificao']
        exclude = ['id', 'nfse']
        extra_kwargs = {
            'nfse': {'required': False}
        }

    tomador = TomadorSerializer()
    intermediario = IntermediarioSerializer(required=False)
    rps = RpsSerializer()
    servico = ServicoSerializer()
    valores = ValoresSerializer()
    data_emissao = serializers.DateTimeField(read_only=True)


class NfseSerializer(serializers_drf.WritableNestedModelSerializer):

    prestador = PrestadorSerializer()
    infos = InfoNfseSerializer(many=True)

    class Meta:
        model = NfseModel
        fields = '__all__'
        read_only_fields = ['data_hora']

    # def create(self, validated_data):
    #     info_data = validated_data.pop('info')
    #     nfse = NfseModel.objects.create(**validated_data)
    #     for info in info_data:
    #         InfoNFseModel.objects.create(nfse=nfse, **info_data)
    #     return nfse

