# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código


class Carro:
    def __init__(self, nome,):
        self.nome = nome
    
    def acelerando(self):
        print(f'{self.nome}, esta acelerando..')



carro1 = Carro('fusca')
print(carro1.nome)
carro1.acelerando()