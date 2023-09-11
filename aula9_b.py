import json


with open('aula9_b.json', 'r', encoding='utf8') as arquivo:
    dados_p1 = json.load(arquivo)


print(f'voce e:{dados_p1}')