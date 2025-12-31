estoque = []

def cadastrar_produtos():
    nome = str(input("nome do produto: "))
    preco = float(input("preco: "))
    if preco <= 0:
        print("preco invalido")
        return
    quantidade = int(input("quantidade inicial: "))
    
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    
    estoque.append(produto)
    print("produto cadastrado com sucesso!\n")


def listar_produtos():
    if not estoque:
        print("estoque vazio")
        return
    
    for i, produto in enumerate(estoque):
        print(f"{i} - {produto['nome']} | "
              f"Preco: R${produto['preco']} | "
              f"Qtd: {produto['quantidade']}")
    print()


def entrada_produtos():
    if not estoque:
        print("estoque vazio\n")
        return
    
    listar_produtos()
    
    indice = int(input("qual o numero do produto: "))
    
    if indice <0 or indice >= len(estoque):
        print("produto invalido.\n")
        return
    
    quantidade = int(input("quantidade a adicionar: "))
    if quantidade <= 0:
        print("quantidade invalida.\n ")
        return
    
    estoque[indice]["quantidade"] += quantidade
    print("Entrada de estoque realizada com sucesso.\n")
    listar_produtos()
    
def saida_produtos():
    if not estoque:
        print("estoque vazio\n")
        return
    
    listar_produtos()
    
    indice = int(input("qual o numero do produto: "))
    if indice <0 or indice >= len(estoque):
        print("produto invalido.\n")
        return
    
    quantidade = int(input("quantidade a remover: "))
    if quantidade <= 0:
        print("quantidade invalida.\n ")
        return
    
    if quantidade > estoque[indice]["quantidade"]:
        print("quantidade maior que o estoque disponivel.\n")
        return

    estoque[indice]["quantidade"] -= quantidade
    print("Saida de estoque realizada com sucesso.\n")
    
    if estoque[indice]["quantidade"] <= 20:
        print("ALERTA!, produto com poucas unidades\n")
        
    listar_produtos()
    
while True:
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Entrada de Produto")
    print("4 - Saida de Produto")
    print("0 - Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        cadastrar_produtos()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        entrada_produtos()
    elif opcao == "4":
        saida_produtos()
    elif opcao == "0":
        break
    else:
        print("opcao invalida\n")