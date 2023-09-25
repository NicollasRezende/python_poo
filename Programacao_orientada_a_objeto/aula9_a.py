# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula9_b.json'


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



p1_nome = input('Nome: ')
p1_idade = input('Idade: ')
p1 = Pessoa(p1_nome, p1_idade)
dados_p1 = vars(p1)


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(
            dados_p1,
            arquivo,
            ensure_ascii=False,
            indent=2,
        )