# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class



class Pessoa:
    def __init__(self,nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome



class Cliente(Pessoa):
    ...
class Aluno(Pessoa):
    ...




c1 = Cliente('Maria','Helena')
c2 = Aluno('Nicollas','Rezende')