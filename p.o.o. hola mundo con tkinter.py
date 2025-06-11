import tkinter as tk
from tkinter import messagebox

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Hola Mundo con POO")

        self.boton_saludo = tk.Button(self.root, text="Saludar", command=self.mostrar_mensaje)
        self.boton_saludo.pack(pady=50)

    def mostrar_mensaje(self):
        messagebox.showinfo("Saludo", "Hola Mundo")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
    
