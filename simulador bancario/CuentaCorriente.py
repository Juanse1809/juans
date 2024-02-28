class CuentaCorriente:
    """----------------------------------
    #Atributos
    -------------------------------------"""
    saldoCorriente = 0
    """----------------------------------
    #Metodos
    -------------------------------------"""

    def SaldoCorriente(self):
        #Aqui va el codigo del metodo
        return self.saldoCorriente
    
    def ConsignarValor(self,saldoCorriente):
        nsaldoCorriente = self.saldoCorriente + ""
        self.saldoCorriente = nsaldoCorriente
        return "Ingrese nuevo valor" + ""
    def RetirarValor(self,saldoCorriente):
        nsaldoCorriente = self.saldoCorriente - ""
        self.saldoCorriente = nsaldoCorriente
        return "Ingrese valor a retirar" + ""
    