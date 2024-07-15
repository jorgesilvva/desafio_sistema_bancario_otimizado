from src.banco import cadastrar_cliente, cadastrar_conta, depositar, sacar, extrato

def menu():
    while True:
        print('\nMenu:\n')
        print('1. Cadastrar Cliente')
        print('2. Cadastrar Conta Bancária')
        print('3. Depositar')
        print('4. Sacar')
        print('5. Extrato')
        print('6. Sair')

        escolha = input('\nEscolha uma opção: ')

        if escolha == '1':
            nome = input('\nDigite o nome do cliente: ')
            cadastrar_cliente(nome)
        elif escolha == '2':
            cliente = input('\nDigite o nome do cliente para vincular a conta: ')
            numero_conta = input('Digite o número da conta bancária: ')
            cadastrar_conta(cliente, numero_conta)
        elif escolha == '3':
            numero_conta = input('\nDigite o número da conta para depósito: ')
            valor = float(input('Digite o valor do depósito: '))
            depositar(numero_conta, valor)
        elif escolha == '4':
            numero_conta = input('\nDigite o número da conta para saque: ')
            valor = float(input('Digite o valor do saque: '))
            sacar(numero_conta, valor)
        elif escolha == '5':
            numero_conta = input('\nDigite o número da conta para extrato: ')
            extrato(numero_conta)
        elif escolha == '6':
            print('Saindo do programa...')
            break
        else:
            print('\nOpção inválida. Por favor, escolha uma opção válida.')

if __name__ == '__main__':
    menu()
