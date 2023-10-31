import tkinter as tk
from PIL import Image, ImageTk
import os

# Lista para almacenar las rutas de las imágenes
lista_imagenes = []
indice_actual = 0


# Función para cargar imágenes del directorio
def cargar_imagenes():
    directorio = "/imagenes"  # Ruta del directorio que contiene las imágenes
    for archivo in os.listdir(directorio):
        if archivo.endswith(".png") or archivo.endswith(".jpg"):
            ruta_imagen = os.path.join(directorio, archivo)
            lista_imagenes.append(ruta_imagen)


# Función para mostrar la imagen actual en la interfaz
def mostrar_imagen():
    global indice_actual
    imagen = Image.open(lista_imagenes[indice_actual])
    imagen = imagen.resize((300, 200), Image.ANTIALIAS)
    foto = ImageTk.PhotoImage(imagen)
    etiqueta.config(image=foto)
    etiqueta.image = foto
    etiqueta_info.config(text=f"Imatge {indice_actual + 1} de {len(lista_imagenes)}")


# Función para el botón "Siguiente"
def siguiente_imagen():
    global indice_actual
    if indice_actual < len(lista_imagenes) - 1:
        indice_actual += 1
        mostrar_imagen()
    actualizar_botones()


# Función para el botón "Anterior"
def anterior_imagen():
    global indice_actual
    if indice_actual > 0:
        indice_actual -= 1
        mostrar_imagen()
    actualizar_botones()


# Función para actualizar el estado de los botones
def actualizar_botones():
    if indice_actual == 0:
        boton_previo.config(state=tk.DISABLED)
    else:
        boton_previo.config(state=tk.NORMAL)

    if indice_actual == len(lista_imagenes) - 1:
        boton_siguiente.config(state=tk.DISABLED)
    else:
        boton_siguiente.config(state=tk.NORMAL)


# Función principal para ejecutar el programa
def main():
    cargar_imagenes()
    mostrar_imagen()

    ventana = tk.Tk()
    ventana.title("Visor de Imágenes")

    global etiqueta, boton_previo, boton_siguiente, etiqueta_info

    etiqueta = tk.Label(ventana, bd=2, relief=tk.SUNKEN)
    etiqueta.grid(row=0, column=0, columnspan=2, sticky=tk.W + tk.E)

    etiqueta_info = tk.Label(ventana, text="", anchor=tk.E)
    etiqueta_info.grid(row=1, column=1, sticky=tk.E)

    boton_previo = tk.Button(ventana, text="Anterior", command=anterior_imagen)
    boton_previo.grid(row=1, column=0, padx=10, pady=10)

    boton_siguiente = tk.Button(ventana, text="Siguiente", command=siguiente_imagen)
    boton_siguiente.grid(row=1, column=1, padx=10, pady=10)

    actualizar_botones()

    ventana.mainloop
