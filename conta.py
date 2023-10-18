class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))
        
    def deposito(self, valor):
        self.__saldo += valor
        
    def saque(self, valor):
        if valor <= self.__saldo + self.__limite:
            self.__saldo -= valor
            print("Operação realizada com sucesso, nova saldo: {}".format(self.__saldo + self.__limite))
        else:
            print("Impossivel sacar valor, saldo disponivel para saque: {}".format(self.__saldo + self.limite))
        
    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
    
    @property    
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def conta(self):
        return self.__numero
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}