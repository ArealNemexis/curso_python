# maneiras de declarar uma lista
lista1 = ['lucas', 1.75, 20, 20, 20, 20]
lista2 = list('lucas', 1.75, 20, 20, 20, 20)
print(lista1)

lista1.append(True)

print(lista1)

lista1.remove(20)

print(lista1)

print(lista1.pop(1))

print(lista1)

qtd_vinte = lista1.count(20)
print(qtd_vinte)
# adicionar ao fim lista1.append(True)
# remover a primeira ocorrencia de um dado na lista lista1.remove(20)
# remove um item no index passado, caso não passe remove o ultimo item lista1.pop(1) 
# conta quantos itens tem dentro da lista lista1.count(20)