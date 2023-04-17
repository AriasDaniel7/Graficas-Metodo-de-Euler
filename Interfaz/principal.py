import tkinter as tk
# -----------Trabajar interfaz FALTA----------------
class principal:
    def __init__(self) -> None:
        #---------Iniciar ventana------------
        self.principal = tk.Tk()
        self.principal.title("Metodo de Euler")

        ancho_total = self.principal.winfo_screenwidth()
        altura_total = self.principal.winfo_screenheight()
        ancho_ventana = 700
        altura_ventana = 500
        ancho = round(ancho_total/2-ancho_ventana/2)
        altura = round(altura_total/2-altura_ventana/2)

        self.principal.geometry(str(ancho_ventana)+"x"+str(altura_ventana)+"+"+str(ancho)+"+"+str(altura))
        self.frame = tk.Frame(self.principal)

        self.frame.pack()
        
    def componentes(self):
        from inicio import inicio
        inicio(self.frame).principal()
    
    def ver_ventana(self):
        self.componentes()
        self.principal.mainloop()
        

principal().ver_ventana()