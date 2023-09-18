from typing import Any


class Multiplicar:
    def __init__(self, func):
        self.func = func
        self. _multiplicador = 10
    
    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador 

@Multiplicar
def soma(x,y):
    return x + y


multiplicar = soma(2,4) 

print(multiplicar)




# class Multiplicar:
#     def __init__(self, multiplicador):
#         self._multiplicador = multiplicador

#     def __call__(self, func):
#         def interna(*args, **kwargs):
#             resultado = func(*args, **kwargs)
#             return resultado * self._multiplicador
#         return interna


# @Multiplicar(2)
# def soma(x, y):
#     return x + y

#isso aqui tambem serve