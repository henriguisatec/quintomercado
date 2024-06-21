produtos =[]

def adicionar_produtos(nome, preco, quantidade):
  produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})

adicionar_produtos('arroz', 15.00, 10)
adicionar_produtos('feijao', 7.00, 10)
adicionar_produtos('acucar', 8.00, 10)

def pesquisar_produtos(nome):
  cont = 1
  for produto in produtos:
    if nome == produto["nome"]:
      print(f'Item localizado {cont}: ', produto["nome"])
      break
    cont += 1

nome = input(str('Digite o nome do produto: '))
pesquisar_produtos(nome)
