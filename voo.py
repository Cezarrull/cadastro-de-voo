cadastrosPessoa = dict()

pessoas = 0

while True:
    print('\nEscolha uma das opções a baixo: ')
    option = input('1 - cadastrar'
    '\n2 - informações'
    '\n\nopção: ')
    if option == '1':
        numPessoas = int(input('Número de pessoas que deseja cadastra: '))

        while pessoas < numPessoas:
            print(f'\n{pessoas + 1}° Pessoa')
            nome = input('Digite seu nome: ')
            cpf = input('Digite seu CPF: ')
            if cpf in cadastrosPessoa.keys():
                print('\nCPF inválido, por favor digite o seu CPF!')
            else:
                idade = input('Digite sua idade: ')
                cidade = input('Digite sua CIDADE ORIGEM: ')

                cadastrosPessoa[cpf] = {
                    'nome': nome,
                    'idade': idade,
                    'cidade Origem': cidade
                }
                pessoas += 1
    elif option == '2':
        while True:
            optionInfo = input('\n1 - cadastros de clientes'
            '\n2 - voos'
            '\n3 - sair'
            '\nopcão: ')
            if optionInfo == '1':
                print(cadastrosPessoa)
            elif optionInfo == '2':
                print('voos**')
            elif optionInfo == '3':
                break
            else:
                print('Digite somente as opções 1, 2 ou 3')
                input('Tecle enter para continuar')