import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Función para cargar y mostrar la imagen
def cargar_imagen():
    ruta_imagen = filedialog.askopenfilename()
    if ruta_imagen:
        imagen = Image.open("/imagenes")
        mostrar_imagen(imagen)

# Función para mostrar la imagen en el widget
def mostrar_imagen(imagen):
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta.config(image=imagen_tk)
    etiqueta.image = imagen_tk

# Función para guardar la imagen con otro nombre
def guardar_imagen():
    ruta_guardar = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG files", "*.png"),
                                                         ("JPEG files", "*.jpg"),
                                                         ("All files", "*.*")])
    if ruta_guardar:
        imagen_original.save(ruta_guardar)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Visor de Imágenes")

# Botón para cargar imagen
boton_cargar = tk.Button(ventana, text="Cargar Imagen", command=cargar_imagen)
boton_cargar.pack(pady=10)

# Etiqueta para mostrar la imagen
etiqueta = tk.Label(ventana)
etiqueta.pack(padx=10, pady=10)

# Botón para guardar imagen
boton_guardar = tk.Button(ventana, text="Guardar Imagen", command=guardar_imagen)
boton_guardar.pack(pady=10)

# Imagen original (para guardar)
imagen_original = None

# Ejecutar la ventana principal
ventana.mainloop()
