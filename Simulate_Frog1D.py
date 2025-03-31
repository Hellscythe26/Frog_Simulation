import matplotlib.pyplot as plt
import time

def simulate_jumps(ri_file, num_jumps):
    """
    Simula los saltos de la rana en un eje unidimensional.
    
    :param ri_file: Nombre del archivo que contiene los números aleatorios Ri.
    :param num_jumps: Cantidad de saltos que realizará la rana.
    :return: Lista con las posiciones de la rana en cada salto, posición final y tiempo de ejecución.
    """
    position = 0  # Posición inicial de la rana en el eje unidimensional
    jumps = []  # Lista para registrar la posición en cada salto
    
    # Leer los números Ri desde el archivo
    with open(ri_file, "r") as file:
        ri_values = [float(line.strip()) for line in file.readlines()]
    
    # Iniciar temporizador
    start_time = time.time()
    
    # Realizar los saltos
    for i in range(num_jumps):
        if ri_values[i] < 0.5:
            position -= 1  # Salto hacia atrás
        else:
            position += 1  # Salto hacia adelante
        jumps.append(position)
    
    # Calcular tiempo de ejecución
    execution_time = time.time() - start_time
    
    return jumps, position, execution_time

def plot_frequencies(jumps, final_position, execution_time):
    """
    Genera gráficos de la simulación de los saltos de la rana.
    
    :param jumps: Lista con las posiciones de la rana en cada salto.
    :param final_position: Posición final de la rana.
    :param execution_time: Tiempo de ejecución de la simulación.
    """
    plt.figure(figsize=(12, 5))
    
    # Histograma de frecuencias
    plt.subplot(1, 2, 1)
    plt.hist(jumps, bins=30, edgecolor='black', alpha=0.7)
    plt.axvline(0, color='blue', linestyle='dashed', linewidth=2, label='Posición Inicial: 0')
    plt.axvline(final_position, color='red', linestyle='dashed', linewidth=2, label=f'Posición Final: {final_position}')
    plt.xlabel("Posición Final")
    plt.ylabel("Frecuencia")
    plt.title(f"Frecuencia de las Posiciones Finales de la Rana\nTiempo de ejecución: {execution_time:.2f} segundos")
    plt.legend()
    
    # Gráfico de dispersión
    plt.subplot(1, 2, 2)
    plt.scatter(range(len(jumps)), jumps, s=0.1, alpha=0.5)
    plt.axhline(0, color='blue', linestyle='dashed', linewidth=2, label='Posición Inicial: 0')
    plt.axhline(final_position, color='red', linestyle='dashed', linewidth=2, label=f'Posición Final: {final_position}')
    plt.xlabel("Número de Salto")
    plt.ylabel("Posición")
    plt.title(f"Dispersión de las Posiciones de la Rana\nTiempo de ejecución: {execution_time:.2f} segundos")
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    print(f"Tiempo de ejecución: {execution_time:.2f} segundos")

# Parámetros de simulación
ri_file = "ri_numbers.txt"
num_jumps = 1000000  # 1 millón de saltos

# Ejecutar simulación
jumps, final_position, execution_time = simulate_jumps(ri_file, num_jumps)

plot_frequencies(jumps, final_position, execution_time)

print(f"La posición final de la rana después de {num_jumps} saltos es: {final_position}")
print(f"Tiempo de ejecución: {execution_time:.2f} segundos")