class CuentaCorriente:
    """----------------------------------
    #Atributos
    -------------------------------------"""
    saldoCorriente = 0
    """----------------------------------
    #Metodos
    -------------------------------------"""

    def ConsultarSaldo(self):
        return self.saldo
    
    def SaldoCorriente(self):
        #Aqui va el codigo del metodo
        return self.saldoCorriente
    
    def ConsignarValor(self,saldoCorriente):
# #Forma 1
        # self.saldo += monto
        # # Forma 2
        # self.saldo = self.saldo + monto
        # # Forma 3
        # total = self.saldo + monto
        # self.saldo = total

        nsaldoCorriente = self.saldoCorriente + ""
        self.saldoCorriente = nsaldoCorriente
        return "Ingrese nuevo valor" + ""
    
    def RetirarMonto(self,Monto):
        # #Forma 1
        # self.saldo -= monto
        # # Forma 2
        # self.saldo = self.saldo - monto
        # # Forma 3
        # total = self.saldo - monto
        # self.saldo = total

        nsaldoCorriente = self.saldoCorriente - ""
        self.saldoCorriente = nsaldoCorriente
        return "Ingrese valor a retirar" + "" 