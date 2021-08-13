meu_cadastro2 = {
    'idade': 20,
    'materias': ['lfa', 'calculo 1', 'estruturas de dados'],
    'matriculado': True,
    'nome': 'Lucas',
    'pai':{"nome": 'Erasmo'},
    'mae': {'nome': 'Regina'},
    'data de nascimento': ('04/09/2000')
    }

idade = meu_cadastro2.get('idade')

#print(meu_cadastro2.keys())
#print(meu_cadastro2.values())

# for chave, valor in meu_cadastro2.items(): #iterar sobre meu dict
#     print(f'a chave {chave} possui o valor {valor}')

# for chave, valor in meu_cadastro2.items():
#     if chave == 'materias':
#         for materia in valor:
#             print(materia)

# for chave, valor in meu_cadastro2.items():
#     if chave == 'pai':
#         print(valor.keys())

