def formata_aluno(nome, idade, estado):
    return f'O aluno {nome} que tem {idade} reside no {estado}'

nome = input('Digite seu nome: ')
idade = int(input('digite sua idade: '))
estado_onde_mora = input('Digite o estado residente: ')

# print(nome)
# print(idade)
# print(estado_onde_mora)
#                                                     0      1        2
#print("O aluno {1} que tem {2} reside no {1}".format(nome, idade, estado_onde_mora))


#Fstrings
#print(f"O aluno {nome} que tem {idade} reside no {estado_onde_mora}")

# apresentacao_aluno = formata_aluno(nome, idade, estado_onde_mora)

# print(apresentacao_aluno)

# terminou_em = input(f'voce tem {idade} anos, ja terminou o ensino medio')

# print(terminou_em)

## strings multilinha que tambem servem de comentario
# print("""
# ola
# pulei linha
# pulei de novo
# finalizando
# """)