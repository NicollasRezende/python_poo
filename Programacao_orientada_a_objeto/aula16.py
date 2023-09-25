# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).


class Carrinho:
    def __init__(self):
        self._produtos = []


    def inserir_produtos(self,*produtos):
        for p in produtos:
            self._produtos.append(p)

    def total(self):
        return sum([p.preco for p in self._produtos])

    def listar(self):
        for produto in self._produtos:
            print()
            print(produto.nome, produto.preco)
            print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco




carrinho = Carrinho()

produto1,produto2  = Produto('caneta', 1.20),Produto('camisa', 20)

carrinho.inserir_produtos(produto1, produto2)

carrinho.listar()

print(carrinho.total())

