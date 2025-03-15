from abc import ABC, abstractclassmethod,
abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n\tOperação falhou!, Você não tem saldo suficeinte!")

        elif valor > 0:
            self._saldo -= valor
            Print("\n\tSaque realizado com sucesso!")
            return True

        else:
            Print("\n\tO valor informado é invalido")
        return False
    
    def depoisitar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n\tDepósito realizado com sucesso!")
        else:
            print("\n\tOperação falhou,valor invalido")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes 
            if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor >self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou Ovalor do saque excede o limite")
        
        elif excedeu_limite:
            print("Numero máximo de saques excedido")
        
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return  f"""\
            Agência: \t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self_.transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data":datetime.now().strftime
                ("%d-%m-%Y %H:%M"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self):
        self._valor = ValueError

        @property
        def valor(self):
            return self._valor

        def registrar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)
            
            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)





def menu():
    menu = """\n
    ========== MENU ==========
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [N] Nova Conta
    [L] Lista Contas
    [U] Novo Usuário
    [Q] Sair
    ==========================
    """
    return input(menu).lower()  # Converte a entrada para minúsculas

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito de: \t\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação não realizada, o valor informado é inválido!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    LIMITE_SAQUES = 3
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Voce não possui saldo suficiente")
    elif excedeu_limite:
        print("Operação falhou! Valor do saque excede o limite")
    elif excedeu_saque:
        print("Operação falhou! Nuero de tentativas excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque no valor de \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("O valor informado é invalido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO SIMPLIFICADO =====")
    print("Não foram realizadas movimentações no período." if not extrato else extrato)
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("=================================")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf(somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usario com esse CPF!")
        return

    nome = input("Informe o Nome Completo: ")
    data_nascimento = input("Informa a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro -  bairro - cidade): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuario criado com sucesso!!!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf(somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    else:
        print("Usuario não encontrado, fluxo de criação de conta encerrado!")
        return None  # Retorna None se o usuário não for encontrado

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" *100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Insira o valor a ser depositado:"))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Insira o valor do saque:"))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUES,
            )
            numero_saques += 1  # Incrementa o número de saques

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo do sistema")
            break
        else:
            print("Opção Inválida")
# correção da branch
main()