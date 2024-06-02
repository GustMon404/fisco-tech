from dataclasses import dataclass, asdict, field
from typing import Optional
from decimal import Decimal
from datetime import datetime

from apps.nfse.models.nfse_model import *


class BaseNfse:
    def __iter__(self):
        for key in self.__dict__:
            if not getattr(self, key):
                continue

            if type(getattr(self, key)) not in (str, int, float, bool):
                yield key, dict(getattr(self, key))
            else:
                yield key, getattr(self, key)


@dataclass
class CpfCnpj(BaseNfse):
    Cpf: str = None
    Cnpj: str = None

    def __init__(self, cpf_cnpj: str):
        if len(cpf_cnpj) == 11:
            self.Cpf = cpf_cnpj
        else:
            self.Cnpj = cpf_cnpj


@dataclass
class Endereco(BaseNfse):
    Endereco: str
    Numero: str
    Complemento: str
    Bairro: str
    CodigoMunicipio: str
    Uf: str
    Cep: str

    def __init__(self, endereco: EnderecoModel):
        self.Endereco = endereco.endereco
        self.Numero = endereco.numero
        self.Complemento = endereco.complemento
        self.Bairro = endereco.bairro
        self.CodigoMunicipio = endereco.codigo_municipio
        self.Uf = endereco.uf
        self.Cep = endereco.uf


@dataclass
class EnderecoExterior(BaseNfse):
    CodigoPais: int
    EnderecoCompletoExterior: str

    def __init__(self, endereco_exterior: EnderecoExteriorModel):
        self.CodigoPais = endereco_exterior.codigo_pais
        self.EnderecoCompletoExterior = endereco_exterior.endereco_completo_exterior


@dataclass
class Contato(BaseNfse):
    Email: str
    Telefone: str


@dataclass
class IdentificacaoOrgaoGerador(BaseNfse):
    CodigoMunicipio: str
    Uf: str


@dataclass
class IdentificacaoRps(BaseNfse):
    Numero: int
    Serie: str
    Tipo: int


@dataclass
class IdentificacaoPessoaEmpresa(BaseNfse):
    CpfCnpj: CpfCnpj
    InscricaoMunicipal: str

    def __init__(self, cpf_cnpj: str, incricao_municipal: str):
        self.CpfCnpj = CpfCnpj(cpf_cnpj)
        self.InscricaoMunicipal = incricao_municipal


@dataclass
class DadosTomador(BaseNfse):
    IdentificacaoTomador: IdentificacaoPessoaEmpresa
    NifTomador: str
    RazaoSocial: str
    Endereco: Endereco | None
    EnderecoExterior: EnderecoExterior | None
    Contato: Contato

    def __init__(self, tomador: TomadorModel):
        self.IdentificacaoTomador = IdentificacaoPessoaEmpresa(tomador.cpf_cnpj, tomador.inscricao_muncipal)
        self.NifTomador = tomador.nif_tomador
        self.RazaoSocial = tomador.razao_social
        self.Endereco = Endereco(tomador.endereco) if tomador.endereco else None
        self.EnderecoExterior = EnderecoExterior(tomador.endereco_exterior) if tomador.endereco_exterior else None
        self.Contato = Contato(tomador.email, tomador.telefone)


@dataclass
class DadosIntermediario(BaseNfse):
    IdentificacaoIntermediario: IdentificacaoPessoaEmpresa
    RazaoSocial: str
    CodigoMunicipio: int

    def __init__(self, intemediario: IntermediarioModel):
        self.IdentificacaoIntermediario = IdentificacaoPessoaEmpresa(intemediario.cpf_cnpj,
                                                                     intemediario.inscricao_muncipal)
        self.RazaoSocial = intemediario.razao_social
        self.CodigoMunicipio = intemediario.codigo_municipio


@dataclass
class ValoresDeclaracaoServico(BaseNfse):
    ValorServicos: Decimal
    ValorDeducoes: Decimal
    ValorPis: Decimal
    ValorCofins: Decimal
    ValorInss: Decimal
    ValorIr: Decimal
    ValorCsll: Decimal
    OutrasRetencoes: Decimal
    ValTotTributos: Decimal
    ValorIss: Decimal
    Aliquota: Decimal
    DescontoIncondicionado: Decimal
    DescontoCondicionado: Decimal

    def __init__(self, valor: ValoresModel):
        self.ValorServicos = valor.valor_servicos
        self.ValorDeducoes = valor.valor_deducoes
        self.ValorPis = valor.valor_pis
        self.ValorCofins = valor.valor_cofins
        self.ValorInss = valor.valor_inss
        self.ValorIr = valor.valor_ir
        self.ValorCsll = valor.valor_csll
        self.OutrasRetencoes = valor.outras_retencoes
        self.ValTotTributos = valor.valor_total_tributos
        self.ValorIss = valor.valor_iss
        self.Aliquota = valor.aliquota
        self.DescontoIncondicionado = valor.desconto_incodicionado
        self.DescontoCondicionado = valor.desconto_condicionado


@dataclass
class ValoresNfse(BaseNfse):
    BaseCalculo: Decimal
    Aliquota: Decimal
    ValorIss: Decimal
    ValorLiquidoNfse: Decimal

    def __init__(self, valor: ValoresModel):
        self.BaseCalculo = valor.base_calculo
        self.Aliquota = valor.aliquota
        self.ValorIss = valor.valor_iss
        self.ValorLiquidoNfse = valor.valor_liquido_nfse


@dataclass
class DadosServico(BaseNfse):
    Valores: ValoresDeclaracaoServico
    IssRetido: int
    ResponsavelRetencao: int
    ItemListaServico: str
    CodigoCnae: int
    CodigoTributacaoMunicipio: str
    CodigoNbs: str
    Discriminacao: str
    CodigoMunicipio: int
    CodigoPais: str
    ExigibilidadeISS: int
    IdentifNaoExigibilidade: str
    MunicipioIncidencia: int
    NumeroProcesso: str

    def __init__(self, servico: ServicoModel, valor: ValoresModel):
        self.Valores = ValoresDeclaracaoServico(valor)
        self.IssRetido = servico.iss_retido
        self.ResponsavelRetencao = servico.responsavel_retencao
        self.ItemListaServico = servico.item_lista_servico
        self.CodigoCnae = servico.codigo_cnae
        self.CodigoTributacaoMunicipio = servico.codigo_tributacao_municipio
        self.CodigoNbs = servico.codigo_nbs
        self.Discriminacao = servico.discriminacao
        self.CodigoMunicipio = servico.codigo_municipio
        self.CodigoPais = servico.codigo_pais
        self.ExigibilidadeISS = servico.exibilidade_iss
        self.IdentifNaoExigibilidade = servico.identificacao_nao_exigibilidade
        self.MunicipioIncidencia = servico.municipio_incidencia
        self.NumeroProcesso = servico.numero_processo


@dataclass
class DadosConstrucaoCivil(BaseNfse):
    CodigoObra: str
    Art: str

    def __init__(self, construcao_civil: ConstrucaoCivilModel):
        self.CodigoObra = construcao_civil.codigo_obra
        self.Art = construcao_civil.art


@dataclass
class Evento(BaseNfse):
    IdentificacaoEvento: str
    DescricaoEvento: str

    def __init__(self, evento: EventoModel):
        self.IdentificacaoEvento = evento.identificao
        self.DescricaoEvento = evento.descricao


@dataclass
class DadosPrestador(BaseNfse):
    RazaoSocial: str
    NomeFantasia: str
    Endereco: Endereco
    Contato: Contato

    def __init__(self, prestador: PrestadorModel):
        self.RazaoSocial = prestador.nome_razao
        self.NomeFantasia = prestador.nome_fantasia
        self.Endereco = Endereco(prestador.endereco)
        self.Contato = Contato(prestador.email, prestador.telefone)


@dataclass
class IdentificacaoNfseDeducao(BaseNfse):
    CodigoMunicipioGerador: int
    NumeroNfse: int
    CodigoVerificao: str


@dataclass
class IdentificacaoNfeDeducao(BaseNfse):
    NumeroNfe: int
    UfNfe: str
    ChaveAcessoNfe: int


@dataclass
class OutroDocumentoDeducao(BaseNfse):
    IdentificacaoDocumento: str


@dataclass
class IdentificacaoDocumentoDeducao(BaseNfse):
    IdentificacaoNfse: IdentificacaoNfseDeducao
    IdentificacaoNFe: IdentificacaoNfeDeducao
    OutroDocumento: OutroDocumentoDeducao

    def __init__(self, deducao: DeducaoModel):
        self.IdentificacaoNfse = IdentificacaoNfseDeducao(deducao.codigo_municipio_gerador, deducao.numero_nfse,
                                                          deducao.codigo_verificacao)
        self.IdentificacaoNFe = IdentificacaoNfeDeducao(deducao.numero_nfe, deducao.uf_nfe, deducao.chave_acesso_nfe)
        self.OutroDocumento = OutroDocumentoDeducao(deducao.identificacao_documento)


@dataclass
class IdentificacaoFornecedor(BaseNfse):
    CpfCnpj: CpfCnpj

    def __init__(self, cpf_cnpj: str):
        self.CpfCnpj = CpfCnpj(cpf_cnpj)


@dataclass
class FornecedorExterior(BaseNfse):
    NifFornecedor: str
    CodigoPais: str


@dataclass
class DadosFornecedor(BaseNfse):
    IdentificacaoFornecedor: IdentificacaoFornecedor
    FornecedorExterior: FornecedorExterior

    def __init__(self, fornecedor: FornecedorModel):
        self.IdentificacaoFornecedor = IdentificacaoFornecedor(fornecedor.cpf_cnpj)
        self.FornecedorExterior = FornecedorExterior(fornecedor.nif_forncedor, fornecedor.codigo_pais)


@dataclass
class DadosDeducao(BaseNfse):
    TipoDeducao: int
    DescricaoDeducao: str
    IdentificacaoDocumentoDeducao: IdentificacaoDocumentoDeducao
    DadosFornecedor: DadosFornecedor
    DataEmissao: str
    ValorDedutivel: Decimal
    ValorUtilizadoDeducao: Decimal

    def __init__(self, deducao: DeducaoModel):
        self.TipoDeducao = deducao.tipo_deducao
        self.DescricaoDeducao = deducao.descricao_deducao
        self.IdentificacaoDocumentoDeducao = IdentificacaoDocumentoDeducao(deducao)
        self.DadosFornecedor = DadosFornecedor(deducao.fornecedor)
        self.DataEmissao = datetime.strftime(deducao.data_emissao, '%Y-%m-%d')
        self.ValorDedutivel = deducao.valor_dedutivel
        self.ValorUtilizadoDeducao = deducao.valor_utilizado_deducao


@dataclass
class InfRps(BaseNfse):
    IdentificacaoRps: IdentificacaoRps
    DataEmissao: str
    status: int
    RpsSubstituido: IdentificacaoRps

    def __init__(self, rps: RpsModel):
        self.IdentificacaoRps = IdentificacaoRps(rps.numero, rps.serie, rps.tipo)
        self.DataEmissao = datetime.strftime(rps.data_emissao_rps, '%Y-%m-%d')
        self.status = rps.status
        self.RpsSubstituido = IdentificacaoRps(rps.numero_substituido, rps.serie_substituido, rps.tipo_substituido)


@dataclass
class InfDeclaracaoPrestacaoServico(BaseNfse):
    Id: str
    Rps: InfRps
    Competencia: str
    Servico: DadosServico
    Prestador: IdentificacaoPessoaEmpresa
    TomadorServico: DadosTomador
    Intermediario: DadosIntermediario | None
    ConstrucaoCivil: DadosConstrucaoCivil | None
    RegimeEspecialTributacao: int
    OptanteSimplesNacional: int
    IncentivoFiscal: int
    Evento: Evento | None
    InformacoesComplementares: str
    Deducao: list[DadosDeducao] | None

    def __init__(self, info_nfse: InfoNFseModel, prestador: PrestadorModel):
        self.Id = f'RPS{info_nfse.pk}'
        self.Rps = InfRps(info_nfse.rps)
        self.Competencia = datetime.strftime(info_nfse.competencia, '%Y-%m-%d')
        self.Servico = DadosServico(info_nfse.servico, info_nfse.valores)
        self.Prestador = IdentificacaoPessoaEmpresa(prestador.cpf_cnpj, prestador.inscricao_muncipal)
        self.TomadorServico = DadosTomador(info_nfse.tomador) if info_nfse.tomador else None
        self.Intermediario = DadosIntermediario(info_nfse.intermediario) if info_nfse.intermediario else None
        self.ConstrucaoCivil = DadosConstrucaoCivil(info_nfse.construcao_civil) if info_nfse.construcao_civil else None
        self.RegimeEspecialTributacao = info_nfse.regime_tributacao
        self.OptanteSimplesNacional = info_nfse.optante_simples_nacional
        self.IncentivoFiscal = info_nfse.incentivo_fiscal
        self.Evento = Evento(info_nfse.evento) if info_nfse.evento else None
        self.InformacoesComplementares = info_nfse.outras_informacoes
        self.Deducao = [DadosDeducao(deducao) for deducao in
                        info_nfse.deducoes.all()] if info_nfse.deducoes.exists() else None


@dataclass
class DeclaracaoPrestacaoServico(BaseNfse):
    InfDeclaracaoPrestacaoServico: InfDeclaracaoPrestacaoServico

    def __init__(self, info: InfoNFseModel, prestador: PrestadorModel):
        self.InfDeclaracaoPrestacaoServico = InfDeclaracaoPrestacaoServico(info, prestador)

    # Signature


@dataclass
class IdentificacaoNfse(BaseNfse):
    Numero: int
    CpfCnpj: CpfCnpj
    InscricaoMunicipal: str
    CodigoMunicipio: int

    def __init__(self, info_nfse: InfoNFseModel, prestador: PrestadorModel):
        self.Numero = info_nfse.numero
        self.CpfCnpj = CpfCnpj(prestador.cpf_cnpj)
        self.InscricaoMunicipal = prestador.inscricao_muncipal
        self.CodigoMunicipio = info_nfse.servico.codigo_municipio


# estrutura de retorno
class InfNfse(BaseNfse):
    Numero: int
    CodigoVerificacao: str
    DataEmissao: str
    NfseSubstituida: int
    OutrasInformacoes: str
    ValoresNfse: ValoresNfse
    DescricaoCodigoTributacaoMunicípio: str
    ValorCredito: str
    PrestadorServico: DadosPrestador
    OrgaoGerador: DeclaracaoPrestacaoServico


# estrutura de retorno
class Nfse(BaseNfse):
    InfNfse: InfNfse
    # Signature


class InfPedidoCancelamento(BaseNfse):
    IdentificacaoNfse: IdentificacaoNfse
    CodigoCancelamento: str


class PedidoCancelamento(BaseNfse):
    InfPedidoCancelamento: InfPedidoCancelamento
    # Signature


class ConfirmacaoCancelamento(BaseNfse):
    Pedido: PedidoCancelamento
    DataHora: str


class CancelamentoNfse(BaseNfse):
    Confirmacao: ConfirmacaoCancelamento
    # Signature


class RetCancelamento(BaseNfse):
    NfseCancelamento: CancelamentoNfse


class InfSubstituicaoNfse(BaseNfse):
    NfseSubstituidora: int


class SubstituicaoNfse(BaseNfse):
    SubstituicaoNfse: InfSubstituicaoNfse
    # Signature


class CompNfse(BaseNfse):
    Nfse: Nfse
    NfseCancelamento: CancelamentoNfse
    NfseSubstituicao: SubstituicaoNfse


class MensagemRetorno(BaseNfse):
    Codigo: str
    Mensagem: str
    Correcao: str


class MensagemRetornoLote(BaseNfse):
    IdentificacaoNfse: IdentificacaoNfse
    Codigo: str
    Mensagem: str


@dataclass
class Rps(BaseNfse):
    Rps: DeclaracaoPrestacaoServico

    def __init__(self, info: InfoNFseModel, prestador: PrestadorModel):
        self.Rps = DeclaracaoPrestacaoServico(info, prestador)


@dataclass
class LoteRps(BaseNfse):
    Id: str
    versao: str
    NumeroLote: int
    Prestador: IdentificacaoPessoaEmpresa
    QuantidadeRps: int
    ListaRps: list[Rps]

    def __init__(self, nfse: NfseModel):
        self.Id = LoteRps.get_value_attr_lote_rps(nfse)
        self.versao = nfse.versao
        self.NumeroLote = nfse.pk
        self.Prestador = IdentificacaoPessoaEmpresa(nfse.prestador.cpf_cnpj, nfse.prestador.inscricao_muncipal)
        self.ListaRps = [Rps(info, nfse.prestador) for info in nfse.infos.all()]
        self.QuantidadeRps = len(self.ListaRps)

    @staticmethod
    def get_value_attr_lote_rps(nfse: NfseModel) -> str:
        if nfse.ambiente == NfseModel.AMBIENTE.PRODUCAO.value:
            return f'LT-SINC-{nfse.prestador.cpf_cnpj}{nfse.prestador.inscricao_muncipal or "-"}{nfse.pk}'
        return f'LT-SINC-HM-{nfse.prestador.cpf_cnpj}{nfse.prestador.inscricao_muncipal or "-"}{nfse.pk}'

    # def __post_init__(self, ListaRps):
    #     pass


class ListaMensagemRetornoLote(BaseNfse):
    MensagemRetorno: MensagemRetornoLote = MensagemRetornoLote()


class ListaMensagemRetorno(BaseNfse):
    MensagemRetorno: MensagemRetorno = MensagemRetorno()


class ListaMensagemAlertaRetorno(BaseNfse):
    MensagemRetorno: MensagemRetorno = MensagemRetorno()


@dataclass
class EnviarLoteRpsSincronoEnvio(BaseNfse):
    LoteRps: LoteRps

    # signature

    def __init__(self, nfse: NfseModel):
        self.LoteRps = LoteRps(nfse)
