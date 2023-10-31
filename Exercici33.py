import tkinter as tk
import sqlite3

# Función para guardar los datos en la base de datos
def guardar_datos():
    # Conectar a la base de datos y crear un cursor
    conexion = sqlite3.connect("mi_base_de_datos.db")
    cursor = conexion.cursor()

    # Obtener los valores de las entradas
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()

    # Insertar los datos en la base de datos
    cursor.execute("INSERT INTO personas (nombre, apellido, edad) VALUES (?, ?, ?)", (nombre, apellido, edad))

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

    # Limpiar las entradas después de guardar los datos
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Introducir Datos en la Base de Datos")

# Etiquetas y entradas para nombre, apellido y edad
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_apellido = tk.Label(ventana, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

# Botón para guardar datos en la base de datos
boton_guardar = tk.Button(ventana, text="Guardar Datos", command=guardar_datos)
boton_guardar.pack()

# Función para imprimir los datos de la base de datos
def imprimir_datos():
    conexion = sqlite3.connect("mi_base_de_datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM personas")
    datos = cursor.fetchall()
    for fila in datos:
        print(f"Nombre: {fila[0]}, Apellido: {fila[1]}, Edad: {fila[2]}")
    conexion.close()

# Botón para imprimir los datos de la base de datos
boton_imprimir = tk.Button(ventana, text="Imprimir Datos", command=imprimir_datos)
boton_imprimir.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
