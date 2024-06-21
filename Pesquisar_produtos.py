produtos = []

def adicionar_produtos(nome, preco, quantidade):
    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})

adicionar_produtos('arroz', 15.00, 10)
adicionar_produtos('feijão', 7.00, 10)
adicionar_produtos('açúcar', 8.00, 10)

def pesquisar_produtos(nome):
    cont = 1
    for produto in produtos:
        if nome == produto["nome"]:
            print(f'Item localizado {cont}: ', produto["nome"])
            break
        cont += 1
    else:
        print(f'Produto "{nome}" não encontrado.')

nome = input(str('Digite o nome do produto: '))
pesquisar_produtos(nome)
