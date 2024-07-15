from src.banco import cadastrar_usuario, cadastrar_conta, depositar, sacar, extrato
from datetime import datetime

# Função para validar data no formato DD/MM/AAAA
def validar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Função para validar CPF
def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

# Menu principal
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
            if not nome.replace(' ', '').isalpha():
                print('Nome inválido. O nome deve conter apenas letras, espaços e acentos.')
                continue

            data_nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')
            if not validar_data(data_nascimento):
                print('Data de nascimento inválida ou fora do formato DD/MM/AAAA.')
                continue

            cpf = input('Digite o CPF (somente números): ')
            if not validar_cpf(cpf):
                print('CPF inválido. O CPF deve conter exatamente 11 números.')
                continue

            endereco = input('Digite o endereço no formato (Logradouro, nº - Bairro - Cidade/UF): ')
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)

        elif escolha == '2':
            cpf = input('\nDigite o CPF (somente números) do usuário para vincular a conta: ')
            if not validar_cpf(cpf):
                print('CPF inválido. O CPF deve conter exatamente 11 números.')
                continue

            numero_conta = input('Digite o número da conta bancária: ')
            cadastrar_conta(cpf, numero_conta)

        elif escolha == '3':
            numero_conta = input('\nDigite o número da conta para depósito: ')
            valor = float(input('Digite o valor do depósito: '))
            depositar(numero_conta, valor)

        elif escolha == '4':
            numero_conta = input('\nDigite o número da conta para saque: ')
            valor = float(input('Digite o valor do saque: '))
            sacar(numero_conta=numero_conta, valor=valor)

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
