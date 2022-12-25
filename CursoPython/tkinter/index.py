import tkinter as tk


ventana = tk.Tk()
ventana.geometry("600x400")
cajaTexto = tk.Entry(ventana,font = "Lucida 20")
cajaTexto.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()
contador = 0
def imprimir():
    texto10 = cajaTexto.get()
    etiqueta["text"] = texto10
    
    print(texto10)



boton1 = tk.Button(ventana, text = "click", command = imprimir)
boton1.pack()
ventana.mainloop()