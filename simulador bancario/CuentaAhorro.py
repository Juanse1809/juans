class CuentaAhorro:
    """--------------------------
    #Atributos
    -----------------------------"""
    saldoAhorro = ""
    interesMensual = ""
    """--------------------------
    #Metodos
    -----------------------------"""

    def ConsultarSaldo(self):
        return self.saldo

    def SaldoAhorro(self):
        #Aqui va el codigo del metodo
        return self.saldoAhorro
    
    def ConsignarValor(self,valor):
        # #Forma 1
        # self.saldo += monto
        # # Forma 2
        # self.saldo = self.saldo + monto
        # # Forma 3
        # total = self.saldo + monto
        # self.saldo = total

        nsaldoAhorro = self.saldoAhorro + ""
        self.saldoAhorro = nsaldoAhorro
        return "Ingrese nuevo valor" + ""
    
    def RetirarMonto(self, monto):
        # #Forma 1
        # self.saldo -= monto
        # # Forma 2
        # self.saldo = self.saldo - monto
        # # Forma 3
        total = self.saldo - monto
        self.saldo = total
    