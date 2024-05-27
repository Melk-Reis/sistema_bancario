
# Inicialização das variáveis
saldo = 0.00
extrato_hist = ""
limite_saque = 500
limite_saque_diario = 3
contador_saques = 0

print("\n\n")
print(" MENU DE OPERACOES BANCARIAS ".center(40,"="))


while True:
    print('''
            1 - Depósito
            2 - Saque
            3 - Consultar Extrato
            4 - Sair      ''')
    op_choice = int(input("\nSelecione uma operação: "))

    if op_choice == 1:
        # Operação de Depósito
        flag = 0
        print("\n\n")
        print(" Operação de deposito ".center(40,"-"))
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

        while flag == 0:
            valor = float(input("Digite o valor a ser depositado: "))
            if valor > 0 and valor < 5000:
                saldo += valor
                extrato_hist += f"Depósito de R$ {valor:.2f}\n" 
                print(f"\nSucesso.\nSeu novo saldo é: R$ {saldo:.2f}")
                print("Finalizando janela de depósito...\n")
                flag = 1
            else:
                flag = 0
                print("Erro - Digite um valor válido.")

    elif op_choice == 2:
        #Saque
        flag = 0
        if contador_saques >= 3:
            flag = 1
            print("\n\nLimite diário de saques atingido. Operação bloqueada")
        else:
            print("\n\n")
            print(" Operação de saque ".center(40,"-"))
            print(f"Seu saldo atual é: R$ {saldo:.2f}") 

        while flag == 0:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor >= 0 and valor <= limite_saque and valor <= saldo:
                saldo += (-valor)
                extrato_hist += f"Saque de R$ {valor:.2f}\n" 
                print(f"\nSucesso. \nSeu novo saldo é: R$ {saldo:.2f}")
                print("Finalizando janela de saque...\n")
                flag = 1
                contador_saques += 1
            else:
                flag = 0
                print("Erro - Digite um valor válido.")

    elif op_choice == 3:
        print(" Operação de extrato ".center(40,"-"))
        print(extrato_hist)
    elif op_choice == 4:
        break
    else:
        print("Opção incorreta. Certifique-se de digitar uma das opções do menu.")