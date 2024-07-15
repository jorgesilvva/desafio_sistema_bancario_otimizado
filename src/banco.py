import regex

clientes = {}
contas = {}


def cadastrar_cliente(nome):
    if regex.match(r'^[\p{L} \s\'-]+$', nome):
        clientes[nome] = []
        print(f'Cliente {nome} cadastrado com sucesso.')
    else:
        print('Nome de cliente inválido. Digite apenas letras.')


def cadastrar_conta(cliente, numero_conta):
    if cliente in clientes:
        contas[numero_conta] = {
            'cliente': cliente,
            'saldo': 0.0,
            'movimentacoes': []
        }
        clientes[cliente].append(numero_conta)
        print(f'Conta bancária {numero_conta} cadastrada para o cliente {cliente}.')
    else:
        print(f'Cliente {cliente} não encontrado.')


def depositar(numero_conta, valor):
    if valor <= 0:
        print('Valor de depósito inválido. O valor deve ser maior que zero.')
    elif numero_conta in contas:
        contas[numero_conta]['saldo'] += valor
        contas[numero_conta]['movimentacoes'].append({
            'tipo': 'deposito',
            'valor': valor
        })
        print(f'Depósito de R$ {valor:.2f} realizado na conta {numero_conta}.')
    else:
        print(f'Conta bancária {numero_conta} não encontrada.')


def sacar(numero_conta, valor):
    if numero_conta in contas:
        if valor <= 0:
            print('Valor de saque inválido. O valor deve ser maior que zero.')
        elif contas[numero_conta]['saldo'] >= valor:
            if len(contas[numero_conta]['movimentacoes']) > 3:
                print('Limite de saques diários atingido.')
            elif valor > 500:
                print('O valor do saque excede o limite máximo de R$ 500,00 por saque.')
            else:
                contas[numero_conta]['saldo'] -= valor
                contas[numero_conta]['movimentacoes'].append({
                    'tipo': 'saque',
                    'valor': valor
                })
                print(f'Saque de R$ {valor:.2f} realizado na conta {numero_conta}.')
        else:
            print(f'Saldo insuficiente na conta {numero_conta} para realizar o saque.')
    else:
        print(f'Conta bancária {numero_conta} não encontrada.')


def extrato(numero_conta):
    if numero_conta in contas:
        print(f'Digite o número da conta para extrato: {numero_conta}')
        print(f"Extrato da conta {numero_conta}:\n")

        movimentacoes = contas[numero_conta]['movimentacoes']

        if not movimentacoes:
            print('Movimentações:')
            print('Nenhuma movimentação realizada.')
        else:
            print('Movimentações:')
            print('-' * 30)  # Linha pontilhada antes do primeiro grupo de movimentações
            tipo_anterior = None
            for movimentacao in movimentacoes:
                tipo = movimentacao['tipo']
                valor = movimentacao['valor']
                if tipo == tipo_anterior or tipo_anterior is None:
                    if tipo == 'deposito':
                        print(f'Depósito de R$ {valor:.2f}')
                    elif tipo == 'saque':
                        print(f'Saque de R$ {valor:.2f}')
                else:
                    print('-' * 30)  # Linha pontilhada entre grupos de movimentações
                    if tipo == 'deposito':
                        print(f'Depósito de R$ {valor:.2f}')
                    elif tipo == 'saque':
                        print(f'Saque de R$ {valor:.2f}')
                tipo_anterior = tipo

            print('-' * 30)  # Linha pontilhada antes do saldo atual
            print(f'Saldo atual: R$ {contas[numero_conta]["saldo"]:.2f}')
    else:
        print(f'Extrato da conta {numero_conta}:\n')
        print(f'Conta bancária {numero_conta} não encontrada.')
