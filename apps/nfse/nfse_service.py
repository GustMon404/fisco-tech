from apps.nfse.models.nfse_model import NfseModel


class NfseService:
    def __init__(self, nfse: NfseModel):
        self.nfse = nfse

    def object_to_dict(self):
        nfse_dict = {
            "LoteRps": {  # tcLoteRps
                "NumeroLote": self.nfse.pk,
                "Prestador": {  # tcIdentificacaoPessoaEmpresa
                    "CpfCnpj": {  # tcCpfCnpj
                        "Cpf": self.nfse.info.prestador.cpf,
                        "Cnpj": self.nfse.info.prestador.cnpj
                    },
                    "InscricaoMunicipal": self.nfse.info.prestador.inscricao_muncipal
                },
                "QuantidadeRps": 1,
                "ListaRps": [
                    {
                        "Rps": {  # tcDeclaracaoPrestacaoServico
                            "InfDeclaracaoPrestacaoServico": {  # tcInfDeclaracaoPrestacaoServico
                                "Rps": {  # tcInfRps
                                    "IdentificacaoRps": {  # tcIdentificacaoRps
                                        "Numero": self.nfse.info.rps.numero,
                                        "Serie": self.nfse.info.rps.serie,
                                        "Tipo": self.nfse.info.rps.tipo
                                    },
                                    "DataEmissao": self.nfse.info.rps.data_emissao_rps,
                                    "Status": self.nfse.info.rps.status,
                                    "RpsSubstituido": {  # tcIdentificacaoRps
                                        "Numero": self.nfse.info.rps.numero_substituido,
                                        "Serie": self.nfse.info.rps.serie_substituido,
                                        "Tipo": self.nfse.info.rps.tipo_substituido
                                    },
                                    "Id": ""
                                },
                                "Competencia": self.nfse.,
                                "Servico": {  # tcDadosServico
                                    "Valores": {  # tcValoresDeclaracaoServico
                                        "ValorServicos": "",
                                        "ValorDeducoes": "",
                                        "ValorPis": "",
                                        "ValorCofins": "",
                                        "ValorInss": "",
                                        "ValorIr": "",
                                        "ValorCsll": "",
                                        "OutrasRetencoes": "",
                                        "ValTotTributos": "",
                                        "ValorIss": "",
                                        "Aliquota": "",
                                        "DescontoIncondicionado": "",
                                        "DescontoCondicionado": ""
                                    },
                                    "IssRetido": "",
                                    "ResponsavelRetencao": "",
                                    "ItemListaServico": "",
                                    "CodigoCnae": "",
                                    "CodigoTributacaoMunicipio": "",
                                    "CodigoNbs": "",
                                    "Discriminacao": "",
                                    "CodigoMunicipio": "",
                                    "CodigoPais": "",
                                    "ExigibilidadeISS": "",
                                    "IdentifNaoExigibilidade": "",
                                    "MunicipioIncidencia": "",
                                    "NumeroProcesso": ""
                                },
                                "Prestador": {  # tcIdentificacaoPessoaEmpresa
                                    "CpfCnpj": {  # tcCpfCnpj
                                        "Cpf": "",
                                        "Cnpj": ""
                                    },
                                    "InscricaoMunicipal": ""
                                },
                                "TomadorServico": {  # tcDadosTomador
                                    "IdentificacaoTomador": {  # tcIdentificacaoPessoaEmpresa
                                        "CpfCnpj": {  # tcCpfCnpj
                                            "Cpf": "",
                                            "Cnpj": ""
                                        },
                                        "InscricaoMunicipal": ""
                                    },
                                    "NifTomador": "",
                                    "RazaoSocial": "",
                                    "Endereco": {  # tcEndereco
                                        "Endereco": "",
                                        "Numero": "",
                                        "Complemento": "",
                                        "Bairro": "",
                                        "CodigoMunicipio": "",
                                        "Uf": "",
                                        "Cep": ""
                                    },
                                    "EnderecoExterior": {  # tcEnderecoExterior
                                        "CodigoPais": "",
                                        "EnderecoCompletoExterior": ""
                                    },
                                    "Contato": {  # tcContato
                                        "Telefone": "",
                                        "Email": ""
                                    }
                                },
                                "Intermediario": {  # tcDadosIntermediario
                                    "IdentificacaoIntermediario": {  # tcIdentificacaoPessoaEmpresa
                                        "CpfCnpj": {  # tcCpfCnpj
                                            "Cpf": "",
                                            "Cnpj": ""
                                        },
                                        "InscricaoMunicipal": ""
                                    },
                                    "RazaoSocial": "",
                                    "CodigoMunicipio": "",
                                },
                                "ConstrucaoCivil": {  # tcDadosConstrucaoCivil
                                    "CodigoObra": "",
                                    "Art": ""
                                },
                                "RegimeEspecialTributacao": "",
                                "OptanteSimplesNacional": "",
                                "IncentivoFiscal": "",
                                "Evento": {  # tcEvento
                                    "IdentificacaoEvento": "",
                                    "DescricaoEvento": "",
                                },
                                "InformacoesComplementares": "",
                                # Deducao: {}
                                "Signature": ""
                            }
                        }
                    }
                ],
                "versao": ""
            }
        }
