import matplotlib.pyplot as plt
from resultadoEcuacionDiferencial import Ecuacion
from CalcularDatos import CalcularDatos

class grafica:
    def __init__(self,funcion,xi,xf,x0,y0,n,h) -> None:
        self.fig, self.ax1 = plt.subplots()
        self.ec = Ecuacion(funcion,xi,xf,n)
        
        x = self.ec.getValoresX()
        y = self.ec.getValoresY()
        
        self.ax1.plot(x, y,'r',label='Solucion Real')
        self.ax1.legend()
        self.ax1.legend(loc='upper left')  
        plt.title((r'$' + self.ec.latex() + r'$'))
        
        
        self.datos = CalcularDatos(x0,y0,n-1,h,funcion)
        datos = self.datos.calcularY()
        x = datos[0]
        y = datos[1]
        
        self.ax2 = self.ax1.twinx()
        self.ax2.plot(x,y,label='Metodo De Euler')
        self.ax2.legend()
        self.ax2.set_yticks([])
        self.ax2.legend(loc='upper center')

        plt.show()
    
grafica('-((x*y)/(1+x**2))',-5,5,0,1,50,0.1)
# grafica('x+y',-5,5,0,1,50,0.1)