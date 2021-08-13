#em codigo como faz um array de dicts?

# lista_alunos = [{'nome': 'daniel'}, {'nome': 'lucas'}]

# lista_alunos[0]['idade'] = 19
# print(lista_alunos)

#podemos usar input na estrutura dicts? ou append?

# meu_dict = dict()
# for _ in range(0, 2):
#     chave = input('digite a chave do campo: ')
#     valor = input('digite o valor do campo')
#     meu_dict[chave] = valor

# print(meu_dict)

dict_karen = {'nome': '', 'idade': -1}

nome = input('Digite seu nome: ')
dict_karen['nome'] = nome

idade = int(input('digite sua idade: '))

dict_karen['idade'] = idade

print(dict_karen)