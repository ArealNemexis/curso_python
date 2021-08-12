#permite indexamento, contagem, iteracao IMUTAVEL
minha_tupla_imutavel = (3.14, 9.8, 3, 20, 3.14, 6.38)
tupla = tuple(3.4,9.8,3)
qtd_pi = minha_tupla_imutavel.count(3.14)

indx = minha_tupla_imutavel.index(3)

# print(indx)

for const in minha_tupla_imutavel: # iterar
    print(const)