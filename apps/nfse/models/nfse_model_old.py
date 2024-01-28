# from django.db import models
#
#
# class NfseModel(models.Model):
#     info_nfse = models.ForeignKey('InfNfseModel', on_delete=models.CASCADE)
#
#
# class InfNfseModel(models.Model):
#     numero = models.IntegerField()
#     codigo_verificacao = models.CharField(max_length=8)
#
#     # TODO: Adicionar Formatador de DATA E HORA (AAAA-MM-DDTHH:mm:ss)
#     data_emissao = models.DateTimeField()
#     nfse_substituida = models.IntegerField(null=True, unique=True)
#     outras_informacoes = models.CharField(max_length=510, null=True)
#     valores_nfse = models.ForeignKey('ValoresNfseModel', on_delete=models.CASCADE)
#     descricao_codigo_tributacao_municipal = models.CharField(max_length=1000, null=True)
#     valor_credito = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#     prestador_servico = models.ForeignKey('PrestadorServicoModel', on_delete=models.CASCADE)
#     orgao_gerador = models.ForeignKey('OrgaoGeradorModel', on_delete=models.CASCADE)
#     declaracao_prestacao_servico = models.ForeignKey('DeclaracaoPrestacaoServicoModel', on_delete=models.CASCADE)
#
#
# class ValoresNfseModel(models.Model):
#     base_calculo = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     aliquota = models.DecimalField(max_digits=4, decimal_places=2, null=True)
#     valor_iss = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     valor_liquido_nfse = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#
#
# class PrestadorServicoModel(models.Model):
#     dados_prestador = models.ForeignKey('DadosPrestadorModel', on_delete=models.CASCADE)
#     endereco = models.ForeignKey('EnderecoModel', on_delete=models.CASCADE)
#     contato = models.ForeignKey('ContatoModel', on_delete=models.CASCADE, null=True)
#
#
# class DadosPrestadorModel(models.Model):
#     nome_razao = models.CharField(max_length=150)
#     nome_fantasia = models.CharField(max_length=60, null=True)
#
#
# class EnderecoModel(models.Model):
#     endereco = models.CharField(max_length=125)
#     numero = models.CharField(max_length=60)
#     complemento = models.CharField(max_length=60, null=True)
#     bairro = models.CharField(max_length=60)
#     codigo_municipio = models.CharField(max_length=7)
#     uf = models.CharField(max_length=2)
#     cep = models.CharField(max_length=8)
#
#
# class ContatoModel(models.Model):
#     telefone = models.CharField(max_length=20, null=True)
#     email = models.CharField(max_length=80, null=True)
#
#
# class OrgaoGeradorModel(models.Model):
#     codigo_municipio = models.CharField(max_length=7)
#     uf = models.CharField(max_length=2)
#
#
# class DeclaracaoPrestacaoServicoModel(models.Model):
#     inf_declaracao_prestaco_servico = models.ForeignKey('InfDeclaracaoPrestacaoServicoModel',
#                                                         on_delete=models.CASCADE)
#
#
# class InfDeclaracaoPrestacaoServicoModel(models.Model):
#     class REGIME_TRIBUTACAO(models.IntegerChoices):
#         MICROEMPRESA_MUNICIPAL = 1, 'Microempresa municipal'
#         ESTIMATIVA = 2, 'Estimativa'
#         SOCIEDADE_PROFISSIONAIS = 3, 'Sociedade de Profissionais'
#         COOPERATIVA = 4, 'Cooperativa'
#         MEI = 5, 'Microempresário Individual (MEI)'
#         MEI_EPP = 6, 'Microempresa ou Empresa de Pequeno Porte (ME EPP)'
#
#     class OPTANTE_SIMPLES_NACIONAL(models.IntegerChoices):
#         SIM = 1, 'SIM'
#         NAO = 2, 'NÃO'
#
#     class INCENTIVO_FISCAL(models.IntegerChoices):
#         SIM = 1, 'SIM'
#         NAO = 2, 'NÃO'
#
#     rps = models.ForeignKey('RpsModel', on_delete=models.CASCADE)
#     competencia = models.DateField()
#     servicos = models.ForeignKey('ServicoModel', on_delete=models.CASCADE)
#     prestador = models.ForeignKey('PrestadorModel', on_delete=models.CASCADE)
#     intermediario = models.ForeignKey('IntermediarioModel', on_delete=models.SET_NULL, null=True)
#     construcao_civil = models.ForeignKey('ConstrucaoCivil', on_delete=models.SET_NULL, null=True)
#     regime_tributacao = models.IntegerField(choices=REGIME_TRIBUTACAO.choices, null=True)
#     optante_simples_nacional = models.IntegerField(choices=OPTANTE_SIMPLES_NACIONAL.choices)
#     incentivo_fiscal = models.IntegerField(choices=INCENTIVO_FISCAL.choices)
#     evento = models.ForeignKey('EventoModel', on_delete=models.SET_NULL, null=True)
#
#
# class RpsModel(models.Model):
#     class STATUS(models.IntegerChoices):
#         NORMAL = 1, 'Normal'
#         CANCELADO = 2, 'Cancelado'
#
#     identificacao_rps = models.ForeignKey('IdentificacaoRpsModel', on_delete=models.SET_NULL, null=True)
#     data_emissao_rps = models.DateField()
#     status = models.IntegerField(choices=STATUS.choices)
#     rps_substituido = models.ForeignKey('RpsSubstituidoModel', on_delete=models.SET_NULL, null=True)
#
#
# class IdentificacaoRpsModel(models.Model):
#     class TIPO(models.IntegerChoices):
#         RECIBO_PROVISORIO_SERVICOS = 1, 'Recibo Provisório de Serviços'
#         RPS_CONJUGADA = 2, 'RPS Nota Fiscal Conjugada (Mista)'
#         CUPOM = 3, 'Cupom'
#
#     numero = models.IntegerField()
#     serie = models.CharField(max_length=5)
#     tipo = models.IntegerField(choices=TIPO.choices)
#
#
# class RpsSubstituidoModel(models.Model):
#     class TIPO(models.IntegerChoices):
#         RECIBO_PROVISORIO_SERVICOS = 1, 'Recibo Provisório de Serviços'
#         RPS_CONJUGADA = 2, 'RPS Nota Fiscal Conjugada (Mista)'
#         CUPOM = 3, 'Cupom'
#
#     numero = models.IntegerField()
#     serie = models.CharField(max_length=5)
#     tipo = models.IntegerField(choices=TIPO.choices)
#
#
# class ServicoModel(models.Model):
#     class ISS(models.IntegerChoices):
#         SIM = 1, 'Sim'
#         NAO = 2, 'Não'
#
#     class RESPONSAVEL_RETENCAO(models.IntegerChoices):
#         TOMADOR = 1, 'Tomador'
#         INTERMEDIARIO = 2, 'Intermediário'
#
#     class EXIGIBILIDADE_ISS(models.IntegerChoices):
#         EXIGIVEL = 1, 'Exígivel'
#         NAO_INCIDENCIA = 2, 'Não Incidência'
#         ISENCAO = 3, 'Isenção'
#         EXPORTACAO = 4, 'Exportação'
#         IMUNIDADE = 5, 'Imunidade'
#         EXIGIBILIDADE_SUSPENSA_DESCISAO_JUDICIAL = 6, 'Exigibilidade Suspensa por Decisão Judicial'
#         EXIGIBILIDADE_SUSPENSA_PROCESSO_ADMINISTRATIVO = 7, ' Exigibilidade Suspensa por Processo Administrativo'
#
#     valores = models.ForeignKey('ValoresModel', on_delete=models.CASCADE)
#     iss_retido = models.IntegerField(choices=ISS.choices)
#     responsavel_retencao = models.IntegerField(choices=RESPONSAVEL_RETENCAO.choices, null=True)
#     item_lista_servico = models.CharField(max_length=5)
#     codigo_cnae = models.IntegerField(null=True)
#     codigo_tributacao_municipio = models.CharField(max_length=20, null=True)
#     codigo_nbs = models.CharField(max_length=9, null=True)
#     discriminacao = models.CharField(max_length=2000)
#     codigo_municipio = models.IntegerField()
#     codigo_pais = models.IntegerField(null=True)
#     exibilidade_iss = models.IntegerField(choices=EXIGIBILIDADE_ISS.choices)
#     identificacao_nao_exigibilidade = models.CharField(max_length=4, null=True)
#     municipio_incidencia = models.IntegerField(null=True)
#     numero_processo = models.CharField(max_length=30, null=True)
#
#
# class ValoresModel(models.Model):
#     valor_servicos = models.DecimalField(max_digits=15, decimal_places=2)
#     valor_deducoes = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     valor_pis = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     valor_cofins = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     valor_inss = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     valor_ir = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     valor_csll = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     outras_retencoes = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     valor_total_tributos = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     valor_iss = models.DecimalField(max_digits=15, decimal_places=2, null=True)
#     aliquota = models.DecimalField(max_digits=4, decimal_places=2, null=True)
#     desconto_incodicionado = models.DecimalField(max_digits=4, decimal_places=2, null=True)
#     desconto_condicionado = models.DecimalField(max_digits=4, decimal_places=2, null=True)
#
#
# class PrestadorModel(models.Model):
#     cpf_cnpj = models.ForeignKey('CpfCnpjModel', on_delete=models.CASCADE)
#     inscricao_muncipal = models.CharField(max_length=15, null=True)
#
#
# class CpfCnpjModel(models.Model):
#     # TODO:  Adicionar constrain para o cnpj e cpf, um ou outro tem que estar prenchido
#     cpf = models.CharField(max_length=11, null=True)
#     cnpj = models.CharField(max_length=14, null=True)
#
#
# class TomadorServicoModel(models.Model):
#     identificao_tomador = models.ForeignKey('IdentificacaoTomadorModel', on_delete=models.CASCADE)
#     nif_tomador = models.CharField(max_length=40, null=True)
#     razao_social = models.CharField(max_length=150)
#
#     # TODO: Adicionar constrain para os endereços, endereco ou endereco_exteiriror tem que estar prenchido
#     endereco = models.ForeignKey('EnderecoModel', on_delete=models.SET_NULL, null=True)
#     endereco_exterior = models.ForeignKey('EnderecoExteriorModel', on_delete=models.SET_NULL, null=True)
#     contato = models.ForeignKey('ContatoModel', on_delete=models.SET_NULL, null=True)
#
#
# class IdentificacaoTomadorModel(models.Model):
#     cpf_cnpj = models.ForeignKey('CpfCnpjModel', on_delete=models.CASCADE)
#     inscricao_municipal = models.CharField(max_length=14, null=True)
#
#
# class EnderecoExteriorModel(models.Model):
#     codigo_pais = models.IntegerField()
#     endereco_completo_exterior = models.CharField(max_length=255)
#
#
# class IntermediarioModel(models.Model):
#     identificacao_intermediario = models.ForeignKey('IdentificacaoIntermediarioModel', on_delete=models.SET_NULL,
#                                                     null=True)
#     razao_social = models.CharField(max_length=150, null=True)
#     codigo_municipio = models.IntegerField(null=True)
#
#
# class IdentificacaoIntermediarioModel(models.Model):
#     cpf_cnpj = models.ForeignKey('CpfCnpjModel', on_delete=models.CASCADE)
#     inscricao_municipal = models.CharField(max_length=15, null=True)
#
#
# # DETALHAMENTO ESPECÍFICO DE OBRA DE ENGENHARIA E ARQUITETURA EM GERAL
# class ConstrucaoCivil(models.Model):
#     codigo_obra = models.CharField(max_length=30, null=True)
#     art = models.CharField(max_length=30, null=True)
#
#
# class EventoModel(models.Model):
#     identificacao_evento = models.CharField(max_length=30, null=True)
#     descricao_evento = models.CharField(max_length=255, null=True)
#     informacoes_comlementares = models.CharField(max_length=2000, null=True)
#
#
# class DeducaoModel(models.Model):
#     pass