import random
import tkinter as tk
from tkinter import messagebox

def truncate(number, decimals):
    """
    Trunca un número a un número específico de decimales.
    
    :param number: Número a truncar.
    :param decimals: Cantidad de decimales a conservar.
    :return: Número truncado.
    """
    factor = 10 ** decimals
    return int(number * factor) / factor

def uniform_distribution(num_samples, max_value, min_value):
    """
    Genera números aleatorios con distribución uniforme en el intervalo [min_value, max_value],
    guarda los números aleatorios RI en un archivo y los números transformados NI en otro.
    
    :param num_samples: Cantidad de números a generar.
    :param max_value: Valor máximo del intervalo.
    :param min_value: Valor mínimo del intervalo.
    """
    with open("ri_numbers.txt", "w") as file_ri, open("ni_numbers.txt", "w") as file_ni:
        for _ in range(num_samples):
            x = truncate(random.uniform(0, 1), 5)  # Genera un número RI truncado a 5 decimales
            ni_value = truncate(min_value + (max_value - min_value) * x, 5)  # Transforma RI a NI
            file_ri.write(f"{x}\n")
            file_ni.write(f"{ni_value}\n")

def generate_numbers():
    """
    Obtiene los valores ingresados por el usuario, verifica que sean válidos y genera los números.
    Muestra mensajes de error si los datos no son correctos y muestra un mensaje de éxito al finalizar.
    """
    try:
        num_samples = int(entry_samples.get())  # Obtiene la cantidad de números
        max_value = float(entry_max.get())  # Obtiene el valor máximo
        min_value = float(entry_min.get())  # Obtiene el valor mínimo
        
        if min_value >= max_value:
            messagebox.showerror("Error", "El valor mínimo debe ser menor que el máximo.")
            return
        
        uniform_distribution(num_samples, max_value, min_value)
        
        messagebox.showinfo("Éxito", "Archivos 'ri_numbers.txt' y 'ni_numbers.txt' generados exitosamente.")
        root.destroy()  # Cierra la ventana después de que el usuario acepte el mensaje
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Números Uniformes")
root.geometry("400x250")

# Etiquetas y entradas
tk.Label(root, text="Cantidad de números:").pack(pady=5)
entry_samples = tk.Entry(root)
entry_samples.pack(pady=5)

tk.Label(root, text="Valor máximo:").pack(pady=5)
entry_max = tk.Entry(root)
entry_max.pack(pady=5)

tk.Label(root, text="Valor mínimo:").pack(pady=5)
entry_min = tk.Entry(root)
entry_min.pack(pady=5)

# Botón para generar números
tk.Button(root, text="Generar", command=generate_numbers).pack(pady=20)

# Ejecutar la aplicación
root.mainloop()