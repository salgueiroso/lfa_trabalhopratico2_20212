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

    def carregar_regra(self, texto: str):
        linhas = list(filter(lambda x: bool(x.strip()),
                      texto.strip().splitlines()))
        for linha in linhas:
            esquerda, direita = map(
                lambda item: item.strip(), linha.split('=>'))
            direitas = re.findall(r"\w+", direita, re.IGNORECASE)
            for item_direita in direitas:
                self.__insere_item_regra(esquerda, item_direita)

    def interpreta(self, palavra: str):

        camadas: list[list[list[str]]] = [[]]

        for item in re.findall(r"[a-z]", palavra, re.IGNORECASE):
            if not self.regra_direita.get(item, None):
                return False

            to_insert = []

            for regra in self.regra_direita[item]:
                to_insert.append(regra)

            camadas[0].append(to_insert)

            print(f'{item}', end='\t')

        print('')

        for items in camadas[0]:
            lst_str = ','.join(items)
            print(f'{lst_str}', end='\t')

        print('')

        for nivel in range(2, len(camadas[0])+1):
            camadas.insert(nivel-1, [])

            for i in range(1, len(camadas[nivel-1-1])):

                possibilidades = []

                for l in range(1, nivel):
                    for primeiro in camadas[l-1][i-1]:
                        for segundo in camadas[nivel-l-1][i+l-1]:
                            possibilidades.append(f'{primeiro}{segundo}')

                camadas[nivel-1].insert(i-1, [])

                for tentativa in possibilidades:
                    if self.regra_direita.get(tentativa, None):
                        for regra in self.regra_direita[tentativa]:
                            inserir = True

                            for teste in camadas[nivel-1][i-1]:
                                if teste == regra:
                                    inserir = False
                                    break

                            if inserir:
                                camadas[nivel-1][i-1].append(regra)

            for items in camadas[nivel-1]:
                saida = ','.join(items)
                print(saida, end='\t')

            print('')

        tam = len(camadas[len(camadas[0])-1][0])

        return tam != 0
