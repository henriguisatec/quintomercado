

cadastro_cliente = []
cadastro_administrador = []

#loop principal do sistema
while True:
    #menu principal
    print('---------------------------------------------')
    print('          1-cadastrar                        ')
    print('          2-login cliente                    ')
    print('          3-login administrador              ')
    print('          0- sair                            ')
    print('---------------------------------------------')
    print()

    #opçoes de escolha do usuario
    opçao = input('digite a opçao desejada: ')

    #opçao cadastrar
    if opçao =='1':
        #exbir menu de cadastro 
        print()
        print('------------------------------------------')
        print('           1- cadastro de cliente         ')
        print('           2- cadastro do administrados   ')
        print('           0- voltar                      ')
        print('------------------------------------------')
        print()

        #opçoes de cadastro
        opçao1 = input('escolha a opçao de cadastro: ')
        #cadastro de cliente
        if opçao1 == '1':
            #informaçoes do cliente
            novo_usuario = {}
            novo_usuario['nome'] = input('Digite seu nome: ')
            novo_usuario['email'] = input('Digite seu email: ')
            novo_usuario['senha'] =input('Digite sua senha')  

            #adicionar novo cliente na linta
            cadastro_cliente.append(novo_usuario)
            print('Cadastro realizado com sucesso! ')

        #cadastro do administrador
        elif opçao1 == '2':
            #informaçoes do administrador
            novo_usuario = {}
            novo_usuario ['nome'] = input('Digite seu nome: ')
            novo_usuario ['email'] =  input('Digite seu email')
            novo_usuario ['senha'] = input('Digite sua senha ')
            novo_usuario ['codigo_de_seguranca'] = input('Digite seu codigo')
            #adicionar novo administrador
            cadastro_administrador.append(novo_usuario)
            print('Cadastro realizado com sucesso!\n')

        #voltar ao menu principal
        elif opçao1 == '0':
            print('voltar ao menu....')
        #opçao invalida
        else:
            print('opçao invalida.Por favor, escolha outra opçao.\n')
    
    #opçao login
    elif opçao == '2':
        #solicitar email e senha do cliente
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        
    #variaveis para verificar tipos de usuario encontrado
        usuario_encontrado = None
        tipo_usuario = None

    #verificaçao de cadastro de cliente
        for usuario in cadastro_cliente:
            if usuario['email'] == email and usuario['senha'] == senha:
                usuario_encontrado = usuario
                tipo_usuario = 'Cliente'
                break
    #se nao for cliente, verificar lista de admininstrador
    elif opçao == '3':
        #solicitar email, senha e codigo segurança
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        codigo_seguranca = input('digite seu codigo: ')
    #variaveis para verificar tipos de usuario encontrado
        usuario_encontrado = None
        tipo_usuario = None

        #verificaçao do login administrador
        
        for usuario in cadastro_administrador:
                if usuario['senha'] == senha and usuario ['codigo_de_seguranca'] == codigo_seguranca:
                    usuario_encontrado = usuario
                    tipo_usuario = 'administrador'
                    break
    #mensagen de boas vindas para o usuario encontrado 
        if usuario_encontrado:
            print(f'bem vindo(a), {usuario_encontrado['nome']}!\n')
        else:
           print('email, senha ou codigo incorreto. tente novamente.\n')

    elif opçao == '0':
        print('saindo do sitema.\n')
        break
    
