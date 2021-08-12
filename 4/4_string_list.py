# nome = 'Lucas ferreira'

# print(nome[0])

palavra = 'computador de mesa'
# for letra in palavra:
#     print(letra)
lista_da_palavra = list(palavra)

# print(palavra)
# print(lista_da_palavra)

# split, join

lista_splitada = palavra.split(' ') # divide e transfoma numa lista pelo separador

print(lista_splitada)

frase_remontada = '_'.join(lista_splitada) # remonta em uma string pelo delimitador

print(frase_remontada)