import tkinter as tk

def segunda_ventana():
    ventana.destroy()
    ventana2= tk.Tk()
    titulo_principal= ventana2.title("pagina principal")
    ventana2.geometry("400x400")
    ventana2.config(background="black")
    titulo2= tk.Label(ventana2, text="Proyecto", bg="turquoise2", fg="white", font=("times new roman", 20))
    titulo2.pack(pady=20)
    ventana2.mainloop()
    
    
    
ventana= tk.Tk()
tittle= ventana.title("Proyecto")
ventana.geometry("400x400")
ventana.config(background="black")
titulo= tk.Label(ventana, text="Proyecto", bg="turquoise2", fg="white", font=("times new roman", 20))
run= tk.Button(ventana, text="iniciar", bg="turquoise2", fg="white", font=("times new roman", 20), command=segunda_ventana)

titulo.pack(pady=20)
run.pack(pady=50)

ventana.mainloop()