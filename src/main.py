from pathlib import Path
import re
import sys

from cyk import CYK


def ler(multi_linhas: bool, mensagem: str) -> str:
    print(mensagem)
    linhas: list[str] = []
    while True:
        _in = input()
        if not _in.strip():
            return "\n".join(linhas)
        linhas.append(_in.strip())
        if not multi_linhas:
            break
    return "\n".join(linhas)


cyk = CYK()

regras = ler(multi_linhas=True, mensagem='Escreva as regras: ')
cyk.carregar_regra(regras)

print('')

palavra = ler(multi_linhas=False, mensagem='Informe a palavra para validar: ')
print('')

result = cyk.interpreta(palavra)

print('')
print(f'Resultado: {result}')
