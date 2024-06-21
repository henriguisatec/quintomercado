produtos = [ ]

def adicionar_produtos (nome, preco, quantidade):
    produtos.append(produtos)

adicionar_produtos('arroz',70, 10)
adicionar_produtos("")
adicionar_produtos("")

def pesquisar_produtos (nome):
    cont = 1
    for produto in produtos:
        if nome == produtos ['nome']:
            print(f'Item localizado {cont}: ', produtos ['nome'])
            break
        cont+=1
nome = input(str('Digite o nome dp produto: '))
pesquisar_produtos(nome)