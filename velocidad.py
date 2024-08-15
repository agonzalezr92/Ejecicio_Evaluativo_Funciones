def calcular_promedio(velocidades):
    """
    Calcula el promedio de una lista de velocidades.
    
    Args:
    velocidades (list): Lista de velocidades de las correas.
    
    Returns:
    float: El promedio de las velocidades.
    """
    return sum(velocidades) / len(velocidades) if velocidades else 0

def posiciones_sobre_promedio(velocidades):
    """
    Determina las posiciones de las correas que están por encima del promedio.
    
    Args:
    velocidades (list): Lista de velocidades de las correas.
    
    Returns:
    list: Lista de índices de las correas que están sobre el promedio.
    """
    promedio = calcular_promedio(velocidades)
    posiciones = [i for i, velocidad in enumerate(velocidades) if velocidad > promedio]
    return posiciones

if __name__ == '__main__':
    velocidades = [25, 12, 19, 16, 11, 11, 24, 1,
                   14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
                   14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
                   14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
                   10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
                   11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
    
    # Obtener las posiciones de las correas sobre el promedio
    posiciones = posiciones_sobre_promedio(velocidades)
    
    # Imprimir las posiciones
    print(posiciones)
