import re
from brutils import format_cnpj, is_valid_cnpj


def format_cnpj_safe(cnpj):
    if not cnpj:
        return None

    cnpj = re.sub(r'\D', '', str(cnpj))

    if len(cnpj) != 14:
        return None

    return format_cnpj(cnpj)