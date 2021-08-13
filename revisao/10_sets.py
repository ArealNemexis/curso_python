# estruturas, lineares, não ordenadados, que garante a mesma propriedade de acessos
# da lista, porem não permite itens duplicados,
# semelhante a conjuntos numericos da matematica, ps: não aceita somente numeros,#
# qualquer coisa é possivel incluir

conjunto = {1,2,4}
conjunto.add('lucas')
#print(conjunto.add('lucas'))
print(conjunto)

conjunto.add('lucas')
print(conjunto)

for item in conjunto:
    print(item)