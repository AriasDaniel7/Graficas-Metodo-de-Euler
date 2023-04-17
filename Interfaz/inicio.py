import tkinter as tk
from tkinter import messagebox
import re
from grafica import grafica


class inicio():
    def __init__(self, frame):
        self.frame = frame
        # --------Cargar imagenes--------------
        # absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        # img = Image.open(os.path.join(absolute_folder_path, 'escudo_62_anios.png')).resize((150,200))
        # self.image = ImageTk.PhotoImage(img)

        # --------Iniciar Etiquetas de salto de linea---------------
        self.salto = tk.Label(
            self.frame, text="")

        # -----------Iniciar etiquetas-----------------
        self.etiqueta1 = tk.Label(
            self.frame, text="Graficadora de Ecuaciones Diferenciales", font=("Arial Black", 22))
        self.etiqueta2 = tk.Label(
            self.frame, text="Created by:", font=("Arial Black", 10))
        self.etiqueta3 = tk.Label(
            self.frame, text="Daniel David Arias Monroy \n Rubert Albany Gonzalez Perez  \n Andres \n Leider", font=("Arial Black", 10))
        self.h = tk.Label(
            self.frame, text="h =")
        self.x0 = tk.Label(
            self.frame, text="x0 =")
        self.y0 = tk.Label(
            self.frame, text="y0 =")
        self.n = tk.Label(
            self.frame, text="n =")
        self.xi = tk.Label(
            self.frame, text="xi =")
        self.xf = tk.Label(
            self.frame, text="xf =")
        # self.etiqueta4 = tk.Label(self.frame,image=self.image)

        # --------Iniciar botones---------------
        self.boton1 = tk.Button(self.frame, width=3,
                                text="^", command=self.escribir_s1)
        self.boton2 = tk.Button(self.frame, width=3,
                                text="*", command=self.escribir_s2)
        self.boton3 = tk.Button(self.frame, width=3,
                                text="/", command=self.escribir_s3)
        self.boton4 = tk.Button(self.frame, width=3,
                                text="x", command=self.escribir_X)
        self.boton5 = tk.Button(self.frame, width=3,
                                text="y", command=self.escribir_s4)
        self.boton6 = tk.Button(self.frame, width=3,
                                text="(", command=self.escribir_s5)
        self.boton7 = tk.Button(self.frame, width=3,
                                text=")", command=self.escribir_s6)
        self.boton9 = tk.Button(self.frame, width=3,
                                text="+", command=self.escribir_s7)
        self.boton10 = tk.Button(self.frame, width=3,
                                 text="-", command=self.escribir_s8)
        self.boton8 = tk.Button(self.frame, width=3,
                                text="DEL", command=lambda: self.entrada1.delete(0, tk.END), background='red', fg='white')
        self.btnCalcular = tk.Button(self.frame, width=9,
                                     text="Grafica", command=self.calular_ecuacion)
        self.btnTabla = tk.Button(self.frame, width=12,
                                  text="Tabla de Error", command=self.calcularTabla)

        # --------Iniciar input---------------
        self.entrada1 = tk.Entry(self.frame, width=40, validate="key", validatecommand=(
            self.frame.register(self.validar_entry), "%S"))

        self.entrada2 = tk.Entry(self.frame, width=5, validate="key", validatecommand=(
            self.frame.register(self.validar_entry2), "%P"))

        self.entrada3 = tk.Entry(self.frame, width=5, validate="key", validatecommand=(
            self.frame.register(self.validar_entry2), "%P"))

        self.entrada4 = tk.Entry(self.frame, width=5, validate="key", validatecommand=(
            self.frame.register(self.validar_entry2), "%P"))

        self.entrada5 = tk.Entry(self.frame, width=5, validate="key", validatecommand=(
            self.frame.register(self.validar_entry2), "%P"))

        self.entrada6 = tk.Entry(self.frame, width=5, validate="key", validatecommand=(
            self.frame.register(self.validar_entry2), "%P"))

        self.entrada7 = tk.Entry(self.frame, width=5, validate="key", validatecommand=(
            self.frame.register(self.validar_entry2), "%P"))

        self.boton8 = tk.Button(self.frame, width=3,
                                text="DEL", command=self.eliminar, background='red', fg='white')

    def eliminar(self):
        cadena = self.entrada1.get()
        for c in cadena:
            self.entrada1.delete(0)

    def escribir_s1(self):
        self.entrada1.insert(tk.END, "^")

    def escribir_s2(self):
        self.entrada1.insert(tk.END, "*")

    def escribir_s3(self):
        self.entrada1.insert(tk.END, "/")

    def escribir_X(self):
        self.entrada1.insert(tk.END, "x")

    def escribir_s4(self):
        self.entrada1.insert(tk.END, "y")

    def escribir_s5(self):
        self.entrada1.insert(tk.END, "(")

    def escribir_s6(self):
        self.entrada1.insert(tk.END, ")")

    def escribir_s7(self):
        self.entrada1.insert(tk.END, "+")

    def escribir_s8(self):
        self.entrada1.insert(tk.END, "-")

    def calcularTabla(self):
        funsion = self.entrada1.get()
        h = self.entrada2.get()
        n = self.entrada3.get()
        x0 = self.entrada4.get()
        y0 = self.entrada5.get()
        xi = self.entrada6.get()
        xf = self.entrada7.get()

        vacio = False
        validate = [funsion, h, n, x0, y0, xi, xf]
        for val in validate:
            if (len(val) == 0):
                vacio = True

        if (vacio != True):
            funsion = self.entrada1.get()
            h = float(self.entrada2.get())
            n = int(self.entrada3.get())
            x0 = float(self.entrada4.get())
            y0 = float(self.entrada5.get())
            xi = int(self.entrada6.get())
            xf = int(self.entrada7.get())

            gf = grafica(funsion, xi, xf, x0, y0, n, h)
            gf.imprimirError()
        else:
            messagebox.showinfo(
                message="Complete todos los datos", title="Alerta")

    def calular_ecuacion(self):
        funsion = self.entrada1.get()
        h = self.entrada2.get()
        n = self.entrada3.get()
        x0 = self.entrada4.get()
        y0 = self.entrada5.get()
        xi = self.entrada6.get()
        xf = self.entrada7.get()

        vacio = False
        validate = [funsion, h, n, x0, y0, xi, xf]
        for val in validate:
            if (len(val) == 0):
                vacio = True

        if (vacio != True):
            funsion = self.entrada1.get()
            h = float(self.entrada2.get())
            n = int(self.entrada3.get())
            x0 = float(self.entrada4.get())
            y0 = float(self.entrada5.get())
            xi = int(self.entrada6.get())
            xf = int(self.entrada7.get())

            gf = grafica(funsion, xi, xf, x0, y0, n, h)
            gf.verGrafica()
        else:
            messagebox.showinfo(
                message="Complete todos los datos", title="Alerta")

    def validar_entry(self, P):
        patron = '^[- x ^ * / y ( ) +]$'
        if not P:
            return True
        if (re.search(patron, P)):
            return True
        try:
            float(P)
        except ValueError:
            return False
        return True

    def validar_entry2(self, P):
        patron = '^[-]$'
        if not P:
            return True
        if (re.search(patron, P)):
            return True
        try:
            float(P)
        except ValueError:
            return False
        return True

    def principal(self):
        # ------Ubicacion de etiquetas------------
        self.etiqueta1.grid(row=0, column=4, pady=40, columnspan=2)
        self.salto.grid(row=2, column=4, pady=80)
        self.etiqueta2.grid(row=3, column=4, pady=20, columnspan=2)
        self.etiqueta3.grid(row=4, column=4, columnspan=2)
        self.h.place(x=450, y=160)
        self.n.place(x=520, y=160)
        self.x0.place(x=450, y=200)
        self.y0.place(x=520, y=200)
        self.xi.place(x=450, y=240)
        self.xf.place(x=520, y=240)

        # ------Ubicacion de botones--------------
        self.boton1.place(x=260, y=200)
        self.boton2.place(x=300, y=200)
        self.boton3.place(x=340, y=160)
        self.boton4.place(x=260, y=160)
        self.boton5.place(x=300, y=160)
        self.boton6.place(x=340, y=200)
        self.boton7.place(x=380, y=200)
        self.boton8.place(x=380, y=160)
        self.boton9.place(x=300, y=240)
        self.boton10.place(x=340, y=240)
        self.btnCalcular.place(x=350, y=280)
        self.btnTabla.place(x=250, y=280)

        # ------Ubicacion de inputs--------------
        self.entrada1.grid(row=1, column=4, padx=210)
        self.entrada2.place(x=480, y=160)
        self.entrada3.place(x=550, y=160)
        self.entrada4.place(x=480, y=200)
        self.entrada5.place(x=550, y=200)
        self.entrada6.place(x=480, y=240)
        self.entrada7.place(x=550, y=240)
