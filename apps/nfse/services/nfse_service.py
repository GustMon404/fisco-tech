from apps.nfse.models.nfse_model import NfseModel
# from apps.nfse.services.NfseAbrasXML import NfseAbrasfXML
from apps.utils.XmlUtil import XmlUtil
from apps.nfse.services.NfseAbrasXML import NfseEnvioSicrono


def get_nfse_id(id: int) -> NfseModel:
    return NfseModel.objects.get(pk=id)


def autorizar(id: int):
    nfse = get_nfse_id(id)
    enviar = NfseEnvioSicrono(nfse)
    enviar.build()

# def autorizar_abrasf(id: int):
#     nfse = get_nfse_id(id)
#     nfse_xml = NfseAbrasfXML(nfse)
#
#     xml = nfse_xml.build()
#     xml = XmlUtil.remove_tags_empty(xml)
#
#     if nfse.ambiente == NfseModel.AMBIENTE.PRODUCAO.value:
#         xml = XmlUtil.add_attr_tag(xml, 'LoteRps', 'Id',
#                                    f'LT-SINC{nfse.info.prestador.cpf_cnpj}{nfse.info.prestador.inscricao_muncipal or "-"}{nfse.pk}')
#     else:
#         xml = XmlUtil.add_attr_tag(xml, 'LoteRps', 'Id',
#                                    f'LT-SINC-HML-{nfse.info.prestador.cpf_cnpj}{nfse.info.prestador.inscricao_muncipal or "-"}{nfse.pk}'')
#     xml = XmlUtil.add_attr_tag(xml, 'InfDeclaracaoPrestacaoServico', 'Id', f'RPS{id}')
#     xml = XmlUtil.add_attr_tag(xml, 'InfDeclaracaoPrestacaoServico', 'versao', '2.02')
#     xml = XmlUtil.add_attr_tag(xml, 'Rps', 'xmlns', 'http://www.abrasf.org.br/nfse.xsd')
#
#     print(xml)

