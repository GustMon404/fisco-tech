from django.core.exceptions import ValidationError
import re


def validade_cpf_cnpj(value):
    if not len(value) in [11, 14]:
        raise ValidationError("'%(value)s' Não é um valor válido para cpf ou cnpj", params={"value": value})
    if not re.match(r'^\d+$', value):
        raise ValidationError("'%(value)s' deve conter apenas números", params={"value": value})
