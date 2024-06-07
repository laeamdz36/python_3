import tkinter as tk

# mensaje a mostrar


def mensaje():
    """funcion para immpresion de mensaje en ventana"""
    print("Hola denuevo")


window = tk.Tk()
window.geometry("400x800")
window.title("Window - Hola Mundo!")

lbl = tk.Label(window, text="Esto es una label tkinter")
lbl.pack()

btn = tk.Button(
    window, text="presiona este boton para mensaje", command=mensaje)
btn.pack()

window.mainloop()
