class Pessoa:

    ano_atual = 2023
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nacimento(self):
        return Pessoa.ano_atual - self.idade



p1 = Pessoa('carlos', 18)
p2 = Pessoa('Joao', 13)

print(p1.get_ano_nacimento())
print(p2.get_ano_nacimento())