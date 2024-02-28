class CuentaAhorro:
    """--------------------------
    #Atributos
    -----------------------------"""
    saldoAhorro= 0
    interesMensual= 0
    """--------------------------
    #Metodos
    -----------------------------"""

    def SaldoAhorro(self):
        #Aqui va el codigo del metodo
        return self.saldoAhorro
    
    def ConsignarValor(self,saldoAhorro):
        nsaldoAhorro = self.saldoAhorro + ""
        self.saldoAhorro = nsaldoAhorro
        return "Ingrese nuevo valor" + ""
    def RetirarValor(self,saldoAhorro):
        nsaldoAhorro = self.saldoAhorro - ""
        self.saldoAhorro = nsaldoAhorro
        return "Ingrese valor a retirar" + ""
    
    