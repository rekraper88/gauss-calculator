def convertir_fila_en_uno(matriz, i=0):
    nueva_fila = []
    primer_elemento = matriz[i][i]

    for numero in matriz[i]:
        nueva_fila.append(numero*(1/primer_elemento))
    return nueva_fila

def restar_filas(matriz, indice_fila, elem=0):
    nueva_fila = []
    primer_elemento = matriz[indice_fila][elem]

    if primer_elemento == 0:
        return matriz[indice_fila]
    else:
        for i, numero in enumerate(matriz[indice_fila]):
            nueva_fila.append(numero - (primer_elemento*matriz[elem][i]))
        return nueva_fila

def calcular_segunda_fila(matriz):
    nueva_fila = []
    elemento_medio = matriz[1][1]

    if elemento_medio == 0:
        if matriz[2][1] == 0:
            return matriz[1], matriz[2]
        else:
            return matriz[2], matriz[1]
    else:
        nueva_fila = convertir_fila_en_uno(matriz, 1)
        return nueva_fila, matriz[2]


def calcular_respuestas(matriz):
    z = matriz[2][3]/matriz[2][2]
    y = (matriz[1][3]-(matriz[1][2]*z))/matriz[1][1]
    x = (matriz[0][3] - (matriz[0][2]*z) - (matriz[0][1]*y))/matriz[0][0]

    return f"x: {x}, y: {y}, z: {z}"
