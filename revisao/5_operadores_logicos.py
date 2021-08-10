# and/e
# comprar um carro
"""
tenho_dinheiro = False
preciso_de_um_carro = False

if tenho_dinheiro and preciso_de_um_carro: # para dar true no if todas as condições do and precisam ser verdadeiras
    print('Vou comprar meu carrão')
else:
    print('Deixa para uma proxima')
"""
"""
# or/ou
# indo ao mercado

tem_biscoito = True
tem_bombom = False
tem_chocolate = True

if tem_biscoito or tem_bombom: # o operador or depende que pelo menos uma condição seja verdadeira
    print('vou levar um dos dois')
else:
    print('melhor ir em outro mercado')

#    true             false = true         true = true
if (tem_biscoito or tem_bombom) and tem_chocolate: # o operador or depende que pelo menos uma condição seja verdadeira
    print('vou levar um dos dois')
else:
    print('melhor ir em outro mercado')

"""


"""
# == != > < >= <=


# == igualdade
# carro por senha
# nome_passado = 'Lucas'
# nome_que_abre_o_carro = 'Lucas'

# if nome_passado == nome_que_abre_o_carro:
#     print('destrancar porta')
# else:
#     print('voce nao é o dono desse carro')
"""


"""
# != diferença
# pet shop para cachorros

# pet_do_cliente = 'cachorro'

# if pet_do_cliente != 'cachorro':
#     print('nao atendemos outros pets')
# else:
#     print('que belo cão')
# """


"""
# > >= maior e maior igual
# academia para maiores de 65 anos
idade_cliente = 18

# if idade_cliente > 64:
#     print('seja bem vindo')
# else:
#     print('procure outra academia')

if idade_cliente >= 65:
    print('seja bem vindo')
else:
    print('procure outra academia')
"""

"""
# < <= menor e menor igual
# matine para menores de 17
idade_do_jovem = 20

if idade_do_jovem <= 17:
    print('aproveite sua festa livre de bebidas')
else:
    print('voce não pode entrar')
"""


"""
# not inverte o valor a ser condicionado

tem_cinto = True

if not tem_cinto:
    print('chamar manutenção')
else:
    print('carregar caminhão')
    """