import tkinter as tk
from PIL import ImageTk, Image
import os
import re


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
            self.frame, text="Solucionador de Ecuaciones Diferenciales", font=("Arial Black", 22))
        self.etiqueta2 = tk.Label(
            self.frame, text="Created by:", font=("Arial Black", 10))
        self.etiqueta3 = tk.Label(
            self.frame, text="Daniel David Arias Monroy \n Rubert Albany Gonzalez Perez  \n Andres \n Leider", font=("Arial Black", 10))
        # self.etiqueta4 = tk.Label(self.frame,image=self.image)

        # --------Iniciar botones---------------
        self.boton1 = tk.Button(self.frame, width=3,
                                text="^", command=self.calular_ecuacion)
        self.boton2 = tk.Button(self.frame, width=3,
                                text="*", command=self.calular_ecuacion)
        self.boton3 = tk.Button(self.frame, width=3,
                                text="/", command=self.calular_ecuacion)
        self.boton4 = tk.Button(self.frame, width=3,
                                text="x", command=self.calular_ecuacion)
        self.boton5 = tk.Button(self.frame, width=3,
                                text="y", command=self.calular_ecuacion)
        self.boton6 = tk.Button(self.frame, width=3,
                                text="(", command=self.calular_ecuacion)
        self.boton7 = tk.Button(self.frame, width=3,
                                text=")", command=self.calular_ecuacion)
        self.boton8 = tk.Button(self.frame, width=3,
                                text="DEL", command=self.calular_ecuacion,background='red',fg='white')
        self.btnCalcular = tk.Button(self.frame, width=6,
                                text="Calcular", command=self.calular_ecuacion)
        
        # --------Iniciar input---------------
        self.entrada1 = tk.Entry(self.frame, width=40, validate="key", validatecommand=(
            self.frame.register(self.validar_entry), "%P"))

    def calular_ecuacion(self):
        pass

    def validar_entry(self, P):
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
        self.salto.grid(row=2, column=4, pady=50)
        self.etiqueta2.grid(row=3, column=4, pady=20, columnspan=2)
        self.etiqueta3.grid(row=4, column=4, columnspan=2)

        # ------Ubicacion de botones--------------
        self.boton1.place(x=260, y=200)
        self.boton2.place(x=300, y=200)
        self.boton3.place(x=340, y=160)
        self.boton4.place(x=260, y=160)
        self.boton5.place(x=300, y=160)
        self.boton6.place(x=340, y=200)
        self.boton7.place(x=380, y=200)
        self.boton8.place(x=380, y=160)
        self.btnCalcular.place(x=310,y=240)
        
        # ------Ubicacion de inputs--------------
        self.entrada1.grid(row=1, column=4, padx=210)
