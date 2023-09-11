# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import copy


lista_total = []
lista_backup = []

#------------------


while True:
    comando = input('Digite um comando: ')
    print()

    if comando == 'adicionar':
        add = input('O que deseja adicionar: ')
        print()
        lista_total.append(add)
        continue

    if comando == 'remover':
        print(lista_total)
        print('lembrando que o primeiro indice e 0 qual dos itens voce deseja remover')
        print()
        remover = input('Remova: ')
        del lista_total[int(remover)]
        continue

    if comando == 'mostrar':
        print()
        print(lista_total)
        continue

    if comando == 'limpar':
        lista_backup = copy.deepcopy(lista_total)
        lista_total.clear()
        print()
        print('Lista limpa')
        continue

    if comando == 'recuperar':
        print()
        lista_total = copy.deepcopy(lista_backup)
        print(lista_total)

