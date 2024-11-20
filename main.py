def convertir_fila_en_uno(matriz, i=0):
    # si el primer elemento es 0
    if matriz[0][0] == 0:
        # intercambiar las filas si no tiene un 0 en la primera posicion
        if matriz[1][0] != 0:
            # intercambiar la fila 1 con fila 2 y convertirlo de nuevo
            matriz[0], matriz[1] = matriz[1], matriz[0]
            return convertir_fila_en_uno(matriz)
        # intercambiar las filas si no tiene un 0 en la primera posicion
        elif matriz[2][0] != 0:
            matriz[0], matriz[2] = matriz[2], matriz[0]
            return convertir_fila_en_uno(matriz)
        else:
            return "No hay solucion"

    nueva_fila = []
    primer_elemento = matriz[i][i]
    # agregar un elemento en el array multiplicado por el inverso del primer elemento
    for numero in matriz[i]:
        nueva_fila.append(numero*(1/primer_elemento))
    return nueva_fila

def restar_filas(matriz, indice_fila, elem=0):
    nueva_fila = []
    elemento_a_convertir = matriz[indice_fila][elem]
    
    # si el numero a convertir es 0, entonces no es necesario hacer la resta
    if elemento_a_convertir == 0:
        return matriz[indice_fila]
    else:
        # por cada numero de la fila, agregar al array ese numero - el elemento a convertir multiplicado por el numero arriba
        # F2: F2 - (F2*F1)
        for i, numero in enumerate(matriz[indice_fila]):
            nueva_fila.append(numero - (elemento_a_convertir*matriz[elem][i]))
        return nueva_fila

def calcular_ultima_fila(matriz):
    nueva_fila = []
    elemento_medio = matriz[1][1]

    # si el elemento del medio es 0:
    if elemento_medio == 0:
        # si el elemento de abajo es 0, entonces no cambiar nada
        if matriz[2][1] == 0:
            return matriz[1], matriz[2]
        # si es un numero no 0, intercambiar la segunda y ultima fila
        else:
            return matriz[2], matriz[1]
    # si el elemento del medio no es 0:
    else:
        # convertir la fila del medio en 0
        segunda_fila = convertir_fila_en_uno(matriz, 1)
        matriz[1] = segunda_fila
        # restar la fila del medio y la segunda para obtener el ultimo elemento
        ultima_fila = restar_filas(matriz, 2, 1)
        return segunda_fila, ultima_fila


def calcular_respuestas(matriz):
    # si alguno de los elementos de la diagonal es 0 entonces no hay solucion unica
    for i in range(3):
        if matriz[i][i] == 0:
            return "La matriz no tiene solucion unica."
    # calcular las incognitas en forma de ecuacion
    z = matriz[2][3]/matriz[2][2]
    y = (matriz[1][3]-(matriz[1][2]*z))/matriz[1][1]
    x = (matriz[0][3] - (matriz[0][2]*z) - (matriz[0][1]*y))/matriz[0][0]

    return f"x: {x}, y: {y}, z: {z}"
