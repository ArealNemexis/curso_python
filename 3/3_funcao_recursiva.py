def exponencial(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * exponencial(base, expoente - 1)