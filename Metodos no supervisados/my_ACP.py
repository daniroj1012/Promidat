import ACP_PRINCE
from ACP_PRINCE import PCA_Prince

class my_acp(PCA_Prince):
    def __init__(self,datos, n_componentes = 5, columna =[]):
        super().__init__(datos,n_componentes)
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
