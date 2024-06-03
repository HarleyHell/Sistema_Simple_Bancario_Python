#Sistema simples para saque, deposito e extrato.

menu = """

[1] Deposito
[2] Saque
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito:"))

        if  valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Deposito não realizado, informe um valor valido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada, saldo insuficiente.")
    
        elif excedeu_limite:
            print("Operação não realizada, valor excede o limite.")
    
        elif excedeu_saques:
            print("Operação não realizada, excedeu o limite de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saque += 1
            print("Saque realizado com sucesso.")

        else:
            print("Saque não realizado, informe um valor valido.")
    
    elif opcao == "3":
        print("\n################### EXTRATO ###################")
        print("Não existem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("###############################################")
    
    elif opcao == "0":
        break

else:
    print("Operação invalida, por favor selecione novamente no menu.")