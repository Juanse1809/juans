class Empleado:
    """-------------------------------
    #Atributos
    ----------------------------------"""
    nombre= "Carlos"
    apellido= "Mina"
    """-------------------------------
    #1 Masculino y 2 Femenino
    ----------------------------------"""
    sexo=0
    salario=0
    """-------------------------------
    #Metodos
    ----------------------------------"""

    def CambiarSalario(self, nuevoSalario):
        #Aqui va el codigo del metodo
        return 0

    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        #Aqui va el codigo del metodo
        return None 
    
    def ConsultarSalario(self):
        #Aqui va el codigo del metodo
        return self.salario
    
    def ConsultarNombre(self):
        #Aqui va el codigo del metodo 
        return self.nombre
    
    def ConsultarApellido(self):
        #Aqui va el codigo del metodo
        return self.apellido

    def ConsultarNombreCompleto(self):
        #Aqui va el codigo del metodo
        return self.nombre +" "+self.apellido
    
    def AumentoSalario(self):
        nSalario= self.salario * 0.05
        nSalario= nSalario + self.salario
        self.salario = nSalario 

        return "El nuevo salario es de: "+self.salario 
    
    