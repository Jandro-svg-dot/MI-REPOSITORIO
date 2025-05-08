# Programas con interfaz de usuario - tkinter
#
import tkinter as tk
from tkinter import messagebox
from smartdevice import SmartDevice

# Función que se ejecuta al hacer clic en el botón
def mostrar_contenido():
    contenido = f'{entrada1.get()} - {entrada2.get()} - {entrada3.get()}'
    messagebox.showinfo("Contenido ingresado", f"Has ingresado: {contenido}")
    
def mostrar_status():
    sd = SmartDevice({entrada1.get()}, {entrada2.get()}, {entrada3.get()})
    contenido = sd.status2()
    messagebox.showinfo("Resultado", f"SmartDevice: {contenido}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("SmartDevice")
ventana.geometry("300x300")

# Etiqueta
etiqueta1 = tk.Label(ventana, text="Marca:")
etiqueta1.pack(pady=5)

# Caja de texto
entrada1 = tk.Entry(ventana, width=30)
entrada1.pack(pady=5)

# Etiqueta
etiqueta2 = tk.Label(ventana, text="Modelo:")
etiqueta2.pack(pady=5)

# Caja de texto
entrada2 = tk.Entry(ventana, width=30)
entrada2.pack(pady=5)

# Etiqueta
etiqueta3 = tk.Label(ventana, text="Mensaje:")
etiqueta3.pack(pady=5)

# Caja de texto
entrada3 = tk.Entry(ventana, width=30)
entrada3.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Mostrar contenido", command=mostrar_contenido)
boton.pack(pady=10)

# Botón
boton2 = tk.Button(ventana, text="status()", command=mostrar_status)
boton2.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()