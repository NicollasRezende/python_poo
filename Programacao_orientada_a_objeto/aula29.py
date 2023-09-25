# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...
class OtherError(Exception):
    ...


def showup():
    exeption_ = MyError("Menssage Error",'a', 'b')
    exeption_.add_note('Oh que foda o update do python 3.11.5')
    raise exeption_



try:
    showup()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OtherError('Descobriram que teu nubank e APKMod')
    raise exception_ from error



# testes tratando e levantando exeçoes e me acostumando a colocar tudo em ingles :)