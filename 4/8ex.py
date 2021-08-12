# escreva um programa que receba do usuario 10 numeros e guardeos em uma lista
# após isso dobre todos os valores da lista e mostrea na tela
# obs pode mostrar inteira ou item por item

def dobra(valor):
    return valor * 2

def dobra_lista(lista_de_transfomacao):
    for index in range(0, len(lista_de_transfomacao)):
        lista_de_transfomacao[index] = lista_de_transfomacao[index] * 2
    
    return lista_de_transfomacao

lista = []

for _ in range(0, 10): # 0 1 2 3 4 5 6 7 8 9
    input_atual = float(input('digite um numero'))
    lista.append(input_atual)


# for index in range(0, len(lista)):
#     lista[index] = dobra(lista[index])

#lista = dobra_lista(lista)

for index in range(0, len(lista)):
    lista[index] = lista[index] * 2


print(lista) 