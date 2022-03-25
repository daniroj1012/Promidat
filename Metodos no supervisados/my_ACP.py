import ACP_PRINCE
from ACP_PRINCE import ACP

class my_acp(ACP):
    def __init__(self,datos, n_componentes = 5, columna):
        datos2=datos.drop(columna,axis=1)
        super().__init__(datos2,n_componentes)
        self.__columna=columna
    
    @property
    def columna(self):
        return self.__columna
    
    @columna.setter

    def columna(self,columna):
        self.__columna=columna
    
        
    def __str__(self):
        return (super().__str__()) 


