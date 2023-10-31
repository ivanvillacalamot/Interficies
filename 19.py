import tkinter as tk
from tkinter import messagebox

# Función para mostrar la ventana emergente y actualizar la etiqueta en la ventana principal
def mostrar_mensaje():
    var_fe = messagebox.askyesno("Titol finestra", "Vols continuar?")
    if var_fe:
        etiqueta.config(text="Has clicat si")
    else:
        etiqueta.config(text="Has clicat no")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Exemple de MessageBox")

# Etiqueta para mostrar el resultado
etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=20)

# Botón para mostrar la ventana emergente
boton_mostrar = tk.Button(ventana, text="Mostrar MessageBox", command=mostrar_mensaje)
boton_mostrar.pack()

# Función principal para ejecutar el programa
ventana.mainloop()

var_showinfo = messagebox.showinfo("Titol finestra", "Aquest es un misatge final.")
etiqueta.config(text="Has clicat showinfo: " + str(var_showinfo))

