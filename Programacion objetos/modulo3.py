class repuesto:
    def __init__(self,codigo,nombre,precio):
        self.__codigo=codigo
        self.__precio=precio
        self.__nombre=nombre
    
    @property
    def codigo(self):
        return self.__codigo
    @property
    def precio(self):
        return self.__precio
    @property
    def nombre(self):
        return self.__nombre

    @codigo.setter
    def codigo(self,valor):
        self.__codigo=valor

    @precio.setter
    def precio(self,valor):
        self.__precio=valor

    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + '\nPrecio: ' + str(self.__precio) + '\nNombre: ' + str(self.__nombre)

class fecha:
    def __init__(self,dia,mes,anno):
        self.__dia=dia
        self.__mes=mes
        self.__anno=anno

    @property

    def dia(self):
        return self.__dia
    @property

    def mes(self):
        return self.__mes

    @property

    def anno(self):
        return self.__anno

    @dia.setter

    def dia(self,dia):
        self.__dia=dia

    @mes.setter

    def mes(self,mes):
        self.__mes=mes

    @anno.setter

    def anno(self,anno):
        self.__anno=anno

    def __str__(self):
        return 'Dia: '+str(self.dia) + '\nMes: ' + str(self.mes) + '\nAnno: ' + str(self.anno)

class fechatest:
    def __init__(self,dias):
        self.__numerodias=dias
       

    @property

    def numerodias(self):
        return self.__numerodias
   

    @numerodias.setter

    def numerodias(self,dias):
        self.__numerodias=dias


    def __str__(self):
        return 'Numero de Dia: '+str(self.numerodias) 

class fabricante:
    def __init__(self,nombre,pais):
        self.__pais=pais
        self.__nombre=nombre
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def pais(self):
        return self.__pais


    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @pais.setter
    def pais(self,pais):
        self.__pais=pais

    def __str__(self):
        return 'Nombre: ' + str(self.__nombre) + '\nPais ' + str(self.__pais)

class proveedor(fabricante):
    def __init__(self,codigo, indice,nombre,pais):
        super().__init__(nombre,pais)
        self.__codigo=codigo
        self.__indice=indice

    @property

    def codigo(self):
        return self.__codigo

    @property

    def indice(self):
        return self.__indice
    
    @codigo.setter

    def codigo(self,codigo):
        self.__codigo=codigo
        
    @indice.setter

    def indice(self,indice):
        self.__indice=indice

    def __str__(self):
        return (super().__str__()) + '\nCodigo: ' + str(self.codigo)+ '\nIndice: ' + str(self.indice)

class fabricanteoriginal(fabricante):
    def __init__(self,direccion,telefono,email,nombre,pais):
        super().__init__(nombre,pais)
        self.__direccion=direccion
        self.__telefono=telefono
        self.__email=email

    @property

    def direccion(self):
        return self.__direccion

    @property

    def telefono(self):
        return self.__telefono
    
    @property

    def email(self):
        return self.__email

    @direccion.setter

    def codigo(self,direccion):
        self.__direccion=direccion
        
    @telefono.setter

    def telefono(self,telefono):
        self.__telefono=telefono

    def __str__(self):
        return (super().__str__()) + '\nDireccion: ' + str(self.direccion)+ '\nTelefono: ' + str(self.telefono) + '\nEmail: ' + str(self.email)       

class nuevo(repuesto):
    def __init__(self,codigo, nombre,precio,annogarantia):
        super().__init__(codigo,nombre,precio)
        self.__annogarantia=annogarantia

    @property

    def annogarantia(self):
        return self.__annogarantia
    
    @annogarantia.setter

    def annogarantia(self,annogarantia):
        self.__annogarantia=annogarantia
    
    def calculaprecio(self):
        return self.precio*self.annogarantia

    def __str__(self):
        return (super().__str__()) + '\nAño Garantia: ' + str(self.annogarantia)

class nooriginal(repuesto):

    def __init__(self,codigo, nombre,precio,paisfabricacion):
        super().__init__(codigo,nombre,precio)
        self.__paisfabricacion=paisfabricacion
    

    @property

    def paisfabricacion(self):
        return self.__paisfabricacion
    
    @paisfabricacion.setter

    def paisfabricacion(self,paisfabricacion):
        self.__paisfabricacion=paisfabricacion

    def __str__(self):
        return (super().__str__()) + '\nPais Fabricacion: ' + str(self.paisfabricacion)

    def calculaprecio(self):
        
       #total=super().precio*0.10+super().precio
        return 0#total

class usados(nooriginal):
    def __init__(self,codigo, nombre,precio,pais,fecha,fechatest):
        super().__init__(codigo,nombre,precio,pais)
        self.__provedor=[]
        self.__fecha=fecha
        self.__fechatest=fechatest
    
    @property

    def provedor(self):
        return self.__provedor

    @property

    def fecha(self):
        return self.__fecha

    @property

    def fechatest(self):
        return self.__fechatest

    @provedor.setter

    def provedor(self,prov):
        self.__provedor.append(prov)

    @fecha.setter

    def fecha(self,fecha):
        self.__fecha=fecha

    @fechatest.setter

    def fechatest(self,fechas):
        self.__fechatest=fechas

    def __str__(self):
        return (super().__str__()) + '\nProvedor: ' + str(self.provedor[0]) + '\nFecha: ' + str(self.fecha) + '\nFecha Test: ' + str(self.fechatest) 

    def calculaprecio(self):
        total=super().calculaprecio()
        return total
    
class nonuevos(nooriginal):

    def __init__(self,codigo, nombre,precio,pais,fabri):
        super().__init__(codigo,nombre,precio,pais)
        self.__fabricante=fabri
    
    @property

    def fabricante(self):
        return self.__fabricante

    @fabricante.setter

    def fabricante(self,fabri):
        self.__fabricante=fabri

    def __str__(self):
        return (super().__str__()) + '\nFabricante: ' + str(self.fabricante) 

    def calculaprecio(self):
        total=super().calculaprecio()
        return total

class original(nuevo):
    def __init__(self,codigo, nombre,precio,anno,fecha,fabricante):
        super().__init__(codigo,nombre,precio,anno)
        self.__fecha=fecha
        self.__fabricanteoriginal=fabricante
    
    @property

    def fecha(self):
        return self.__fecha
    @property

    def fabricanteoriginal(self):
        return self.__fabricanteoriginal

    @fecha.setter

    def fecha(self,fecha):
        self.__fecha=fecha

    @fabricanteoriginal.setter

    def fabricanteoriginal(self,fabri):
        self.__fabricanteoriginal=fabri

    def __str__(self):
        return (super().__str__()) + '\nFecha: ' + str(self.fecha) + '\nFabricante Orinigal ' + str(self.fabricanteoriginal) 

    def calculaprecio(self):
        total=(super().calculaprecio()*0.25)+super().calculaprecio()
        return total
