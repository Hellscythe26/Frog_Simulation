import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D

def simulate_jumps_3d(file_ri, target_x, target_y, target_z):
    """
    Simula los movimientos aleatorios de una rana en un espacio tridimencional.
    
    Parámetros:
        file_ri (str): Ruta del archivo que contiene los números Ri.
        target_x (int): Coordenada X de la posición objetivo.
        target_y (int): Coordenada Y de la posición objetivo.
        target_z (int): Coordenada Z de la posición objetivo.
    
    Retorna:
        tuple: Listas con las posiciones en X, Y y Z, la posición final alcanzada, tiempo de ejecución y número de brincos realizados.
    """
    x, y, z = 0, 0, 0  # Posición inicial en el espacio 3D
    positions_x = [x]
    positions_y = [y]
    positions_z = [z]
    
    # Leer los números Ri desde el archivo
    with open(file_ri, "r") as file:
        ri_values = [float(line.strip()) for line in file.readlines()]
    
    # Iniciar temporizador
    start_time = time.time()
    
    threshold = 1 / 6  # Seis posibles direcciones
    
    # Realizar los saltos
    for i, step in enumerate(ri_values):
        if 0 < step <= threshold:  # Arriba
            y += 1
        elif threshold < step <= 2 * threshold:  # Abajo
            y -= 1
        elif 2 * threshold < step <= 3 * threshold:  # Derecha
            x += 1
        elif 3 * threshold < step <= 4 * threshold:  # Izquierda
            x -= 1
        elif 4 * threshold < step <= 5 * threshold:  # Adelante
            z += 1
        elif 5 * threshold < step <= 1:  # Atrás
            z -= 1
        
        positions_x.append(x)
        positions_y.append(y)
        positions_z.append(z)
        
        # Verificar si se alcanzó la posición objetivo
        if x == target_x and y == target_y and z == target_z:
            execution_time = time.time() - start_time
            return positions_x, positions_y, positions_z, x, y, z, execution_time, i + 1
    
    # Si no se alcanzó el objetivo
    execution_time = time.time() - start_time
    return positions_x, positions_y, positions_z, x, y, z, execution_time, len(ri_values)

def plot_3d_movements(positions_x, positions_y, positions_z, final_x, final_y, final_z, execution_time, jumps, target_x, target_y, target_z):
    """
    Grafica la trayectoria de la rana en un espacio 3D.
    
    Parámetros:
        positions_x (list): Lista con las posiciones en el eje X.
        positions_y (list): Lista con las posiciones en el eje Y.
        positions_z (list): Lista con las posiciones en el eje Z.
        final_x (int): Coordenada X de la posición final alcanzada.
        final_y (int): Coordenada Y de la posición final alcanzada.
        final_z (int): Coordenada Z de la posición final alcanzada.
        execution_time (float): Tiempo de ejecución de la simulación.
        jumps (int): Número total de brincos realizados.
        target_x (int): Coordenada X del objetivo.
        target_y (int): Coordenada Y del objetivo.
        target_z (int): Coordenada Z del objetivo.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(positions_x, positions_y, positions_z, linestyle='-', alpha=0.7)
    ax.scatter(0, 0, 0, color='blue', label='Posición Inicial (0,0,0)', zorder=3)
    ax.scatter(final_x, final_y, final_z, color='red', label=f'Posición Final ({final_x},{final_y},{final_z})', zorder=3)
    ax.scatter(target_x, target_y, target_z, color='green', label=f'Objetivo ({target_x},{target_y},{target_z})', zorder=3)
    
    ax.set_xlabel("Posición en X")
    ax.set_ylabel("Posición en Y")
    ax.set_zlabel("Posición en Z")
    ax.set_title(f"Trayectoria de la Rana en 3D (Tiempo: {execution_time:.2f} segs, Brincos: {jumps})")
    ax.legend()
    plt.show()
    
    print(f"Tiempo de ejecución: {execution_time:.2f} segundos")
    print(f"Número total de brincos: {jumps}")

# Parámetros de simulación
file_ri = "ri_numbers.txt"
target_x, target_y, target_z = 45, 23, 17  # Coordenadas objetivo

# Ejecutar simulación
positions_x, positions_y, positions_z, final_x, final_y, final_z, execution_time, jumps = simulate_jumps_3d(file_ri, target_x, target_y, target_z)

plot_3d_movements(positions_x, positions_y, positions_z, final_x, final_y, final_z, execution_time, jumps, target_x, target_y, target_z)

if final_x == target_x and final_y == target_y and final_z == target_z:
    print(f"La rana llegó a la posición ({target_x}, {target_y}, {target_z}) en {jumps} brincos.")
else:
    print(f"No fue posible alcanzar la posición ({target_x}, {target_y}, {target_z}) después de {jumps} brincos.")

print(f"Tiempo de ejecución: {execution_time:.2f} segundos")