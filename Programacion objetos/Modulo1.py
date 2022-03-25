from cmath import pi
import pandas as pd
import numpy as np


class circulo:
    def __init__(self,diametro=0):
        self.__diametro=diametro
    @property
    def diametro(self):
        print("Pasó por obtener")
        return self.__diametro
    @diametro.setter
    def diametro(self, nuevo_diametro):
        print("Pasó por modificar")
        if nuevo_diametro< 0:
            raise ValueError("El diametro debe ser mayor a 0")
        print('Escribiendo Valor')
        self.__diametro = nuevo_diametro
        
    def __str__(self):
        return "Circulo de Diametro: %i" % (self.diametro)    
     
    def calcular_area(self):
        area=pi*((self.__diametro/2)**2)
        return area
    def calcular_perimetro(self):
        perimetro=2*pi*(self.__diametro/2)
        return perimetro

class cuadrado:
    def __init__(self,lado=0):
        self.__lado=lado
    @property
    def lado(self):
        print("Pasó por obtener")
        return self.__lado
    @lado.setter
    def lado(self, nuevo_lado):
        print("Pasó por modificar")
        if nuevo_lado< 0:
            raise ValueError("El lado debe ser mayor a 0")
        print('Escribiendo Valor')
        self.__lado = nuevo_lado
        
    def __str__(self):
        return "Cuadrado de Lado: %i" % (self.__lado)    
     
    def calcular_area(self):
        area=(self.__lado)**2
        return area
    def calcular_perimetro(self):
        perimetro=self.__lado*4
        return perimetro
    
    
class tarjeta:
    def __init__(self,nombre='',pin=0,saldo=0):
        self.__nombre=nombre
        self.__pin=pin
        self.__saldo=saldo
       
    @property
    def nombre(self):
        print("Pasó por obtener")
        return self.__nombre
    @property
    def pin(self):
        print("Pasó por obtener")
        return self.__pin
    @property
    def saldo(self):
        print("Pasó por obtener")
        return self.__saldo


    @nombre.setter
    def nombre(self,nomb):
        self.__nombre=nomb
    @pin.setter
    def pin(self,valor):
        self.__pin=valor
    @saldo.setter
    def saldo(self,valor):
        print('Escribiendo Saldo')
        self.__saldo=valor

    def __str__(self):
        return "Nombre: %s, Pin:%i , Saldo %f"% (self.__nombre,self.__pin,self.__saldo)  

    def depositar_dinero(self,deposito):
        if deposito< 0:
            raise ValueError("No existen depositos negativos")
        else:
            self.__saldo=self.__saldo+deposito

    def retirar_dinero(self,retiro):
        if retiro< 0:
            raise ValueError("No existen retiros negativos")
        else:
            if retiro>self.__saldo:
                raise ValueError("No puede retirar mas que lo que tiene")
            else:
                self.__saldo=self.__saldo-retiro    
       
    

class calificaciones():
  def _init_(self, DF = pd.DataFrame()):
    self.__DF = DF

  @property
  def DF(self):
    return self.__DF  
  @DF.setter
  def DF(self,nuevo_DF):
      self.__DF=nuevo_DF
     
        
  def __str__(self):
      return self.DF
  
  def actualizar_nota(self,nombre,materia,nota_nueva):
    self.DF.loc[(self.DF.iloc[:,0]==nombre),materia]=nota_nueva
   
        
  def promedio_estudiante(self,nombre):
    index=self.DF[self.DF.iloc[:,0]==nombre].index
    valores=self.DF.iloc[index,1:6]
    promedio=valores.mean(numeric_only=True).mean()
    return promedio

  def promedio_materia(self,materia):   
      promedio=self.DF.loc[:,materia].mean()
      return promedio
      
  def cantidad_reprobados(self,materia):  
      subdf=self.DF.loc[:,materia]
      i=0
      for e in subdf:
          
          if(e<6.75):
              i=i+1
      return 'La cantidad de estudiantes reprobados para la materia %s es de: %i' %(materia,i)

     
  def agregar_estudiante(self,df):
      self.DF.loc[len(self.DF.index)] = df
      return 'Estudiante agregado correctamente'
      
  def eliminar_estudiante(self,nombre):    
      index=self.DF[self.DF.iloc[:,0]==nombre].index
      self.DF=self.DF.drop(index[0])
      return 'Estudiante eliminado correctamente'

class mi_DF():
    def __init__(self, DF = pd.DataFrame()):
        self.__num_filas = DF.shape[0]
        self.__num_columnas = DF.shape[1]
        self.__DF = DF
    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    @property
    def DF(self):
        return self.__DF  
    def maximo(self):
        max = self.DF.iloc[0,0]
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] > max:
                    max = self.DF.iloc[i,j]
        return max
    def valores(self):
        min = self.DF.iloc[0,0]
        max = self.DF.iloc[0,0]
        total_ceros = 0
        total_pares = 0
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                if self.DF.iloc[i,j] > max:
                    max = self.DF.iloc[i,j]
                    if self.DF.iloc[i,j] < min:
                        min = self.DF.iloc[i,j]
                        if self.DF.iloc[i,j] == 0:
                            total_ceros = total_ceros+1
                            if self.DF.iloc[i,j] % 2 == 0:
                                total_pares = total_pares+1
        return {'Maximo' : max, 'Minimo' : min, 'Total_Ceros' : total_ceros, 'Pares' : total_pares}
    def estadisticas(self,nc):
        media = np.mean(self.DF.iloc[:,nc])
        mediana = np.median(self.DF.iloc[:,nc])
        deviacion = np.std(self.DF.iloc[:,nc])
        varianza = np.var(self.DF.iloc[:,nc])
        maximo = np.max(self.DF.iloc[:,nc])
        minimo = np.min(self.DF.iloc[:,nc])
        return {'Variable' : self.DF.columns.values[nc],
                'Media' : media,
                'Mediana' : mediana,
                'DesEst' : deviacion,
                'Varianza' : varianza,
                'Maximo' : maximo,
                'Minimo' : minimo}
    
    def divisibles_3(self):
        count=0
        dftemp=self.DF.iloc[:,1:self.num_columnas]
        
        for i in range(dftemp.shape[0]):
            for j in range(dftemp.shape[1]):
                if (dftemp.iloc[i,j]%3 == 0):
                    count=count+1
        return count
    
    def relacion_columnas(self,columna1,columna2):
        df1=self.DF.iloc[:,columna1]
        df2=self.DF.iloc[:,columna2]
        df3=pd.concat([df1, df2], axis=1)
        cor=df3.corr().to_dict()
        cov=df3.cov().to_dict()
       
        dictionary={'Correlacion':cor['Matematicas'],'Covarianza':cov['Matematicas']}
        print(dictionary)
        return dictionary
        
      
        

class analisis:
    def __init__(self,np=np.matrix([])):
        self.__np=np
    @property
    def np(self):
        #print("Pasó por obtener")
        return self.__np
    @np.setter
    def np(self, nuevo_np):
        #print("Pasó por modificar")
       
        self.__np = nuevo_np
        
    def __str__(self):
        return "Matriz: %object" % (self.np)  
    
    def as_data_frame(self):
        return pd.DataFrame(self.np)
        

    def desviacion_estandar(self,df):
        Std=df.std()
        return Std.to_dict()
    
    def media(self,df):
        Media=df.mean()
        return Media.to_dict()
    
    def mediana(self,df):
        Mediana=df.median()
        return Mediana.to_dict()
    
    def maximo(self):
        return np.amax(self.np)
    
    def buscar(self,numero):
        tamano=self.np.shape
        indices=[]
        try:
            for i in range(tamano[0]):
                for j in range(tamano[1]):
                    if(self.np[i,j]==numero):
                        indices.append([i,j])
            return indices[0]
        except:
            return'none'
    
    

#