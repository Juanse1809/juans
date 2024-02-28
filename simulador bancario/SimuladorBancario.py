from typing import Any
from CuentaAhorro import CuentaAhorro
from CuentaCorriente import CuentaCorriente

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
        return ""

    def RetirarTodo(self):
        return ""

    def DuplicarAhorro(self):
        return ""

    def ConsignarCuentaCorriente(self, saldo):
        #Aqui va el codigo del metodo
        return self.saldoCorriente.consignarValor(saldo)
    
    def CalcularSaldoTotal(self):
        #Aqui va el codigo del metodo¿
        return "El saldo total es de: "+self.cuentaAhorro.saldoAhorro() + self.cuentaCorriente.saldoCorriente()

    def PasarAhorroaCorriente(self):
        #Aqui va el codigo del metodo
        return CuentaAhorro  
    
    