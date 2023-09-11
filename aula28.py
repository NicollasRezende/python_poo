# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
#Python nao suporta overload
#Python usa Sobreposiçao de metodos(override)

from abc import ABC, abstractmethod

class Notifications(ABC):
    def __init__(self, menssagem) -> None:
        self.menssagem = menssagem

    @abstractmethod
    def enviar(self) -> bool: ...


class Notifications_email(Notifications):
    def enviar(self): 
        print('email enviado...', self.menssagem)
        #finge que tem um puta processo de verificaçao aqui fds
        return True
class Notifications_SMS(Notifications):
    def enviar(self): 
        print('SMS enviado...', self.menssagem)
        return True
#this is polimorfismo primata :)
def notificar(notificacao: Notifications):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('notificacao enviada')
    else: 
        print('notificacao nao enviada')

notificacao_email = Notifications_email('email de spam da nubank')
notificacao_sms = Notifications_SMS('link para clonar seu cartao, clica ai neandertal')

notificar(notificacao_email)
notificar(notificacao_sms)


