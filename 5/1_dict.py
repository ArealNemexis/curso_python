from pprint import pprint

# estrutura de dados não linear, que utiliza do conceito chave valor para indexamento
# permite aninhamento
# pode ser iteravel
# utiliza a sintaxe de indexamento numerico com a chave dentro 'meu_cadastro['nome']'
# até o python3.6 ele é era desordenado, a partir do 3.7  garantiu-se a ordenação


meu_cadastro = dict()

meu_cadastro['nome'] = 'Lucas'
meu_cadastro['idade'] = 20
meu_cadastro['matriculado'] = True
meu_cadastro['materias'] = ['lfa', 'calculo 1', 'estruturas de dados']

#pprint(meu_cadastro)

meu_cadastro2 = {
    'idade': 20,
    'materias': ['lfa', 'calculo 1', 'estruturas de dados'],
    'matriculado': True,
    'nome': 'Lucas',
    'pai':{"nome": 'Erasmo'},
    'mae': {'nome': 'Regina'},
    'data de nascimento': ('04/09/2000')
    }
pprint(meu_cadastro2)