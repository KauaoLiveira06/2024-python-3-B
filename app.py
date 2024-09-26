import os

clientes = []

def nome_clientes():
    print('Cadastrar Clientes')
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')
    telefone = input('Digite o telefone do cliente: ')

    cliente = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'ativo': True
    }

    clientes.append(cliente)
    print('Cliente cadastrado com sucesso!')

def listar_clientes():
    print('Listar Clientes')
    if clientes:
        for idx, cliente in enumerate(clientes):
            status = 'Ativo' if cliente['ativo'] else 'Inativo'
            print(f"{idx + 1}. Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}, Status:{status}")

    else:
            print('Nenhum cliente cadastrado.\n')

def ativar_clientes():
    print('Ativar/Desativar Clientes')
    listar_clientes()
    if clientes:
        try:
            cliente_id = int(input('Escolha o número do cliente para ativar/desativar: '))
            if 1 <= cliente_id <= len(clientes):
                cliente = clientes[cliente_id - 1]
                cliente['ativo'] = not cliente['ativo']
                print(f"Cliente {cliente['nome']} agora está {'Ativo' if cliente['ativo'] else 'Inativo'}.\n")
            else:
                print('Cliente  não encontrado!\n')
        except ValueError:
            print('Entrada inválida! Por favor, insira um número válido.\n')

def sair_aplicação():
    print('Sair da Aplicação')
    exit()

def mostrar_menu():
    print('''
    Company papelaria & embalagens
    
    1. Cadastro de clientes
    2. Lista de clientes
    3. Ativar clientes
    4. Sair da aplicação
    
    '''
    )

while True:
    mostrar_menu()
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            nome_clientes()
        elif opcao_escolhida == 2:
            listar_clientes()
        elif opcao_escolhida == 3:
            ativar_clientes()
        elif opcao_escolhida == 4:
            sair_aplicação()
            break
        else:
            print('Opção Inválida')
    except ValueError:
        print('Entrada Inválida! Digite um número.')