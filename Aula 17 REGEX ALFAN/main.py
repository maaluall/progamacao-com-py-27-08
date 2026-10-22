# import re

# codigo = input("digite um código!")
# if re.fullmatch(r"[a-z0-9]{5}", codigo):
#     print("Código válido")
# else:
    
    # print("Código inválido!")


codigo = input("Digite um código!")

while not re.fullmatch(r"[a-z0-9]{5}", codigo):
    codigo = input("Digite o código novamente: ")
    
print("Código aceito!")
