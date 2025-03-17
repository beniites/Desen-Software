class Conta:
    def __init__(self,saldo:float,numero:int,agencia:str,cliente,historico):
        self.saldo  = saldo
        self.numero= numero
        self.agencia=agencia
        self.cliente = cliente
        self.historico = historico
    
    def info_saldo(self):
        return self.saldo
    
    def nova_conta(self, cliente, numero:int, conta):
        pass

    def sacar():
        pass

    def depositar():
        pass


class Conta_corrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite:float , limite_saque:float):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite = limite
        self.limite_saque = limite_saque


class Historco:
    def adicionar_tarnsacao():
        pass


class Cliente:
    def __init__(self,endereco:str, contas:list):
        self.endereco = endereco
        self.contas = contas

class Pessoa_Fisica(Cliente):
    def __init__(self, endereco, contas, cpf:str, nome:str):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome

class Transacao:
    def registrar_conta():
        pass

class Deposito(Transacao):
    def __init__(self,valor:float):
        pass

class Saque(Transacao):
    def __init__(self,valor:float):
        pass

