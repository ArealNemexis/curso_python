# escreva um programa simples com 2 funcoes, somar e dividir, 
# receba dois numeros e pergunte ao usuario qual operacao ele deseja fazer
# exiba o resultado da funcao com a frase que desejar a frente, utilizando fstring ou format

"""
TODO INPUT TRAZ UMA STRING

int(input('pergunta'))

f'{nome_variavel}'

def nomefuncao(parametro1, parametro2):
    return

if condicao:

else:


QUEM FOR TERMINANDO DIGITE NO CHAT
"""

def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def dividir(primeiro_numero, segundo_numero):
    resultado = primeiro_numero / segundo_numero
    return resultado


n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))

operacao = int(input("""
Digite 1 para divisao ou 2 para soma """))

if operacao == 1:
    resultado = dividir(n1, n2)
    print('o resultado da divisao é {}'.format(resultado))

if operacao == 2:
    print(f'o resultado da soma é {somar(n1, n2)}')