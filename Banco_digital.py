def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios, nome, cpf, endereco):
    cpf_numeros = "".join(filter(str.isdigit, cpf))
    if any(usuario["cpf"] == cpf_numeros for usuario in usuarios):
        print("Já existe usuário com esse CPF.")
        return None
    usuario = {
        "nome": nome,
        "cpf": cpf_numeros,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário criado com sucesso.")
    return usuario

def criar_conta(usuarios, contas, cpf):
    cpf_numeros = "".join(filter(str.isdigit, cpf))
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf_numeros), None)
    if not usuario:
        print("Usuário não encontrado. Conta não criada.")
        return None
    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print("Conta criada com sucesso.")
    return conta

def main():
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta Corrente
[q] Sair

=> """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            endereco = input("Endereço (bairro - cidade): ")
            criar_usuario(usuarios, nome, cpf, endereco)

        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário para a conta: ")
            criar_conta(usuarios, contas, cpf)

        elif opcao == "q":
            break
        else:
            print("Operação inválida.")

if __name__ == "__main__":
    main()