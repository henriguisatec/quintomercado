#sistema de compra

#codigo do adm

lista = []
print(lista)
while exit != 6:
    print("        Bem vindo ao Quinto Mercado.         ")
    print(" ")
    print("O que você deseja fazer hoje?: ")
    print("1. Cadastro de um novo produto.")
    print("2. Editar dados de um produto.")
    print("3. Excluir um produto.")
    print("4. Listar todos os produtos.")
    print("5. Adicionar descontos.")
    print("6. Sair do programa.")
    print("---------------------------------")
    entrada = int(input("Insira o número da opção desejada: "))
    if entrada < 0 or entrada > 6:
        print("O número não é uma opção.")
        print(" ")
    if entrada == 1:
        print("Opção 1 - Cadastro de produtos")
        if len(lista) == 0:
                nome = str(input("Insira o nome do produto: "))
                cor = str(input("Insira a cor do produto: "))
                preço = float(input("Insira o preço do produto: "))
                catego = input("Insira a categoria do produto: ")
                qtd = int(input("Insira a quantidade de itens: "))
                novoproduto = {
                    'nome': nome,
                    'cor': cor,
                    'preço': preço,
                    'categoria': catego,
                    'quantidade': qtd
                 }
                lista.append(novoproduto)
                print("O novo produto foi adicionado a lista com sucesso.")
        else:
            nome = str(input("Insira o nome do produto: "))
            for i in range(len(lista)):
                if nome == (lista[i]['nome']):
                    print("O produto já foi cadastrado.")
                else:
                    cor = str(input("Insira a cor do produto: "))
                    preço = float(input("Insira o preço do produto: "))
                    catego = input("Insira a categoria do produto: ")
                    qtd = int(input("Insira a quantidade de itens: "))
                    novoproduto = {
                        'nome': nome,
                        'cor': cor,
                        'preço': preço,
                        'categoria': catego,
                        'quantidade': qtd
                    }
                    lista.append(novoproduto)
                    print("O novo produto foi adicionado a lista com sucesso.")
    elif entrada == 2:
        if (len(lista)) == 0:
            print("Sua lista está vazia.")
            break
        for i in range (len(lista)):
            print(i, "-", lista[i])
        indice = int(input("Insira indice do produto que você deseja editar: "))
        print(lista[indice]) #imprime a posição do indice
        print(" ")
        leave = 0
        while leave!=6:
            print("Qual informação que você deseja editar: ")
            print("1. Nome.")
            print("2. Cor.")
            print("3. Preço.")
            print("4. Categoria.")
            print("5. Quantidade.")
            print("6. Sair.")
            editar = int(input("Insira o número da opção correspondente: "))
            if entrada < 0 or entrada > 6:
                print("O número não é uma opção.")
                print(" ")
            if editar == 1:
                for i in range (len(lista)):
                    print(lista[indice])
                new = str(input("Insira o novo nome: "))
                novoproduto['nome'] = new
                for i in range (len(lista)):
                    print(lista[indice])
                print("O nome foi alterado com sucesso para:", new)
                print(" ")
            if editar == 2:
                for i in range (len(lista)):
                    print(lista[indice])
                new = str(input("Insira a nova cor: "))
                novoproduto['cor'] = new
                for i in range (len(lista)):
                    print(lista[indice])
                print("A cor foi alterada com sucesso para:", new)
                print(" ")
            if editar == 3:
                for i in range (len(lista)):
                    print(lista[indice])
                new = float(input("Insira o novo preço: "))
                novoproduto['preço'] = new
                for i in range (len(lista)):
                    print(lista[indice])
                print("O preço foi alterado com sucesso para:", new)
                print(" ")
            if editar == 4:
                for i in range (len(lista)):
                    print(lista[indice])
                new = str(input("Insira a nova categoria: "))
                novoproduto['catego'] = new
                print(lista[indice])
                print("A categoria foi alterada com sucesso para:", new)
                print(" ")
            if editar == 5:
                for i in range (len(lista)):
                    print(lista[indice])
                new = int(input("Insira a quantidade: "))
                novoproduto['quantidade'] = new
                print(lista[indice])
                print("A quantidade foi alterada com sucesso para:", new)
                print(" ")
            if editar == 6:
                sair = str(input("Tem certeza que quer sair da edição?: (S/N) "))
                if sair == "S" or sair == 's':
                    leave = 6
                elif sair == "N" or sair == "n":
                    leave = 0
                else:
                    print("Essa opção é invalida.")
    elif entrada == 3:
        if (len(lista)) == 0:
            print("Sua lista está vazia.")
            break
        print('Qual o item que você deseja excluir?: ')
        for i in range (len(lista)):
            print(i, "-", lista[i])
        itemparaexc = int(input("Insira o indice do item: "))
        lista.pop(itemparaexc)
        print("Item removido com sucesso!")
        print("Lista atual: ",i, "-", lista[i])
    elif entrada == 4:
        if (len(lista)) == 0:
            print("Sua lista está vazia.")
            break
        for i in range (len(lista)):
            print(i, "-", lista[i])
        print("Sua lista atual é: ",i, "-", lista[i])
        print("Possui", len(lista),"itens.")
    elif entrada == 5:
        print("Adicionar descontos.")
        desc = int(input("Insira o percentual de desconto: "))
        print(lista)
        prod = int(input("Insira o indice do produto a ser descontado: "))
        valorprod = (lista[prod]['preço'])-(lista[prod]['preço'])*(desc/100)
        print (valorprod)
        (lista[prod]['preço']) = round(valorprod, 2)
        print(lista[prod])
    elif entrada == 6:
        exit = 6