# Menu de opções para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>
"""

# Variáveis iniciais
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo de saque por operação
extrato = ""  # Histórico de transações
numero_saques = 0  # Contador de saques realizados
LIMITES_SAQUES = 1  # Limite máximo de saques permitidos por dia

# Loop principal do programa
while True:
    # Exibe o menu e solicita a escolha do usuário
    opcoes = input(menu)

    # Depósito
    if opcoes == "d":
        valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito
        if valor > 0:
            saldo += valor  # Atualiza o saldo com o valor do depósito
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona o depósito ao extrato
        else:
            print("Operação Falhou! O valor informado é inválido.")  # Mensagem de erro para valor inválido

    # Saque
    elif opcoes == "s":
        valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque

        # Verifica as condições para o saque
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo
        excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite permitido
        excedeu_saques = numero_saques >= LIMITES_SAQUES  # Verifica se o número de saques permitidos foi excedido

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")  # Mensagem de erro se o saldo for insuficiente
        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite.")  # Mensagem de erro se o saque exceder o limite
        elif excedeu_saques:
            print("Operação Falhou! Número máximo de saques excedido.")  # Mensagem de erro se o número de saques for excedido
        elif valor > 0:
            saldo -= valor  # Atualiza o saldo após o saque
            extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona o saque ao extrato
            numero_saques += 1  # Incrementa o contador de saques
        else:
            print("Operação Falhou! O valor informado é inválido.")  # Mensagem de erro para valor inválido

    # Extrato
    elif opcoes == "e":
        print("\n=================== Extrato ====================")
        # Exibe o extrato das transações realizadas ou uma mensagem caso não haja movimentações
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual
        print("==================================================")

    # Sair
    elif opcoes == "q":
        break  # Sai do loop principal e encerra o programa

    # Opção inválida
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")  # Mensagem de erro para opção inválida
