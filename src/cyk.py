import re


class CYK:

    regra_esquerda: dict[str, list]
    regra_direita: dict[str, list]

    def __init__(self) -> None:
        self.regra_esquerda = {}
        self.regra_direita = {}

    def __insere_item_regra(self, esquerda: str, direita: str):
        self.regra_esquerda[esquerda] = self.regra_esquerda.get(esquerda, [])
        self.regra_direita[direita] = self.regra_direita.get(direita, [])

        self.regra_esquerda[esquerda].append(direita)
        self.regra_direita[direita].append(esquerda)
