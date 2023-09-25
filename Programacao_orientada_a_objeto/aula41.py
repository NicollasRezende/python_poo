from typing import Any


def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr
        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')
        return cls
    def __call__(self, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        print(instancia.__dict__)
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Implemente nome')
        return instancia

class Pessoa(object, metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self):
        print('Falando...')




p1 = Pessoa('Nicollas')
print(p1.attr)
print(Pessoa.attr)