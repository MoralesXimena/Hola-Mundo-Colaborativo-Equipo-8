import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Hola Mundo!")

ventana = tk.Tk()
ventana.title("Hola Mundo")

etiqueta = tk.Label(ventana, text="Presiona el botón para ver el mensaje")
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()