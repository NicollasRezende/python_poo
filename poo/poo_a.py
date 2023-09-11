#CLASSE CLIENTE

class Cliente():
    def __init__(self,nome, idade,cpf):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf

#--nome property e setter
    @property
    def nome_cliente(self):
        return self._nome
    @nome_cliente.setter
    def mudar_nome(self,nome):
        self._nome = nome

#--idade property e setter
    @property
    def idade_cliente(self):
        return self._idade
    @idade_cliente.setter
    def mudar_idade(self, idade):
        self._idade = idade

#----cpf property e setter
    @property
    def cpf_cliente(self):
        return self._cpf
    @cpf_cliente.setter
    def mudar_cpf(self,cpf):
        self._cpf = cpf

#criando os dados
dados_cliente = ['jose',27,'123.456.789-01']

cliete = Cliente(*dados_cliente)

#acessando os dados
print(cliete.nome_cliente)
print(cliete.cpf_cliente)
print(cliete.idade_cliente)
print()


#mudando os dados
cliete.mudar_nome = 'Nicollas'
cliete.mudar_idade = 18
cliete.mudar_cpf = '123.456.789.01'
#acessando os dados
print(cliete.nome_cliente)
print(cliete.cpf_cliente)
print(cliete.idade_cliente)
