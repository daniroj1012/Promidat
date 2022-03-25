import ACP_PRINCE
from ACP_PRINCE import ACP

class my_acp(ACP):
    def __init__(self,datos, n_componentes = 5, columna =[]):
        super().__init__(datos=datos.drop(columna, axis=1),n_componentes=5)
        
    def __str__(self):
        return (super().__str__()) + '\nCodigo: ' + str(self.codigo)+ '\nIndice: ' + str(self.indice)


