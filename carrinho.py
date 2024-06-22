carrinho = []
print('----------------------carrinho de compras----------------------')
itn = str(input('Informe o produto que deseja adicionar ao carrinho de compra: '))
carrinho.append(itn)
print(carrinho)
opc = 1
while opc !=0: #adicionar produtos ao carrinho
    print('----------------------Adicionar produto----------------------')
    print('Deseja adicionar mais algum produto ao carrinho?: ')
    print('1. Sim')
    print('0. Não')
    print('-------------------------------------------------------------')
    opc = int(input('informe: '))
    if opc == 1:
        otp = input(str('Informe o produto: '))
        carrinho.append(otp)
        print(carrinho)
    if opc == 0:
        print('--------------Sem novos produtos adicionados--------------')
        
opc2 = 1 # menu principal 
while opc2 !=0:
    print('--------------------------Carrinho--------------------------')
    print('Qual ação deseja realizar agora?: ')
    print('1. Excluir')
    print('2. Produtos no carrinho')
    print('3. Adicionar')
    print('4. Finalizar compra')
    print('5. Cancelar compra')
    print('------------------------------------------------------------')
    kc = int(input('informe: '))
    if kc == 1: #excluir produtos do carrinho
        print('Excluir')
        ed = len(carrinho)
        print('----------------------Remover produto----------------------')
        print(carrinho)
        bola = input('Qual item deseja remover?: ')
        for i in range(ed):
            if carrinho[i]== bola:
                print('Item excluido', carrinho[i])
                carrinho.pop(i)
                break
    
    if kc == 2: #mostrar produtos no carrinho
        print('--------------------Produtos no carrinho--------------------')
        print('No carrinho: ')
        car = len(carrinho)
        for i in range(car):
            print(f'{i} - {carrinho[i]}')
    
    if kc == 3: #adicioar produtos ao carrinho
        print('----------------------Adcionar produto----------------------')
        prod = str(input('Informe o produdo: '))
        print(f'produto adicionado: {prod}')
        carrinho.append(prod)
        print(carrinho)
        cpo = 1
        while cpo !=0:
            print('deseja adicionar mais algum produto?')
            print('1. Sim')
            print('0. Não')
            kol = int(input('informe: '))
            if kol == 1:
                twix = str(input('informe o produto: '))
                carrinho.append(twix)
                print(carrinho)
            if kol == 0:
                print('------------------Nem um produto adicionado------------------')
                break

                
    
    # lista para produto + preço
    oloco = {   
        'nome': 'tomate',
        'preço':'5.00'
    }
    qiso = {
        'nome': 'manga',
        'preço': '4.00'
    }
    loto = []
    loto.append(oloco)
    loto.append(qiso)
    for i in range(len(oloco)):
        print(i)

    po = {}

    lista = [
        {
            'nome': 'maça',
            'preco': '5.00',
            'cor': 'vermelho',
            'categoria': 'fruta',
            'quantidade': '1'
        },
        {
            'nome': 'arroz',    
            'preco': '10.00',
            'cor': 'branco',
            'categoria': 'alimento',
            'quantidade': '2'
        },
        {
            'nome': 'feijao',   
            'preco': '8.00',
            'cor': 'preto',
            'categoria': 'alimento',
            'quantidade': '1'
        }
        ]
    if kc == 4:
        print('finalizar produto')
        for i in range(len(lista)):
            print(f'nome: {lista[i]["nome"]}, {lista[i]['preco']}')




    
    
        

    





