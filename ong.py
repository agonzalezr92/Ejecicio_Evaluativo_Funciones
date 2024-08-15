def calcular_factorial(n):
    """
    Calcula el factorial de un número entero n.
    
    Args:
    n (int): El número del que se desea calcular el factorial.
    
    Returns:
    int: El factorial de n.
    """
    if n < 0:
        return "El factorial no está definido para números negativos."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def calcular_productoria(lista):
    """
    Calcula la productoria de una lista de números.
    
    Args:
    lista (list): La lista de números para calcular la productoria.
    
    Returns:
    int: La productoria de los elementos de la lista.
    """
    productoria = 1
    for num in lista:
        productoria *= num
    return productoria

def calcular(**kwargs):
    """
    Controla los cálculos de factoriales y productorias, 
    e imprime los resultados.
    
    Args:
    kwargs: Argumentos con nombres que pueden ser fact_i (factorial) o prod_i (productoria).
    """
    for key, value in kwargs.items():
        if 'fact' in key:
            resultado = calcular_factorial(value)
            print(f"El factorial de {value} es {resultado}.")
        elif 'prod' in key:
            resultado = calcular_productoria(value)
            print(f"La productoria de {value} es {resultado}.")
        else:
            print(f"No se reconoció el argumento: {key}")

# Ejecución de la función calcular con diferentes combinaciones de argumentos
if __name__ == '__main__':
    calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
    calcular(prod_1=[4, 6, 7, 4, 3], fact_1=3)
    calcular(fact_2=4, prod_2=[1, 2, 3, 4, 5])
