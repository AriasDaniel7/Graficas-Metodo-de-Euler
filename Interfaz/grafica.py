import matplotlib.pyplot as plt
from resultadoEcuacionDiferencial import Ecuacion
from CalcularDatos import CalcularDatos

class grafica:
    def __init__(self,funcion,xi,xf,x0,y0,n,h) -> None:
        self.fig, self.ax1 = plt.subplots()
        self.ec = Ecuacion(funcion,xi,xf,n)
        
        self.x = self.ec.getValoresX()
        self.y = self.ec.getValoresY()
        
        self.ax1.plot(self.x, self.y,'r',label='Solucion Real')
        self.ax1.legend()
        self.ax1.legend(loc='upper left')  
        plt.title((r'$' + self.ec.latex() + r'$'))
        
        
        self.datos = CalcularDatos(x0,y0,n,h,funcion)
        datos = self.datos.calcularY()
        self.x = datos[0]
        self.y = datos[1]
        
        self.ax2 = self.ax1.twinx()
        self.ax2.plot(self.x,self.y,'o-',label='Metodo De Euler')
        self.ax2.legend()
        self.ax2.set_yticks([])
        self.ax2.legend(loc='upper center')
        
    def imprimirError(self):
        resultado = []
        for dato in self.x:
            resultado.append(self.ec.trabajarFuncion(dato))
        self.datos.margenDeError(resultado)
        
    def verGrafica(self):
        plt.show()
    
# gf = grafica('-((x*y)/(1+x**2))',-5,5,0,1,100,0.1)
# gf = grafica('x+y',-5,5,0,1,50,0.1)
# gf.imprimirError()
# gf.verGrafica()