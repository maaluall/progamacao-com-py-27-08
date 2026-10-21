personagens = []

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    classe = input("Digite a classe do seu personagem: ")
    nivel = int(input("Digite o nível do seu personagem: "))
    
# Dicionario em py sig: chave - valor... ex: "nome": "Bob Esponja"

    personagem = {
       "nome": nome,
       "classe": classe,
      "nivel": nivel
    }
    personagens.append(personagem)
    
    #print("DADOS DO PERSONAGEM")
    #print("Nome: ", personagem["nome"])
    #print("Classe: ", personagem["classe"])
    #print("Nível: ", personagem["nivel"])
    
quantidade = int(input("Quantos personagens criar?: "))

for i in range(quantidade):
    print(f"Criando personagem {i + 1}")
    criar_personagem()
    
print("---LISTA FINAL DE PERSONAGENS CRIADOS---")
for personagem in personagens:
    print("Nome", personagem["nome"])
    print("Classe", personagem["classe"])
    print("Nível", personagem["nivel"])
    print()
    
    
    
    