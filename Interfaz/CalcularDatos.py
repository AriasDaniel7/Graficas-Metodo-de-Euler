import sympy as sp
import tabulate as tb


class CalcularDatos:
    def __init__(self, x0, y0, n, h, funcion) -> None:
        self.x0 = x0
        self.y0 = y0
        self.n = n
        self.h = h
        self.funcion = funcion
        self.listaX = []
        self.listaY = []

    def calcularX(self):
        i = 0
        self.listaX.append(self.x0)
        while (i < self.n):
            self.x0 = self.listaX[0] + (i)*self.h
            self.listaX.append(self.x0)
            i += 1
        return self.listaX

    def calcularY(self):
        self.calcularX()
        listaX = self.listaX
        self.listaY = []
        self.simboloX, self.simboloY = sp.symbols('x y')
        i = 0
        self.listaY.append(self.y0)
        while (i < self.n):
            calcular = sp.simplify(self.funcion)
            calcular = calcular.subs(
                {self.simboloX: listaX[i], self.simboloY: self.listaY[i]})
            resultado = self.listaY[i] + self.h*calcular
            self.listaY.append(resultado)
            i += 1
        listaDatos = [self.listaX, self.listaY]
        return listaDatos

    def margenDeError(self, datos):
        cop = []
        i = 0

        for dato in datos:
            error = dato - self.listaY[i]
            cop.append([self.listaX[i], self.listaY[i], dato, error])
            i += 1

        headers = ["xi", "yi", "y(x)", "Error"]
        datos = cop

        tabla = tb.tabulate(datos, headers=headers,
                            tablefmt="grid", numalign="center")
        print(tabla)
