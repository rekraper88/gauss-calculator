# x1 = (int)(input("Ingrese el coefieciente de x: "))
# y1 = (int)(input("Ingrese el coefieciente de y: "))
# z1 = (int)(input("Ingrese el coefieciente de z: "))
# respuesta1 = (int)(input("Toda la ecuacion es igual a: "))

# print("Segunda ecuacion: ")

# x2 = (int)(input("Ingrese el coefieciente de x: "))
# y2 = (int)(input("Ingrese el coefieciente de y: "))
# z2 = (int)(input("Ingrese el coefieciente de z: "))
# respuesta2 = (int)(input("Toda la ecuacion es igual a: "))

# print("Tercera ecuacion: ")

# x3 = (int)(input("Ingrese el coefieciente de x: "))
# y3 = (int)(input("Ingrese el coefieciente de y: "))
# z3 = (int)(input("Ingrese el coefieciente de z: "))
# respuesta3 = (int)(input("Toda la ecuacion es igual a: "))
#
#









print("Primera ecuacion: ")

x1 = 1
y1 = 1
z1 = 1
respuesta1 = 30

print("Segunda ecuacion: ")

x2 = 1
y2 = 1
z2 = -2
respuesta2 = 0

print("Tercera ecuacion: ")

x3 = 1
y3 = 3
z3 = -2
respuesta3 = 20

matriz = [
    [x1, y1, z1],
    [x2, y2, z2],
    [x3, y3, z3]
]

respuestas = [respuesta1, respuesta2, respuesta3]

def cambiar_respuesta(respuesta, numero_para_mult, referencia_cambio):
    resp = 0
    if respuesta > 0:
        resp = respuesta - (numero_para_mult*referencia_cambio)
    else:
        resp = respuesta + (numero_para_mult*referencia_cambio)
    return resp

def cambiar_fila_a_1(i, j, num):
    return matriz[i][j]*(1/num)

def check_if_matrix_done():
    if matriz[1][0] == 0 and matriz[2][0] == 0 and matriz[2][1] == 0:
        get_answers()

def get_answers():
    z = round(respuestas[2]/matriz[2][2], 1)
    y = round((respuestas[1] - (matriz[1][2]*z))/matriz[1][1], 1)
    x = round((respuestas[0] - (matriz[0][1]*y) - (matriz[0][2]*z))/matriz[0][0], 1)

    print(x, y, z)

# setear la primera fila
for i in range(len(matriz[0])):
    matriz[0][i] = cambiar_fila_a_1(0, i, x1)
respuestas[0] = respuestas[0]*(1/x1)

# segunda fila
for i in range(len(matriz[1])):
    if x2 > 0:
        matriz[1][i] = matriz[1][i] - (x2*matriz[0][i])
    else:
        matriz[1][i] = matriz[1][i] + (x2*matriz[0][i])
respuestas[1] = cambiar_respuesta(respuestas[1], x2, respuestas[0])

# tercera fila
for i in range(len(matriz[2])):
    if x3 > 0:
        matriz[2][i] = matriz[2][i] - (x3*matriz[0][i])
    else:
        matriz[2][i] = matriz[2][i] + (x3*matriz[0][i])
respuestas[2] = cambiar_respuesta(respuestas[2], x3, respuestas[0])



numero_medio = matriz[1][1]

if numero_medio == 0:
    fila_medio = matriz[1]
    ultima_fila = matriz[2]

    respuesta_medio = respuestas[1]
    ultima_respuesta = respuestas[2]

    matriz[1] = ultima_fila
    matriz[2] = fila_medio
    respuestas[1] = ultima_respuesta
    respuestas[2] = respuesta_medio



    print('\n\n')
    numero_medio = matriz[1][1]

check_if_matrix_done()
# convertir el numero del medio en 1
for i in range(len(matriz[1])):
    matriz[1][i] = cambiar_fila_a_1(1, i, numero_medio)
respuestas[1] = respuestas[1]*(1/numero_medio)

numero_a_cambiar = matriz[2][1]
for i in range(len(matriz[2])):
    if numero_a_cambiar > 0:
        matriz[2][i] = matriz[2][i] - (numero_a_cambiar*matriz[1][i])
    else:
        matriz[2][i] = matriz[2][i] + (numero_a_cambiar*matriz[1][i])
respuestas[2] = cambiar_respuesta(respuestas[2], numero_a_cambiar, respuestas[1])

for fila in matriz:
    print(fila)

get_answers()
