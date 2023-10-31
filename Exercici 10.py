import tkinter as tk

# Función para manejar los números y operaciones
def agregar_caracter(caracter):
    entrada_texto.insert(tk.END, caracter)

def borrar():
    entrada_texto.delete(0, tk.END)

def igual():
    global operacion
    entrada = entrada_texto.get()
    try:
        resultado = eval(entrada)
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, str(resultado))
    except:
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, "Error")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Entrada de texto
entrada_texto = tk.Entry(ventana, font=("Arial", 18), width=14, borderwidth=2, relief="solid", justify="right")
entrada_texto.grid(row=0, column=0, columnspan=4)

# Definición de los botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Funciones para los botones
fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 18), command=igual).grid(row=fila, column=columna)
    elif boton == 'C':
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 18), command=borrar).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, padx=20, pady=20, font=("Arial", 18), command=lambda x=boton: agregar_caracter(x)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Variable global para almacenar el tipo de operación
operacion = None

# Función principal para ejecutar la aplicación
ventana.mainloop()
