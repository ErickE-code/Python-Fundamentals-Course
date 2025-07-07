import numpy as np
from matplotlib import pyplot as plt

# Función para simular la máquina de Galton
def simular_maquina_galton(n_canicas, niveles):
    # Crear un array para almacenar los resultados
    resultados = np.zeros(n_canicas, dtype=int)
    
    # Simular cada canica
    for i in range(n_canicas):
        # Cada canica pasa por todos los niveles
        for _ in range(niveles):
            # Decide si cae a la izquierda (0) o derecha (1)
            if np.random.random() < 0.5:
                resultados[i] += 1  # Suma 1 si va a la derecha
    return resultados

# Función para graficar el histograma
def graficar_histograma(resultados, niveles):
    # Crear el histograma
    plt.hist(resultados, bins=np.arange(-0.5, niveles + 1.5, 1), edgecolor='black', align='mid')
    plt.title("Simulación de la Máquina de Galton")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")
    plt.show()

# Parámetros de la simulación
n_canicas = 3000  # Número de canicas
niveles = 12      # Número de niveles de obstáculos

# Ejecutar la simulación
resultados = simular_maquina_galton(n_canicas, niveles)

# Graficar los resultados
graficar_histograma(resultados, niveles)
