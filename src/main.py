from pathlib import Path
import re
import sys


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
