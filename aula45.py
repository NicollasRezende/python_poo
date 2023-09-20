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


class ContaCorrente(Banco):
    def __init__(self, tipoconta, nomebanco, saldo, senha) -> None:
        super().__init__(tipoconta, nomebanco, saldo, senha)
        self.definir_saldo = 0
        self.definir_nome_banco ='Nenhum'
        self.definir_senha = 12
        self.definir_tipo_conta = 'Nenhum'
        self.sacar = True
        self.depositar = True
        self.verificar_saldo = True
        self.fazer_tranferencia = True



class ContaPoupanca(Banco):
    def __init__(self, tipoconta, nomebanco, saldo, senha) -> None:
        super().__init__(tipoconta, nomebanco, saldo, senha)
        self.definir_saldo = 0
        self.definir_nome_banco ='Nenhum'
        self.definir_senha = 12
        self.definir_tipo_conta = 'Nenhum'
        self.sacar = True
        self.depositar = True
        self.verificar_saldo = True
        self.fazer_tranferencia = False


#---------------------CONF DE CRIACAO----------------------------
import random
CONTA_GERADA = None
BANCO = None
NOME = None
IDADE = None
TRABALHO = None
SENHA = None
TIPO_CONTA = None
USER = None
MENU = True
def gerar_numero_conta():
    NUMERO_CONTA = random.randint(1000000, 9999999)
    return NUMERO_CONTA

#---------------------CRIACAO DA CONTA----------------------------
criar = input('Deseja criar uma conta?[S]im, [N]ao: ')

if criar == 'S':

    criar2 = input('Qual Banco? 1-Bradesco, 2-Santander, 3-Banco do Brasil: ')

    if criar2 == 1:
        BANCO = 'Bradesco'
    if criar2 == 2:
        BANCO = 'Santander'
    if criar2 == 3:
        BANCO = 'Banco_do_Brasil'

    user_nome = input('Digite seu nome: ')
    user_idade = input('Digite sua idade: ')
    user_emprego = input('Voce trabalha de que? : ')
    user_tipo_conta = input('Escolha um tipo de conta, Conrrente-1, Poupança-2: ')
    user_senha_conta = input('crie uma senha de 4 digitos: ')

    CONTA_GERADA = gerar_numero_conta()
    NOME = user_nome
    IDADE = user_idade
    TRABALHO = user_emprego
    SALDO = 0
    SENHA = user_senha_conta
    print(f'o Banco escolhido foi {BANCO}')
    print(f'o numero da sua conta e {CONTA_GERADA}')
    print(f'o seu nome e {NOME}')
    print(f'voce tem {IDADE} anos')
    print(f'voce trabalha como {TRABALHO}')
    print(f'Sua senha escolhida foi: {SENHA}')


    if user_tipo_conta == '1':
        TIPO_CONTA = 'Corrente'
        USER = ContaCorrente('Corrente', BANCO, SALDO, SENHA)

    if user_tipo_conta == '2':
        TIPO_CONTA = 'Poupança'
        USER = ContaPoupanca('Poupança', BANCO, SALDO, SENHA)
    
    USER.definir_nome_banco = BANCO
    USER.tipo_conta = TIPO_CONTA
    USER.definir_nome_pessoa = NOME
    USER.definir_idade_pessoa = IDADE
    USER.definir_trabalho_pessoa = TRABALHO
    USER.definir_saldo = SALDO

else: 
    print('sifode entao')
    MENU = False


#---------------------MENU BANCO----------------------------

while MENU:
    print()
    print(f'BEM VINDO AO MENU DO {BANCO}')
    print()
    print('O QUE VOCE DESEJA REALIZAR:')
    print('1- ACESSAR INFORMAÇOES DA CONTA')
    print('2- ACESSAR MENU DE TRANSFERENCIA')
    print('3- CONSULTAR O SALDO DA CONTA')
    print('4- MENU DE DEPOSITO')
    print('5- MENU DE SAQUE')
    print('6- SAIR')
    
    usuario1 = input('Digite o numero da opçao: ')


    if usuario1 == 1:
        print()
        print(f'SEU BANCO: {BANCO}')
        print(f'NUMERO DA SUA CONTA: {CONTA_GERADA}')
        print(f'SEU NOME: {NOME}')
        print(f'SUA IDADE: {IDADE}')
        print(f'SUA PROFIÇAO: {TRABALHO}')
        print(f'SUA SENHA:{SENHA}')
        continue
    if usuario1 == 2 and USER.fazer_tranferencia == True:
        print()
        print('-MENU DE TRANFERENCIA-')
        trasnferir1 = int(input('Quanto deseja tranferir:'))
        if trasnferir1 < SALDO:
            print('voce nao tem saldo suficiente para fazer isso.')
        else:
            print()
            digitar_senha1 = int(input('DIGITE SUA SENHA DE 7 DIGITOS:'))
            if digitar_senha1 == SENHA:
                SALDO -= trasnferir1
                USER.definir_saldo(SALDO)
                print()
                print(f'Sua transferencia no valor de {trasnferir1} foi concluida com sucesso!')
                print(f'Seu saldo atual e de {SALDO}')
                continue
            else:
                print('nao foi possivel realizar a transferencia')
                continue
    if usuario1 == 3:
        print()
        print(f'O SEU SALDO E DE:')
        print(f'({SALDO})')
        continue
    if usuario1 == 4:
        print()
        print('-MENU DE DEPOSITO-')
        print()
        digitar_senha1 = int(input('DIGITE SUA SENHA DE 7 DIGITOS:'))
        if digitar_senha1 == SENHA:
            print()
            deposito1 = int(input('QUANTO VOCE DESEJA DEPOSITAR:'))
            print()
            SALDO += deposito1
            USER.definir_saldo(SALDO)
            print(f'DEPOSITO NO VALOR DE {deposito1} REALIZADO COM SUCESSO!')
            print(f'SEU SALDO ATUAL E DE {SALDO}')
            continue
        else:
            print('nao foi possivel realizar o deposito')
            continue
    if usuario1 == 5:
        print()
        print('-MENU DE SAQUE-')
        digitar_senha1 = int(input('DIGITE SUA SENHA DE 7 DIGITOS:'))
        if digitar_senha1 == SENHA:
            print()
            saque1 = input('QUANTO VOCE DESEJA SACAR?: ')
            if saque1 > SALDO:
                print(f'SEU SAQUE NO VALOR DE {saque1} NAO PODE SER REALIZADO POIS O SALDO DA SUA CONTA E MENOR DO QUE O VALOR SOLICITADO')
                print(f'SEU SALDO E DE {SALDO}')
                continue
            if saque1 < SALDO:
                print()
                SALDO -= saque1
                USER.definir_saldo(SALDO)
                print(f'O SEU SAQUE NO VALOR DE {saque1} FOI REALIZADO COM SUCESSO!')
                print(f'O SEU SALDO ATUAL E DE {SALDO}')
                continue
        else:
            print('nao foi possivel realizar o saque')
            continue






