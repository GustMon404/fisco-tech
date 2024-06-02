# from collections import OrderedDict
# from datetime import datetime
#
# from dicttoxml2 import dicttoxml
# from xml.dom.minidom import parseString
# from django.db.models import QuerySet
#
# from apps.nfse.models.nfse_model import NfseModel
# from apps.nfse.services.Nfse import LoteRps, Rps
#
# class EnviarLoteRpsSincronoEnvio:
#     LoteRps: LoteRps = LoteRps()
#
#     def _gera_rps(self, nfse: NfseModel) -> Rps:
#         servico = Rps()
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.IdentificacaoRps.Numero = nfse.info.rps.numero
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.IdentificacaoRps.Serie = nfse.info.rps.serie
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.IdentificacaoRps.Tipo = nfse.info.rps.serie
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.IdentificacaoRps.Tipo = nfse.info.rps.serie
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.DataEmissao = datetime.strftime(nfse.info.rps.data_emissao_rps, '%Y-%m-%d')
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.Status = nfse.info.rps.status
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.RpsSubstituido.Numero = nfse.info.rps.numero_substituido
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.RpsSubstituido.Serie = nfse.info.rps.serie_substituido
#         servico.Rps.InfDeclaracaoPrestacaoServico.Rps.RpsSubstituido.Tipo = nfse.info.rps.tipo_substituido
#         servico.Rps.InfDeclaracaoPrestacaoServico.Competencia = datetime.strftime(nfse.info.competencia, '%Y-%m-%d')
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValorServicos = nfse.info.valores.valor_servicos
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValorDeducoes = nfse.info.valores.valor_deducoes
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValorPis = nfse.info.valores.valor_pis
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValorCofins = nfse.info.valores.valor_cofins
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValorInss = nfse.info.valores.valor_inss
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValorIr = nfse.info.valores.valor_ir
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValorCsll = nfse.info.valores.valor_csll
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.OutrasRetencoes = nfse.info.valores.outras_retencoes
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValTotTributos = nfse.info.valores.valor_total_tributos
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.ValorIss = nfse.info.valores.valor_iss
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.Aliquota = nfse.info.valores.aliquota
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.DescontoIncondicionado = nfse.info.valores.desconto_incodicionado
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Valores.DescontoCondicionado = nfse.info.valores.desconto_condicionado
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.IssRetido = nfse.info.servico.iss_retido
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.ResponsavelRetencao = nfse.info.servico.responsavel_retencao
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.ItemListaServico = nfse.info.servico.item_lista_servico
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.CodigoCnae = nfse.info.servico.codigo_cnae
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.CodigoTributacaoMunicipio = nfse.info.servico.codigo_tributacao_municipio
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.CodigoNbs = nfse.info.servico.codigo_nbs
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.Discriminacao = nfse.info.servico.discriminacao
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.CodigoMunicipio = nfse.info.servico.codigo_municipio
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.CodigoPais = nfse.info.servico.codigo_pais
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.ExigibilidadeISS = nfse.info.servico.exibilidade_iss
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.IdentifNaoExigibilidade = nfse.info.servico.identificacao_nao_exigibilidade
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.MunicipioIncidencia = nfse.info.servico.municipio_incidencia
#         servico.Rps.InfDeclaracaoPrestacaoServico.Servico.NumeroProcesso = nfse.info.servico.numero_processo
#         servico.Rps.InfDeclaracaoPrestacaoServico.Prestador.CpfCnpj.Cpf = nfse.info.prestador.cpf
#         servico.Rps.InfDeclaracaoPrestacaoServico.Prestador.CpfCnpj.Cnpj = nfse.info.prestador.cnpj
#         servico.Rps.InfDeclaracaoPrestacaoServico.Prestador.InscricaoMunicipal = nfse.info.prestador.inscricao_muncipal
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.IdentificacaoTomador.CpfCnpj.Cpf = nfse.info.tomador.cpf
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.IdentificacaoTomador.CpfCnpj.Cnpj = nfse.info.tomador.cnpj
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.IdentificacaoTomador.InscricaoMunicipal = nfse.info.tomador.inscricao_muncipal
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.NifTomador = nfse.info.tomador.nif_tomador
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.RazaoSocial = nfse.info.tomador.razao_social
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Endereco.Endereco = nfse.info.tomador.endereco.endereco,
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Endereco.Numero = nfse.info.tomador.endereco.numero,
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Endereco.Complemento = nfse.info.tomador.endereco.complemento,
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Endereco.Bairro = nfse.info.tomador.endereco.bairro,
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Endereco.CodigoMunicipio = nfse.info.tomador.endereco.codigo_municipio,
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Endereco.Uf = nfse.info.tomador.endereco.uf,
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Endereco.Cep = nfse.info.tomador.endereco.cep
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Endereco.Cep = nfse.info.tomador.endereco.cep
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.EnderecoExterior.EnderecoCompletoExterior = nfse.info.tomador.endereco_exterior.endereco_completo_exterior
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.EnderecoExterior.CodigoPais = nfse.info.tomador.endereco_exterior.endereco_completo_exterior
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Contato.Telefone = nfse.info.tomador.telefone
#         servico.Rps.InfDeclaracaoPrestacaoServico.TomadorServico.Contato.Email = nfse.info.tomador.email
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.CpfCnpj.Cpf = nfse.info.prestador.cpf
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.CpfCnpj.Cnpj = nfse.info.prestador.cnpj
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.InscricaoMunicipal = nfse.info.prestador.inscricao_muncipal
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.RazaoSocial = nfse.info.prestador.inscricao_muncipal
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.CodigoMunicipio = nfse.info.prestador.inscricao_muncipal
#
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.CodigoMunicipio = nfse.info.prestador.inscricao_muncipal
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.CodigoMunicipio = nfse.info.prestador.inscricao_muncipal
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.CodigoMunicipio = nfse.info.prestador.inscricao_muncipal
#         servico.Rps.InfDeclaracaoPrestacaoServico.Intermediario.IdentificacaoIntermediario.CodigoMunicipio = nfse.info.prestador.inscricao_muncipal
#
#
#
#
#
#
#
#     def build(self, lista_nfse: QuerySet[NfseModel], numero_lote: int, inscricao_municipal: int, cpf: int = None, cnpj: int = None):
#         self.LoteRps.NumeroLote = numero_lote
#         if cpf:
#             self.LoteRps.Prestador.CpfCnpj.Cpf = cpf
#         else:
#             self.LoteRps.Prestador.CpfCnpj.Cnpj = cnpj
#         self.LoteRps.Prestador.InscricaoMunicipal = inscricao_municipal
#         self.LoteRps.QuantidadeRps = lista_nfse.count()
#
#         if lista_nfse.count() > 1:
#             for nfse in lista_nfse:
#                 self.LoteRps.ListaRps.append(self._gera_rps(nfse))
#         else:
#             self.LoteRps.Rps = self._gera_rps(lista_nfse.first())
#
#
#
# class NfseAbrasfXML:
#     def __init__(self):
#         # self.nfse = nfse
#         self.nfse_dict = {}
#
#     def gerar_lote_rps_dict(self, numero_lote: int, inscricao_municipal: int, cpf: int = None, cnpj: int = None):
#         self.nfse_dict = OrderedDict({
#             "LoteRps": {  # tcLoteRps
#                 "NumeroLote": numero_lote,
#                 "Prestador": {  # tcIdentificacaoPessoaEmpresa
#                     "CpfCnpj": {  # tcCpfCnpj
#                         "Cpf": cpf,
#                         "Cnpj": cnpj
#                     },
#                     "InscricaoMunicipal": inscricao_municipal
#                 },
#                 "QuantidadeRps": 0,
#                 "ListaRps": [],
#                 "versao": ""
#             }
#         })
#
#     def gerar_rps_dict(self, nfse: NfseModel):
#         return OrderedDict({
#             "Rps": {  # tcDeclaracaoPrestacaoServico
#                 "InfDeclaracaoPrestacaoServico": {  # tcInfDeclaracaoPrestacaoServico
#                     "Rps": {  # tcInfRps
#                         "IdentificacaoRps": {  # tcIdentificacaoRps
#                             "Numero": nfse.info.rps.numero,
#                             "Serie": nfse.info.rps.serie,
#                             "Tipo": nfse.info.rps.tipo
#                         },
#                         "DataEmissao": str(nfse.info.rps.data_emissao_rps),
#                         "Status": nfse.info.rps.status,
#                         "RpsSubstituido": {  # tcIdentificacaoRps
#                             "Numero": nfse.info.rps.numero_substituido,
#                             "Serie": nfse.info.rps.serie_substituido,
#                             "Tipo": nfse.info.rps.tipo_substituido
#                         },
#                         "Id": ""
#                     },
#                     "Competencia": str(nfse.info.competencia),
#                     "Servico": {  # tcDadosServico
#                         "Valores": {  # tcValoresDeclaracaoServico
#                             "ValorServicos": nfse.info.valores.valor_servicos,
#                             "ValorDeducoes": nfse.info.valores.valor_deducoes,
#                             "ValorPis": nfse.info.valores.valor_pis,
#                             "ValorCofins": nfse.info.valores.valor_cofins,
#                             "ValorInss": nfse.info.valores.valor_inss,
#                             "ValorIr": nfse.info.valores.valor_ir,
#                             "ValorCsll": nfse.info.valores.valor_csll,
#                             "OutrasRetencoes": nfse.info.valores.outras_retencoes,
#                             "ValTotTributos": nfse.info.valores.valor_total_tributos,
#                             "ValorIss": nfse.info.valores.valor_iss,
#                             "Aliquota": nfse.info.valores.aliquota,
#                             "DescontoIncondicionado": nfse.info.valores.desconto_incodicionado,
#                             "DescontoCondicionado": nfse.info.valores.desconto_condicionado
#                         },
#                         "IssRetido": nfse.info.servico.iss_retido,
#                         "ResponsavelRetencao": nfse.info.servico.responsavel_retencao,
#                         "ItemListaServico": nfse.info.servico.item_lista_servico,
#                         "CodigoCnae": nfse.info.servico.codigo_cnae,
#                         "CodigoTributacaoMunicipio": nfse.info.servico.codigo_tributacao_municipio,
#                         "CodigoNbs": nfse.info.servico.codigo_nbs,
#                         "Discriminacao": nfse.info.servico.discriminacao,
#                         "CodigoMunicipio": nfse.info.servico.codigo_municipio,
#                         "CodigoPais": nfse.info.servico.codigo_pais,
#                         "ExigibilidadeISS": nfse.info.servico.exibilidade_iss,
#                         "IdentifNaoExigibilidade": nfse.info.servico.identificacao_nao_exigibilidade,
#                         "MunicipioIncidencia": nfse.info.servico.municipio_incidencia,
#                         "NumeroProcesso": nfse.info.servico.numero_processo
#                     },
#                     "Prestador": {  # tcIdentificacaoPessoaEmpresa
#                         "CpfCnpj": {  # tcCpfCnpj
#                             "Cpf": nfse.info.prestador.cpf,
#                             "Cnpj": nfse.info.prestador.cnpj
#                         },
#                         "InscricaoMunicipal": nfse.info.prestador.inscricao_muncipal
#                     },
#                     "TomadorServico": {  # tcDadosTomador
#                         "IdentificacaoTomador": {  # tcIdentificacaoPessoaEmpresa
#                             "CpfCnpj": {  # tcCpfCnpj
#                                 "Cpf": nfse.info.tomador.cpf,
#                                 "Cnpj": nfse.info.tomador.cnpj
#                             },
#                             "InscricaoMunicipal": nfse.info.tomador.inscricao_muncipal
#                         },
#                         "NifTomador": nfse.info.tomador.nif_tomador,
#                         "RazaoSocial": nfse.info.tomador.razao_social,
#                         "Endereco": {  # tcEndereco
#                             "Endereco": nfse.info.tomador.endereco.endereco,
#                             "Numero": nfse.info.tomador.endereco.numero,
#                             "Complemento": nfse.info.tomador.endereco.complemento,
#                             "Bairro": nfse.info.tomador.endereco.bairro,
#                             "CodigoMunicipio": nfse.info.tomador.endereco.codigo_municipio,
#                             "Uf": nfse.info.tomador.endereco.uf,
#                             "Cep": nfse.info.tomador.endereco.cep
#                         },
#                         # "EnderecoExterior": "",
#                         "Contato": {  # tcContato
#                             "Telefone": nfse.info.tomador.telefone,
#                             "Email": nfse.info.tomador.email
#                         }
#                     },
#                     # "Intermediario": "",
#                     # "ConstrucaoCivil": {  # tcDadosConstrucaoCivil
#                     #     "CodigoObra": "",
#                     #     "Art": ""
#                     # },
#                     "RegimeEspecialTributacao": nfse.info.regime_tributacao,
#                     "OptanteSimplesNacional": nfse.info.optante_simples_nacional,
#                     "IncentivoFiscal": nfse.info.incentivo_fiscal,
#                     # "Evento": {  # tcEvento
#                     #     "IdentificacaoEvento": "",
#                     #     "DescricaoEvento": "",
#                     # },
#                     "InformacoesComplementares": nfse.info.outras_informacoes,
#                     # Deducao: {}
#                     "Signature": ""
#                 }
#             }
#         })
#
#     def _add_fields_optional(self, rps: dict):
#         if self.nfse.info.intermediario:
#             rps['Rps']['InfDeclaracaoPrestacaoServico']['Intermediario'] = OrderedDict({  # tcDadosIntermediario
#                 "IdentificacaoIntermediario": {  # tcIdentificacaoPessoaEmpresa
#                     "CpfCnpj": {  # tcCpfCnpj
#                         "Cpf": self.nfse.info.intermediario.cpf,
#                         "Cnpj": self.nfse.info.intermediario.cnpj
#                     },
#                     "InscricaoMunicipal": self.nfse.info.intermediario.inscricao_muncipal
#                 },
#                 "RazaoSocial": self.nfse.info.intermediario.razao_social,
#                 "CodigoMunicipio": self.nfse.info.intermediario.codigo_municipio if self.nfse.ambiente == self.nfse.AMBIENTE.PRODUCAO else 9999999,
#             })
#         if self.nfse.info.tomador.endereco_exterior:
#             rps["Rps"]["InfDeclaracaoPrestacaoServico"]["Tomador"]["EnderecoExterior"] = OrderedDict(
#                 {  # tcEnderecoExterior
#                     "CodigoPais": self.nfse.info.tomador.endereco_exterior.codigo_pais,
#                     "EnderecoCompletoExterior": self.nfse.info.tomador.endereco_exterior.endereco_completo_exterior
#                 })
#
#         return rps
#
#     # def build(self, nfse: NfseModel):
#     #     self.gerar_rps_dict()
#     #
#     #     rps = self._add_fields_optional(self._add_lote_rps_dict())
#     #     lote_rps["LoteRps"]['QuantidadeRps'] = len(rps)
#     #     lote_rps["LoteRps"]["ListaRps"].append(rps)
#     #
#     #     return dicttoxml(lote_rps, root=False, attr_type=False, fold_list=False)
#         # nfse_xml = dicttoxml(lote_rps, root=False, attr_type=False)
#         # print(parseString(nfse_xml).toprettyxml())
#
#     @property
#     def id_lote_rps(self) -> str:
#         if self.nfse.ambiente == self.nfse.AMBIENTE.PRODUCAO:
#             return "LT-SINC-{}{}{}".format(
#                 self.nfse.info.prestador.cpf or self.nfse.info.prestador.cnpj,
#                 self.nfse.info.prestador.inscricao_muncipal or '_',
#                 self.nfse.pk  # NumeroLote
#             )
#
#         return "LT-SINC-HML-{}{}{}".format(
#             self.nfse.info.prestador.cpf or self.nfse.info.prestador.cnpj,
#             self.nfse.info.prestador.inscricao_muncipal or '_',
#             self.nfse.pk  # NumeroLote
#         )

from dataclasses import asdict

# from dicttoxml2 import dicttoxml
import xmltodict

from apps.nfse.services.Nfse import EnviarLoteRpsSincronoEnvio
from apps.nfse.models.nfse_model import NfseModel
from apps.utils.XmlUtil import XmlUtil


# o método unparse da lib xmltodict converte keys com prefixo @ em attr para a key pai
def factory(data):
    attrs = {
        'Id': '@Id',
        'versao': '@versao'
    }
    return {(attrs.get(key) if key in attrs.keys() else key): value for key, value in data}


class NfseEnvioSicrono:
    xml: str

    def __init__(self, nfse: NfseModel):
        self.nfse = EnviarLoteRpsSincronoEnvio(nfse)

    def _to_dict(self) -> dict:
        nfse_dic = dict()
        nfse_dic['EnviarLoteRpsSincronoEnvio'] = asdict(self.nfse, dict_factory=factory)
        return nfse_dic

    def _to_xml(self, nfse_dict: dict):
        self.xml = xmltodict.unparse(nfse_dict, full_document=False)

    def _add_namespace(self):
        self.xml = XmlUtil.add_attr_tag(self.xml, './/ListaRps/Rps', 'xmlns', 'http://www.abrasf.org.br/nfse.xsd')
        self.xml = XmlUtil.add_attr_tag(self.xml, '.', 'xmlns', 'http://www.abrasf.org.br/nfse.xsd')

    def build(self):
        nfse_dict = self._to_dict()
        self._to_xml(nfse_dict)
        #
        # print(self.xml)
        # self.xml = str(self.xml, encoding='utf8')
        # print(self.xml)
        self.xml = XmlUtil.add_signature(self.xml, './/ListaRps/Rps')
        self.xml = XmlUtil.add_signature(self.xml, '.')
        self.xml = XmlUtil.remove_tags_empty(self.xml)
        self._add_namespace()
        print(XmlUtil.to_string(self.xml))
        # print(str(self.xml, encoding='utf8'))

# def teste(nfse):
#     a = asdict(LoteRps(nfse))
#     print(a)
