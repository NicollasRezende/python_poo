"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Cliente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod

class Cria_Pessoa(ABC):

    def __init__(self):
        self._nome_pessoa = None
        self._idade_pessoa = None
        self._trabalho_pessoa = None

    @property
    def nome_pessoa(self):
        return self._nome_pessoa
    
    @property
    def idade_pessoa(self):
        return self._idade_pessoa
    
    @property
    def trabalho_pessoa(self):
        return self._trabalho_pessoa
    
    @nome_pessoa.setter
    def definir_nome_pessoa(self,muda_nome):
        self._nome_pessoa = muda_nome

    @idade_pessoa.setter
    def definir_idade_pessoa(self,muda_idade):
        self._idade_pessoa = muda_idade

    @trabalho_pessoa.setter
    def definir_trabalho_pessoa(self,muda_trabalho):
        self._trabalho_pessoa = muda_trabalho

class Banco(ABC):
    def __init__(self, tipoconta, nomebanco,saldo,senha) -> None:
        self._tipo_conta = tipoconta
        self._nome_banco = nomebanco
        self._saldo = saldo
        self._senha = senha
    @property
    def tipo_conta(self):
        return self._tipo_conta
    
    @property
    def nome_banco(self):
        return self._nome_banco

    @property
    def saldo(self):
        return self._saldo

    @property
    def senha(self):
        return self._senha
    

    @tipo_conta.setter
    def definir_tipo_conta(self, tipo):
        self.tipo_conta = tipo


    @nome_banco.setter
    def definir_nome_banco(self, nome):
        self.nome_banco = nome

    @saldo.setter
    def definir_saldo(self, valor):
        self.saldo = valor

    @senha.setter
    def definir_senha(self, senha_def):
        self.senha = senha_def




