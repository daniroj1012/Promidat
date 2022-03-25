from datetime import datetime
import os 


class Cliente:
    
    def __init__(self,nombrecliente,direccioncliente,telefonocliente):
        self.__nombrecliente=nombrecliente
        self.__direccioncliente=direccioncliente
        self.__telefonocliente=telefonocliente
       
    @property
    def nombrecliente(self):
        return self.__nombrecliente
    
    @property
    def direccioncliente(self):
        return self.__direccioncliente

    @property
    def telefonocliente(self):
        return self.__telefonocliente 

    @nombrecliente.setter
    def nombrecliente(self,valor):
        self.__nombrecliente=valor

    @direccioncliente.setter
    def direccioncliente(self,valor):
        self.__direccioncliente=valor

    @telefonocliente.setter
    def telefonocliente(self,valor):
        self.__telefonocliente=valor

    def __str__(self):
        return 'Nombre: '+self.__nombrecliente +'\nDireccion: ' +self.direccioncliente + '\nTelefono: ' + self.telefonocliente

class Ciudad:
    def __init__(self,salida,destino): 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S") # Quiero que cuando se cree el objeto se asocie la hora actual
        self.__salida_destino= 'Salida: '+ salida + ' Destino: ' + destino
        self.__horaactual=current_time

    @property
    def salida_destino(self):
        return self.__salida_destino

    @property
    def horaactual(self):
        return self.__horaactual

    @salida_destino.setter
    def salida_destino(self,salida,destino):
        self.__salida_destino='Salida: '+ salida + ' Destino: ' + destino    
    
    def __str__(self):
        return self.__salida_destino + '\nHora:' +' '+ self.__horaactual

class Alimentoextra:
    def __init__(self,codigo,descripcion,precio):
        self.__codigo=codigo
        self.__descripcion=descripcion
        self.__precio=precio

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio(self):
        return self.__precio

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo   

    @descripcion.setter
    def descripcion(self,descripcion):
        self.__descripcion=descripcion 

    @precio.setter
    def precio(self,precio):
        self.__precio=precio 

    def __str__(self):
        return 'Codigo: ' + str(self.codigo) + '\nPrecio: ' + str(self.precio) + '\nDescripcion: ' +self.descripcion

    def totalalimento(self):
        total=self.precio
class BoletoAvion:
    def __init__(self,nombrecliente,direcioncliente,telefonocliente,salida,destino,valorBoleto,impuestoSalida,horaSalida,horaLlegada):
        self.__valorBoleto=valorBoleto
        self.__impuestoSalida=impuestoSalida
        self.__horaLlegada=horaLlegada
        self.__horaSalida=horaSalida
        self.__cliente=Cliente(nombrecliente,direcioncliente,telefonocliente)
        self.__ciudad=Ciudad(salida,destino)

    @property
    def valorBoleto(self):
        return self.__valorBoleto
    
    @property
    def impuestoSalida(self):
        return self.__impuestoSalida

    @property
    def horaLlegada(self):
        return self.__horaLlegada

    @property
    def horaSalida(self):
        return self.__horaSalida

    @property
    def cliente(self):
        return self.__cliente

    @property
    def ciudad(self):
        return self.__ciudad


    @valorBoleto.setter
    def valorBoleto(self,valor):
        self.__valorBoleto=valor

    @impuestoSalida.setter
    def impuestoSalida(self,valor):
        self.__impuestoSalida=valor

    @horaLlegada.setter
    def horaLlegada(self,valor):
        self.__horaLlegada=valor

    @horaSalida.setter
    def horaSalida(self,valor):
        self.__horaSalida=valor 

    @cliente.setter
    def cliente(self,cliente):
        self.__valorBoleto=cliente 

    @ciudad.setter
    def ciudad(self,ciudad):
        self.__ciudad=ciudad

    def __str__(self):
        return 'Valor Boleto: ' + str(self.valorBoleto) + '\nImpuesto Salida: ' + str(self.impuestoSalida) + '\nHora Salida: ' +str(self.horaSalida) + '\nHora llegada: ' + str(self.horaLlegada) + '\n' + str(self.cliente) +'\n' + str(self.ciudad)

    def precioPagar(self):
        precio=(self.valorBoleto*self.impuestoSalida)+self.valorBoleto
        return precio

class BoletoEjecutivo(BoletoAvion):
    def __init__(self,nombrecliente,direcioncliente,telefonocliente,salida,destino,valorBoleto,impuestoSalida,horaSalida,horaLlegada):
        super().__init__(nombrecliente,direcioncliente,telefonocliente,salida,destino,valorBoleto,impuestoSalida,horaSalida,horaLlegada)
        self.__Alimentoextra=[]

    @property

    def Alimentoextra(self):
        return self.__Alimentoextra
    
    @Alimentoextra.setter

    def Alimentoextra(self,alimento):
        self.__Alimentoextra.append(alimento)

    def __str__(self):
        return (super().__str__()) 
    
    def precioPagar(self):
        precio=0
        for e in range(len(self.Alimentoextra)):
            precio=precio+self.Alimentoextra[e].precio
       
        precio=precio+super().precioPagar()
        return precio 
    
class Boletoclientefrecuente(BoletoAvion):
    def __init__(self,nombrecliente,direcioncliente,telefonocliente,salida,destino,valorBoleto,impuestoSalida,horaSalida,horaLlegada,descuento):
        super().__init__(nombrecliente,direcioncliente,telefonocliente,salida,destino,valorBoleto,impuestoSalida,horaSalida,horaLlegada)
        self.__descuento=descuento

    @property

    def descuento(self):
        return self.__descuento
    
    @descuento.setter

    def descuento(self,descuento):
        self.__descuento=descuento

    def __str__(self):
        return (super().__str__()) +str(self.descuento)
    
    def precioPagar(self):
        precio= (1-self.descuento)*super().precioPagar()
        return precio






