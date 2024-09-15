saldo = 0
extrato = []

def depositar(valor):
    if valor > 0:
        print("Deposito feito com sucesso!")
        extrato.append(valor)
    else:
        print("Valor invalido para deposito!")
        valor  = 0
    return valor

while True:
    opcao = input("Digite a operação(deposito ='d' saque='s' sair ='q' extrato ='e'):")
    match opcao:
        case 'd':
            valor = float(input("Digite o valor a ser depositado:"))
            depositar(valor)
            
        case 'e':
            for valores in extrato:
                print(valores ,end=' ')
            print()
        case 'q':
            print("Adeus!!")
            break





