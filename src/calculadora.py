def dividir(a, b):
    """
    Realiza la división de dos números reales.
    Lanza TypeError si los argumentos no son int o float.
    Lanza ValueError si el divisor es cero.
    """
    # El QA exigió esta validación para evitar comportamientos inesperados
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números enteros o decimales.")
    
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
        
    return a / b
