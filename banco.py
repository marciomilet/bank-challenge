saldo = 50.0
extrato = []
opcao_selecionada = ''
valor_selecionado = 0

def operacao():
    valor_operacao = float(input(print(f"Digite o valor para {opcao_selecionada}:")))
    return valor_operacao

def depositar(valor) -> float:
    if valor > 0:
        print("Deposito feito com sucesso!")
        extrato.append(valor)
    else:
        print("Valor invalido para deposito!")
        valor  = 0
    return valor

def sacar(valor,saldo) -> float:
    if valor <= saldo:
        extrato.append(-valor)
        print("Saque feito com sucesso!")
    else:
        print("Saldo Insuficiente!")
        valor = 0
    return valor

while True:
    opcao = input("Digite a operação(deposito ='d' saque='s' sair ='q' extrato ='e' saldo = 'sa' sair = 'q'):")
    match opcao:
        case 'd':
            opcao_selecionada = 'deposito'
            valor_selecionado = operacao()
            saldo += depositar(valor_selecionado)
        case 's':
            opcao_selecionada = 'saque'
            valor_selecionado = operacao()
            saldo -= sacar(valor_selecionado,saldo)    
        case 'e':
            for valores in extrato:
                print(valores ,end=' ')
            print()
        case 'sa':
            print(saldo)
        case 'q':
            print("Adeus!!")
            break
        