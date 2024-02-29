from CuentaAhorro import CuentaAhorro
from CuentaCorriente import CuentaCorriente
from CDT import CDT 

class SimuladorBancario:
    """----------------------
    #Atributos
    -------------------------"""
    cedula= 0
    nombre= 0
    mesActual= 0
    """----------------------
    #Asociaciones
    -------------------------"""
    cuentaAhorro = CuentaAhorro()
    cuentaCorriente = CuentaCorriente()
    CDT = CDT()
    """----------------------
    #Metodos
    -------------------------"""

    def consignarValor(self):
        #Aqui va el codigo del metodo
        #ValorConsignar + saldo = saldo
        #return "su saldo ahora es de: "+saldo
        return ""
    
    def RetirarValor(self):
        #Aqui va el codigo del metodo
        #ValorRetirar - saldo = saldo
        #return "su saldo disponible es de: "+saldo
        return ""
    
    def InteresMensual(self):
        #Aqui va el codigo del metodo
        return ""
    
    def ConsultarSaldoCorriente(self):
        #Aquin va el codigo del metodo
        return self.cuentaCorriente.ConsultarSaldo()

    def RetirarTodo(self, monto):
        #forma 1
        #self.cuentaAhorro.SaldoAhorro, self.cuentaCorriente.SaldoCorriente -= monto
        #forma 2
        # self.saldoAhorro self.saldoCorriente =self.saldoAhorro - self.saldoCorriente - monto
        #Forma 3
        #total = self.saldoAhorro - monto - self.saldoCorriente - monto
        #self.saldoAhorro, saldoCorriente = total
        total = self.CalcularSaldoTotal()
        self.cuentaCorriente.RetirarMonto(self.cuentaCorriente.ConsultarSaldo())
        self.cuentaAhorro.RetirarMonto(self.cuentaAhorro.ConsultarSaldo())       

        return "Retirar total: "+total
    
    def DuplicarAhorro(self):
        #Forma 1
        self.CuentaAhorro.ConsignarValor( self.CuentaAhorro.ConsultarSaldo())
        #Forma 2 
        # self.cuentaAhorro.saldo *= 2

    def ConsignarCuentaCorriente(self, saldo):
        #Aqui va el codigo del metodo
        #return self.saldoCorriente.consignarValor(saldo)
        self.CuentaCorriente.ConsignarValor(saldo)

    def CalcularSaldoTotal(self):
        #Aqui va el codigo del metodo¿
        return "El saldo total es de: "+self.CuentaAhorro.saldoAhorro() + self.cuentaCorriente.saldoCorriente()    

    def PasarAhorroaCorriente(self):
        #Forma 1
        # self.cuentaCorriente.ConsignarValor(self.cuentaAhorro.ConsignarValor())
        # self.cuentaAhorro.RetirarValor(self.cuentaAhorro.ConsultarSald())

        #Forma 2 
        # SaldoAhorro = self.cuentaAhorro.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(SaldoAhorro)
        # self.ahorros.RetirarValor(self, )

        #Forma 3
        return
    