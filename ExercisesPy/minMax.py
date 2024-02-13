def min_Max(matrix):
    """
    Devuelve una matriz 2xn en la que la primera columna son
    los minimos de las filas, y la segunda columna el maximo
    de las columnas de la matriz original 
    """
    mM = []
    n = len(matrix)
    
    # iteramos por todo n
    for i in range(n):
        # maximo se inicializa como el primer elemento de la fila
        max = matrix[0][i]
        
        # minimo es el minimo de la fila        
        minim = min(matrix[i])
        
        # Se busca el maximo por la columna
        for pos in range(n):
            if matrix[pos][i] > max:
                max = matrix[pos][i]

        mM.append([minim,max])        
    return mM