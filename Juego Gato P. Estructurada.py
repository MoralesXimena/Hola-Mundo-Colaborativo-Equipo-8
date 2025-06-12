import tkinter as tk
from tkinter import messagebox

turno = "X"
tablero = [""] * 9
botones = []

def clic_boton(indice):
    global turno
    if tablero[indice] == "":
        tablero[indice] = turno
        botones[indice].config(text=turno, state="disabled")
        if verificar_ganador(turno):
            messagebox.showinfo("Fin del juego", f"¡Ganó el jugador {turno}!")
            guardar_historial(turno)
            desactivar_tablero()
        elif "" not in tablero:
            messagebox.showinfo("Fin del juego", "¡Empate!")
            guardar_historial("Empate")
        else:
            turno = "O" if turno == "X" else "X"

def verificar_ganador(jugador):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6] 
    ]
    for combo in combinaciones:
        if all(tablero[i] == jugador for i in combo):
            return True
    return False

def guardar_historial(ganador):
    with open("historial.txt", "a") as f:
        f.write(f"Ganador: {ganador}\n")

def mostrar_historial():
    try:
        with open("historial.txt", "r") as f:
            historial = f.read()
        messagebox.showinfo("Historial de Partidas", historial)
    except FileNotFoundError:
        messagebox.showinfo("Historial de Partidas", "No hay partidas registradas.")

def reiniciar_juego():
    global turno, tablero
    turno = "X"
    tablero = [""] * 9
    for boton in botones:
        boton.config(text="", state="normal")

def desactivar_tablero():
    for boton in botones:
        boton.config(state="disabled")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Juego del Gato (Tic-Tac-Toe)")
    ventana.geometry("300x360")
    ventana.config(bg="lightpink")

    for i in range(9):
        boton = tk.Button(ventana, text="", font=("Arial", 20), width=5, height=2,
                          command=lambda i=i: clic_boton(i))
        boton.grid(row=i//3, column=i%3)
        botones.append(boton)

    btn_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar_juego)
    btn_reiniciar.grid(row=3, column=0, columnspan=3, sticky="we")

    btn_historial = tk.Button(ventana, text="Ver Historial", command=mostrar_historial)
    btn_historial.grid(row=4, column=0, columnspan=3, sticky="we")

    ventana.mainloop()

crear_ventana()