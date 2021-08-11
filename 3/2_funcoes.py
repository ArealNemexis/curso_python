# def dois_xis(x):
#     return 2*x

# primeiro_valor = dois_xis(3)

# print(primeiro_valor)

def eh_par(numero_candidato):
    if numero_candidato % 2 == 0:
        return 'par'
    else:
        return 'impar'


paridade = eh_par(655)

print(paridade)
print(eh_par(655))
