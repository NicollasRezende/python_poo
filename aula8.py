class Pessoa:

    ano_atual = 2023
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nacimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'idade': 18, 'nome': 'carlos'}

p1 = Pessoa('carlos', 18)
p1 = Pessoa(**dados)

# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'sla'
# del p1.__dict__['nome']
#e possivel alterar ^^^^^^

print(p1.__dict__)
print(vars(p1))