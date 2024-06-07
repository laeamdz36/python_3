"""Practicas de modulo tkinter"""
import tkinter as tk
import tkinter.messagebox as tkm


def messageShow():
    tkm.showinfo("hola mundo", "python")
    return


def msgWarning():
    tkm.showwarning("Mensaje de warning", "Esto es un warning")
    return


window = tk.Tk()
window.title("Testing tkinter module")
window.geometry("640x480")
# window.resizable(width=False, height=False)

btn_1 = tk.Button(window, text="Boton 1",
                  activebackground="#00ff00", bg="#ff0000", fg="#0000ff", font="Arial 12", command=messageShow)
# btn_1.grid(column=0, row=4, sticky="E", padx=10, pady=5, columnspan=3)
# btn_1.place(relx=0.5, rely=0.7)
btn_1.pack(side=tk.BOTTOM, fill="x")

btn_2 = tk.Button(window, text="Show Warning", command=msgWarning)
# btn_2.grid(column=0, row=5, sticky="E", padx=10, pady=5, columnspan=3)
# btn_2.place(relx=0.5, rely=0.6)
btn_2.pack(side=tk.BOTTOM, fill="x")

label_1 = tk.Label(window, text="Label 1", bg="yellow",
                   font=("Arial", 12))
# label_1.grid(column=0, row=1, sticky="W")
label_1.pack(side="left", expand=True, fill="x")

label_2 = tk.Label(window, text="Label 2", bg="blue", font=("Arial", 12))
# entry_2.grid(column=1, row=0, sticky="E", columnspan=2)
label_2.pack(side="top", fill="x", expand=True)

label_3 = tk.Label(window, text="Label 3", bg="red")
# entry_1.grid(column=1, row=1, sticky="E", columnspan=2)
label_3.pack(fill="x", expand=True)

# """

# """

window.mainloop()
