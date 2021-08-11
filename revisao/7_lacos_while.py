# o laço while é utilizado em conjunto a uma expressão condicional, para repetições que não sabemos
# quantas vezes serão repetidas

senha_correta = '123'
senha = ''
while senha != senha_correta:
    senha = input('Digite a senha')

print('Senha correta, acesso concedido')