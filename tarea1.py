class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("Monto inválido para depositar.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Monto inválido para retirar.")

    def obtener_saldo(self):
        return self.__saldo
    
if __name__ == "__main__":
    cuenta = CuentaBancaria()
    print("Saldo inicial:", cuenta.obtener_saldo())  

    cuenta.depositar(100)
    print("Saldo después de depositar $", cuenta.obtener_saldo()) 

    cuenta.retirar(30)
    print("Saldo después de retirar $30 -> $", cuenta.obtener_saldo()) 

    cuenta.retirar(100)
    print("Saldo final: -> $", cuenta.obtener_saldo())
