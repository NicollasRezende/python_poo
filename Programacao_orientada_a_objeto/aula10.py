# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('ola')

    @classmethod
    def criar_com_50(cls, nome):
        return cls(nome, 50) #factore



p1 = Pessoa('Ricardo', 32)
p2 = Pessoa.criar_com_50('jose')



print(p2.nome, p2.idade)
print(Pessoa.ano)
Pessoa.metodo_de_classe()