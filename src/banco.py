import regex

usuarios = []
contas = []

# Função para cadastrar usuário
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    if not regex.match(r'^[\p{L} \s\'-]+$', nome):
        print('Nome de usuário inválido. Digite apenas letras e espaços.')
        return

    cpf_numeros = regex.sub(r'\D', '', cpf)  

    if any(user['cpf'] == cpf_numeros for user in usuarios):
        print('CPF já cadastrado para outro usuário.')
        return

    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf_numeros,
        'endereco': endereco
    })
    print(f'Usuário {nome} cadastrado com sucesso.')


# Função para cadastrar conta bancária
def cadastrar_conta(usuario_cpf, numero_conta):
    usuario_encontrado = None
    for user in usuarios:
        if user['cpf'] == usuario_cpf:
            usuario_encontrado = user
            break

    if usuario_encontrado:
        contas.append({
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario_encontrado,
            'saldo': 0.0,
            'movimentacoes': []
        })
        print(f'Conta bancária {numero_conta} cadastrada para o usuário {usuario_encontrado["nome"]}.')
    else:
        print(f'Usuário com CPF {usuario_cpf} não encontrado.')


# Função para realizar depósito
def depositar(numero_conta, valor):
    if valor <= 0:
        print('Valor de depósito inválido. O valor deve ser maior que zero.')
        return

    conta_encontrada = None
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break

    if not conta_encontrada:
        print(f'Conta bancária {numero_conta} não encontrada.')
        return

    conta_encontrada['saldo'] += valor
    conta_encontrada['movimentacoes'].append({
        'tipo': 'deposito',
        'valor': valor
    })
    print(f'Depósito de R$ {valor:.2f} realizado na conta {numero_conta}.')


# Função para realizar saque
def sacar(*, numero_conta, valor):
    if valor <= 0:
        print('Valor de saque inválido. O valor deve ser maior que zero.')
        return

    conta_encontrada = None
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break

    if not conta_encontrada:
        print(f'Conta bancária {numero_conta} não encontrada.')
        return

    if len(conta_encontrada['movimentacoes']) > 3:
        print('Limite de três saques diários atingido.')
        return

    if valor > 500:
        print('O valor do saque excede o limite máximo de R$ 500,00 por saque.')
        return

    if conta_encontrada['saldo'] < valor:
        print(f'Saldo insuficiente na conta {numero_conta} para realizar o saque.')
        return

    conta_encontrada['saldo'] -= valor
    conta_encontrada['movimentacoes'].append({
        'tipo': 'saque',
        'valor': valor
    })
    print(f'Saque de R$ {valor:.2f} realizado na conta {numero_conta}.')


# Função para exibir extrato
def extrato(numero_conta):
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            print(f'Extrato da conta {numero_conta}:')
            print(f"{'-' * 40}")
            print(f"{'Movimentações:':<30}")
            print(f"{'-' * 40}")
            for movimentacao in conta['movimentacoes']:
                if movimentacao['tipo'] == 'deposito':
                    print(f"{'Depósito de R$':<25} {movimentacao['valor']:.2f}")
                elif movimentacao['tipo'] == 'saque':
                    print(f"{'Saque de R$':<25} {movimentacao['valor']:.2f}")
            print(f"{'-' * 40}")
            print(f"{'Saldo atual:':<25} R$ {conta['saldo']:.2f}")
            print(f"{'-' * 40}")
            return
    print(f'Conta bancária {numero_conta} não encontrada.')


# Função para exibir extrato
def extrato(numero_conta):
    conta_encontrada = None
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break

    if not conta_encontrada:
        print(f'Conta bancária {numero_conta} não encontrada.')
        return

    print(f'Extrato da conta {numero_conta}:')
    print('-' * 40)

    movimentacoes = conta_encontrada['movimentacoes']

    if not movimentacoes:
        print('Movimentações:')
        print('Nenhuma movimentação realizada.')
    else:
        print('Movimentações:')
        print('-' * 40)
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
                print('-' * 40)
                if tipo == 'deposito':
                    print(f'Depósito de R$ {valor:.2f}')
                elif tipo == 'saque':
                    print(f'Saque de R$ {valor:.2f}')
            tipo_anterior = tipo

    print('-' * 40)
    print(f'Saldo atual: R$ {conta_encontrada["saldo"]:.2f}')
    print('-' * 40)
