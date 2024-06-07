import tkinter as tk


def mensaje():
    print("Hola denuevo")


window = tk.Tk()
window.geometry("400x200")
window.title("Window - Hola Mundo!")

lbl = tk.Label(window, text="Esto es una label tkinter", bg="blue")
lbl.place(x=10, y=10, width=140, height=30)

btn = tk.Button(
    window, text="presiona este boton para mensaje", command=mensaje)
btn.place(x=160, y=10, width=200, height=30)

window.mainloop()
