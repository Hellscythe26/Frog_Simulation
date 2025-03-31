import matplotlib.pyplot as plt
import time

def simulate_jumps_2d(ri_file, target_x, target_y):
    """
    Simula los saltos de la rana en un espacio bidimensional.
    
    :param ri_file: Nombre del archivo que contiene los números aleatorios Ri.
    :param target_x: Coordenada X del objetivo.
    :param target_y: Coordenada Y del objetivo.
    :return: Listas con las posiciones en X e Y, posición final en X e Y, tiempo de ejecución y número de saltos.
    """
    x, y = 0, 0  # Posición inicial en el espacio 2D
    positions_x = [x]
    positions_y = [y]
    
    # Leer los números Ri desde el archivo
    with open(ri_file, "r") as file:
        ri_values = [float(line.strip()) for line in file.readlines()]
    
    # Iniciar temporizador
    start_time = time.time()
    
    threshold = 1 / 4  # Cuatro posibles direcciones
    
    # Realizar los saltos
    for i, step in enumerate(ri_values):
        if 0 < step <= threshold:  # Arriba
            y += 1
        elif threshold < step <= 2 * threshold:  # Abajo
            y -= 1
        elif 2 * threshold < step <= 3 * threshold:  # Derecha
            x += 1
        elif 3 * threshold < step <= 1:  # Izquierda
            x -= 1
        
        positions_x.append(x)
        positions_y.append(y)
        
        # Verificar si se alcanzó la posición objetivo
        if x == target_x and y == target_y:
            execution_time = time.time() - start_time
            return positions_x, positions_y, x, y, execution_time, i + 1
    
    # Si no se alcanzó el objetivo
    execution_time = time.time() - start_time
    return positions_x, positions_y, x, y, execution_time, len(ri_values)

def plot_movements_2d(positions_x, positions_y, final_x, final_y, execution_time, jumps, target_x, target_y):
    """
    Genera un gráfico de la trayectoria de la rana en el espacio 2D.
    
    :param positions_x: Lista con las posiciones en X de la rana.
    :param positions_y: Lista con las posiciones en Y de la rana.
    :param final_x: Posición final en X.
    :param final_y: Posición final en Y.
    :param execution_time: Tiempo de ejecución de la simulación.
    :param jumps: Número total de saltos realizados.
    :param target_x: Coordenada X del objetivo.
    :param target_y: Coordenada Y del objetivo.
    """
    plt.figure(figsize=(10, 8))
    plt.plot(positions_x, positions_y, linestyle='-', alpha=0.7)
    plt.scatter(0, 0, color='blue', label='Posición Inicial (0,0)', zorder=3)
    plt.scatter(final_x, final_y, color='red', label=f'Posición Final ({final_x},{final_y})', zorder=3)
    plt.scatter(target_x, target_y, color='green', label=f'Objetivo ({target_x},{target_y})', zorder=3)
    
    plt.xlabel("Posición en X")
    plt.ylabel("Posición en Y")
    plt.title(f"Trayectoria de la Rana en 2D (Tiempo: {execution_time:.2f} segs)")
    plt.legend()
    plt.show()
    
    print(f"Tiempo de ejecución: {execution_time:.2f} segundos")

# Parámetros de simulación
ri_file = "ri_numbers.txt"
target_x, target_y = 250, 300  # Coordenadas objetivo

# Ejecutar simulación
positions_x, positions_y, final_x, final_y, execution_time, jumps = simulate_jumps_2d(ri_file, target_x, target_y)

plot_movements_2d(positions_x, positions_y, final_x, final_y, execution_time, jumps, target_x, target_y)

print(f"Número de brincos realizados: {jumps}")
print(f"Tiempo de ejecución: {execution_time:.2f} segundos")