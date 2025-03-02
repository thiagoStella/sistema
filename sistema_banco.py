menu = """
### BANCO NACIONAL ###
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Insira o valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de: R$ {valor:.2f}\n"
        else:
            print("Operação não realizada, informe um valor válido!")

    elif opcao == "s":
        valor = float(input("Insira o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Voce não possui saldo suficiente")
        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite")
        elif excedeu_saque:
            print("Operação falhou! Nuero de tentativas excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de R$ {valor:.2}\n"
            numero_saque += 1
        else:
            print("O valor informado é invalido")
        
    elif opcao == "e":
        print("\n===== EXTRATO SIMPLIFICADO =====")
        print("Não foram realizadas movimentações no período." if not extrato else extrato)
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("=================================")
    elif opcao == "q":
        print("Saindo do sistema")
        break
    else:
        print("Opção Inválida")