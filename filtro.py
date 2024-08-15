import sys

def filtrar_productos(precios, umbral, condicion='mayor'):
    """
    Filtra los productos según el precio y la condición especificada.
    
    Args:
    precios (dict): Un diccionario de productos y sus precios.
    umbral (float): El umbral de precio para el filtrado.
    condicion (str): La condición de filtrado ('mayor' o 'menor').
    
    Returns:
    dict: Un diccionario con los productos que cumplen la condición.
    """
    productos_filtrados = {}

    for producto, precio in precios.items():
        if condicion == 'mayor' and precio > umbral:
            productos_filtrados[producto] = precio
        elif condicion == 'menor' and precio < umbral:
            productos_filtrados[producto] = precio

    return productos_filtrados

if __name__ == '__main__':
    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }

    if len(sys.argv) < 2:
        print("Por favor, ingresa un umbral.")
        sys.exit(1)

    umbral = float(sys.argv[1])
    condicion = 'mayor'  # Valor por defecto

    if len(sys.argv) == 3:
        condicion = sys.argv[2].lower()

    if condicion not in ['mayor', 'menor']:
        print("Lo sentimos, no es una operación válida.")
        sys.exit(1)

    productos_filtrados = filtrar_productos(precios, umbral, condicion)

    if condicion == 'mayor':
        print(f"Los productos mayores al umbral son: {', '.join(productos_filtrados.keys())}.")
    elif condicion == 'menor':
        print(f"Los productos menores al umbral son: {', '.join(productos_filtrados.keys())}.")
