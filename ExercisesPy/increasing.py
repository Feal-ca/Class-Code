def is_increasing(n:int)-> bool:
    """
    Devuelve si un numero es creciente de izquierda a derecha o no
    """
    if n < 10:
        return True
    elif n%10<(n//10)%10:
        return False    
    return is_increasing(n//10)