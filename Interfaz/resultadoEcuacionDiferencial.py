import sympy as sp
import numpy as np

class Ecuacion:
    def __init__(self,ecuacion,xi,xf,n) -> None:
        self.ecuacion = ecuacion
        # ----- Leer valores -------
        self.entrada = ecuacion
        self.entrada = self.entrada.replace("y", "y(x)")

        # Definir la variable independiente y la función desconocida
        self.x = sp.symbols('x')
        self.y = sp.Function('y')(self.x)
        self.conver = sp.simplify(self.entrada)
        # Definir la EDO
        self.f = sp.Eq(self.y.diff(self.x), self.conver)
        # Resolver la EDO
        self.ics = {self.y.subs(self.x, 0): 1}
        self.sol = sp.dsolve(self.f, self.y,ics=self.ics)
        
        self.expresion_num = sp.lambdify(self.x,self.sol.rhs)

        self.x_valores = np.linspace(xi,xf,num=n)
        self.y_valores = self.expresion_num(self.x_valores)
        
        
    def imprimirECG(self):
        sp.pprint(self.sol)
    
    def getValoresX(self):
        return self.x_valores
    
    def getValoresY(self):
        return self.y_valores
    
    def trabajarFuncion(self,valorX):
        res = self.expresion_num(valorX)
        return res
    
    def latex(self):
        return sp.latex(self.sol)