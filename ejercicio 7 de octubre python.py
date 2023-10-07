import tkinter as tk

def convertir():
    try:
        # Obtiene el valor ingresado en el campo de entrada
        kilometros = float(entrada_kilometros.get())

        # Realiza la conversión a millas (1 kilómetro = 0.621371 millas)
        millas = kilometros * 0.621371

        etiqueta_resultado.config(text=f"{kilometros} kilómetros son {millas} millas")

    except ValueError:
        # Manejo de errores para entradas no válidas
        etiqueta_resultado.config(text="Ingrese un valor numérico válido.")

# Crea la ventana Principal
ventana = tk.Tk()
ventana.title("Conversor de kilómetros a Millas")
ventana.geometry("300x150")

# Crea etiquetas de introducción y colócala en la cuadrícula
etiqueta_instruccion = tk.Label(ventana, text="Ingrese la Distancia en Kilómetros:")
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entrada de Datos y colócala en la Cuadrícula
entrada_kilometros = tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10)

# Botón de Conversión
boton_convertidor = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertidor.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Crear etiqueta de resultados y colócala en la cuadrícula
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()

        
