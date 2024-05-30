import tkinter as tk

ventana= tk.Tk()
tittle= ventana.title("Proyecto")
ventana.geometry("400x400")
ventana.config(background="black")
titulo= tk.Label(ventana, text="Proyecto", bg="black", fg="white")
titulo.pack(pady=60)

ventana.mainloop()