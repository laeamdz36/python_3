"""ventana para sumaro dos numeros"""

import tkinter as tk

# modo de posicionamiento de controles
# place, pack, grid
# No mezclar distinos metodos de posicionamiento dentro de un mismo contenedor

# place, posicionamiento de control en ubicacion x y y


def sumar_v1():
    """Funcion sumar dos numeros"""
    number_1 = btxt_1.get()
    number_2 = btxt_2.get()
    result = int(number_1) + int(number_2)
    # Borrar contenido en caja de texto 3 desde posicion 0 hasta el final
    btxt_3.delete(0, "end")
    # INsertar resultado en caja de texto 3
    btxt_3.insert(0, result)


def result_box_clear():
    """Borrar contenido en caja de texto de resultado"""
    btxt_3.delete(0, "end")
    btxt_1.delete(0, "end")
    btxt_2.delete(0, "end")


window = tk.Tk()
window.title("Sumar dos numeros")
window.geometry("400x280")

# etiquetas
label_1 = tk.Label(window, text="Primer numero", bg="green")
label_1.place(x=10, y=20, width=100, height=15)

label_1 = tk.Label(window, text="Segundo numero", bg="green")
label_1.place(x=10, y=60, width=100, height=15)

label_1 = tk.Label(window, text="Resultado", bg="yellow")
label_1.place(x=10, y=120, width=100, height=15)

# cajas de texto

btxt_1 = tk.Entry(window, bg="pink")
btxt_1.place(x=120, y=10, width=100, height=30)

btxt_2 = tk.Entry(window, bg="pink")
btxt_2.place(x=120, y=60, width=100, height=30)

btxt_3 = tk.Entry(window, bg="pink")
btxt_3.place(x=120, y=120, width=100, height=30)

# button

btn_1 = tk.Button(window, text="Sumar", command=sumar_v1)
btn_1.place(x=230, y=50, width=80, height=30)

btn_clear = tk.Button(window, text="Borrar", command=result_box_clear)
btn_clear.place(x=230, y=120, width=80, height=30)

window.mainloop()
