# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...


class MyOpen:
    def __init__(self,file_path, mode_w_r,):
        self.file = file_path
        self.mode = mode_w_r
        self.archive = None
    def __enter__(self):
        self.archive = open(self.file,self.mode, encoding='utf8')
        return self.archive

    def __exit__(self, class_exeption, exeption_, traceback_):
        self.archive.close


with MyOpen('aula33.txt', 'w') as something:
    something.write('HAINIKI, FUCK YE')
    print('WITH', something)

#__init__
#__enter__
#corpo do with
#__exit__
