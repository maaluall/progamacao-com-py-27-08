'''
def cadastrar_usuario(idade=18, nome = "João",
                      cidade="Amoreira")

'''
numero = 20 #variável global
def calcular():
    numero = 10 #variável local
calcular()
print(numero)


saldo = 5000
def deposito():
    global saldo
    saldo = saldo + 100
    return saldo
print(deposito())