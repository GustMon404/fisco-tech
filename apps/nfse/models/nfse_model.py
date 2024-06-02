from django.db import models

from apps.nfse.models.validators import validade_cpf_cnpj


class NfseModel(models.Model):
    class AMBIENTE(models.TextChoices):
        PRODUCAO = 'PD', 'Produção'
        HOMOLOGACAO = 'HM', 'Homologação'

    versao = models.CharField(max_length=20)
    ambiente = models.CharField(choices=AMBIENTE.choices, max_length=2)
    data_hora = models.DateTimeField(auto_now_add=True)

    # TODO: Adicionar UPPERCASE
    municipio_prefeitura = models.CharField(max_length=50)
    quem_lancou = models.CharField(max_length=30)

    prestador = models.OneToOneField('PrestadorModel', on_delete=models.CASCADE)

    class Meta:
        db_table = "nfse"


class InfoNFseModel(models.Model):
    class REGIME_TRIBUTACAO(models.IntegerChoices):
        MICROEMPRESA_MUNICIPAL = 1, 'Microempresa Municipal'
        ESTIMATIVA = 2, 'Estimativa'
        SOCIEDADE_PROFISSIONAIS = 3, 'Sociedade de Profissionais'
        COOPERATIVA = 4, 'Cooperativa'
        MEI = 5, 'Microempresário Individual (MEI)'
        MEI_EPP = 6, 'Microempresa ou Empresa de Pequeno Porte (ME EPP)'

    class OPTANTE_SIMPLES_NACIONAL(models.IntegerChoices):
        SIM = 1, 'SIM'
        NAO = 2, 'NÃO'

    class INCENTIVO_FISCAL(models.IntegerChoices):
        SIM = 1, 'SIM'
        NAO = 2, 'NÃO'

    nfse = models.ForeignKey('NfseModel', on_delete=models.CASCADE, related_name='infos')
    numero = models.IntegerField(null=True)
    codigo_verificao = models.CharField(max_length=9, null=True)
    nfse_substituida = models.IntegerField(null=True, unique=True)
    outras_informacoes = models.CharField(max_length=510, null=True)
    data_emissao = models.DateTimeField(null=True)
    competencia = models.DateField()
    regime_tributacao = models.IntegerField(choices=REGIME_TRIBUTACAO.choices, null=True)
    optante_simples_nacional = models.IntegerField(choices=OPTANTE_SIMPLES_NACIONAL.choices)
    incentivo_fiscal = models.IntegerField(choices=INCENTIVO_FISCAL.choices)
    tomador = models.OneToOneField('TomadorModel', on_delete=models.CASCADE)
    intermediario = models.OneToOneField('IntermediarioModel', null=True, on_delete=models.SET_NULL)
    construcao_civil = models.OneToOneField('ConstrucaoCivilModel', null=True, on_delete=models.SET_NULL)
    evento = models.OneToOneField('EventoModel', null=True, on_delete=models.SET_NULL)
    rps = models.OneToOneField('RpsModel', on_delete=models.CASCADE)
    servico = models.OneToOneField('ServicoModel', on_delete=models.CASCADE)
    valores = models.OneToOneField('ValoresModel', on_delete=models.CASCADE)

    class Meta:
        db_table = "nfse_info"


class EnderecoModel(models.Model):
    endereco = models.CharField(max_length=125)
    numero = models.CharField(max_length=60)
    complemento = models.CharField(max_length=60, null=True)
    bairro = models.CharField(max_length=60)
    codigo_municipio = models.CharField(max_length=7)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    class Meta:
        db_table = "nfse_endereco"


class EnderecoExteriorModel(models.Model):
    codigo_pais = models.IntegerField()
    endereco_completo_exterior = models.CharField(max_length=255)

    class Meta:
        db_table = "nfse_endereco_exterior"


class PrestadorModel(models.Model):
    nome_razao = models.CharField(max_length=150)
    nome_fantasia = models.CharField(max_length=60, null=True)
    cpf_cnpj = models.CharField(max_length=14, validators=[validade_cpf_cnpj])
    inscricao_muncipal = models.CharField(max_length=15, null=True)
    telefone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=80, null=True)
    # endereco = models.OneToOneField('EnderecoModel', on_delete=models.CASCADE)

    class Meta:
        db_table = "nfse_prestador"

    @property
    def cpf(self):
        return self.cpf_cnpj if len(self.cpf_cnpj) == 11 else ''

    @property
    def cnpj(self):
        return self.cpf_cnpj if len(self.cpf_cnpj) == 14 else ''


class TomadorModel(models.Model):
    razao_social = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=14, validators=[validade_cpf_cnpj])
    inscricao_muncipal = models.CharField(max_length=15, null=True)
    nif_tomador = models.CharField(max_length=40, null=True)
    telefone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=80, null=True)
    endereco = models.OneToOneField('EnderecoModel', on_delete=models.CASCADE)
    endereco_exterior = models.OneToOneField('EnderecoExteriorModel', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "nfse_tomador"

    @property
    def cpf(self):
        return self.cpf_cnpj if len(self.cpf_cnpj) == 11 else ''

    @property
    def cnpj(self):
        return self.cpf_cnpj if len(self.cpf_cnpj) == 14 else ''


class IntermediarioModel(models.Model):
    cpf_cnpj = models.CharField(max_length=14, null=True, validators=[validade_cpf_cnpj])
    inscricao_muncipal = models.CharField(max_length=15, null=True)
    razao_social = models.CharField(max_length=150, null=True)
    codigo_municipio = models.IntegerField(null=True)

    class Meta:
        db_table = "nfse_intermediario"

    @property
    def cpf(self):
        return self.cpf_cnpj if len(self.cpf_cnpj) == 11 else ''

    @property
    def cnpj(self):
        return self.cpf_cnpj if len(self.cpf_cnpj) == 14 else ''


class ConstrucaoCivilModel(models.Model):
    codigo_obra = models.CharField(max_length=30, null=True)
    art = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = "nfse_construcao_civil"


class EventoModel(models.Model):
    identificao = models.CharField(max_length=30, null=True)
    descricao = models.CharField(max_length=255, null=True)


    class Meta:
        db_table = "nfse_evento"

class RpsModel(models.Model):
    class TIPO(models.IntegerChoices):
        RECIBO_PROVISORIO_SERVICOS = 1, 'Recibo Provisório de Serviços'
        RPS_CONJUGADA = 2, 'RPS Nota Fiscal Conjugada (Mista)'
        CUPOM = 3, 'Cupom'

    class STATUS(models.IntegerChoices):
        NORMAL = 1, 'Normal'
        CANCELADO = 2, 'Cancelado'

    numero = models.IntegerField()
    serie = models.CharField(max_length=5, default='ÚNICA')
    tipo = models.IntegerField(choices=TIPO.choices)
    numero_substituido = models.IntegerField(null=True)
    serie_substituido = models.CharField(null=True, max_length=5)
    tipo_substituido = models.IntegerField(null=True, choices=TIPO.choices)
    data_emissao_rps = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS.choices)

    class Meta:
        db_table = "nfse_rps"


class ServicoModel(models.Model):
    class ISS(models.IntegerChoices):
        SIM = 1, 'Sim'
        NAO = 2, 'Não'

    class RESPONSAVEL_RETENCAO(models.IntegerChoices):
        TOMADOR = 1, 'Tomador'
        INTERMEDIARIO = 2, 'Intermediário'

    class EXIGIBILIDADE_ISS(models.IntegerChoices):
        EXIGIVEL = 1, 'Exígivel'
        NAO_INCIDENCIA = 2, 'Não Incidência'
        ISENCAO = 3, 'Isenção'
        EXPORTACAO = 4, 'Exportação'
        IMUNIDADE = 5, 'Imunidade'
        EXIGIBILIDADE_SUSPENSA_DESCISAO_JUDICIAL = 6, 'Exigibilidade Suspensa por Decisão Judicial'
        EXIGIBILIDADE_SUSPENSA_PROCESSO_ADMINISTRATIVO = 7, ' Exigibilidade Suspensa por Processo Administrativo'

    discriminacao = models.CharField(max_length=2000)
    iss_retido = models.IntegerField(choices=ISS.choices)
    responsavel_retencao = models.IntegerField(choices=RESPONSAVEL_RETENCAO.choices, null=True)
    item_lista_servico = models.CharField(max_length=5)
    codigo_cnae = models.IntegerField(null=True)
    codigo_tributacao_municipio = models.CharField(max_length=20, null=True)
    codigo_nbs = models.CharField(max_length=9, null=True)
    codigo_municipio = models.IntegerField()
    codigo_pais = models.IntegerField(null=True)
    exibilidade_iss = models.IntegerField(choices=EXIGIBILIDADE_ISS.choices)
    identificacao_nao_exigibilidade = models.CharField(max_length=4, null=True)
    municipio_incidencia = models.IntegerField(null=True)
    numero_processo = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = "nfse_servico"


class ValoresModel(models.Model):
    base_calculo = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    aliquota = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    valor_iss = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_liquido_nfse = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_servicos = models.DecimalField(max_digits=15, decimal_places=2)
    valor_deducoes = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_inss = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_ir = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_csll = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    outras_retencoes = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_total_tributos = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    valor_iss = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    aliquota_servico = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    desconto_incodicionado = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    desconto_condicionado = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    class Meta:
        db_table = "nfse_valores"


class FornecedorModel(models.Model):
    nif_forncedor = models.CharField(max_length=40, null=True)
    codigo_pais = models.CharField(max_length=4, null=True)
    cpf_cnpj = models.CharField(max_length=14, validators=[validade_cpf_cnpj])

    class Meta:
        db_table = "nfse_fornecedor"


class DeducaoModel(models.Model):
    class TipoDeducao(models.IntegerChoices):
        MATERIAIS = 1, 'Materiais'
        MAO_DE_OBRA = 2, 'Subempreitada de Mão de Obra'
        SERVICOS = 3, 'Serviços'
        PRODUCAO_EXTERNA = 4, 'Produção Externa'
        ALIMENTACAO = 5, 'Alimentação e Bebidas/Frigobar'
        REEMBOLSO = 6, 'Reembolso de Despesas'
        REPASSE_CONSORCIADO = 7, 'Repasse Consorciado'
        REPASSE_SAUDE = 8, 'Repasse Plano de Saúde'
        OUTRAS_DEDUCOES = 99, 'Outras Deduções'

    info_nfse = models.ForeignKey('InfoNFseModel', on_delete=models.CASCADE, related_name='deducoes')
    tipo_deducao = models.IntegerField(choices=TipoDeducao.choices)
    descricao_deducao = models.CharField(max_length=150, null=True)
    codigo_municipio_gerador = models.IntegerField(null=True)
    numero_nfse = models.IntegerField(null=True)
    codigo_verificacao = models.CharField(max_length=9, null=True)
    numero_nfe = models.IntegerField(null=True)
    chave_acesso_nfe = models.IntegerField(null=True)
    uf_nfe = models.CharField(max_length=2)
    identificacao_documento = models.CharField(max_length=255, null=True)
    fornecedor = models.ForeignKey(FornecedorModel, on_delete=models.CASCADE)
    data_emissao = models.DateField(auto_now_add=True)
    valor_dedutivel = models.DecimalField(max_digits=15, decimal_places=2)
    valor_utilizado_deducao = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = "nfse_deducao"
