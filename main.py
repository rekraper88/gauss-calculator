print("Primera ecuacion: ")

x1 = (int)(input("Ingrese el coefieciente de x: "))
y1 = (int)(input("Ingrese el coefieciente de y: "))
z1 = (int)(input("Ingrese el coefieciente de z: "))
respuestas1 = (int)(input("Toda la ecuacion es igual a:"))

print("Segunda ecuacion: ")

x2 = (int)(input("Ingrese el coefieciente de x: "))
y2 = (int)(input("Ingrese el coefieciente de y: "))
z2 = (int)(input("Ingrese el coefieciente de z: "))
respuestas2 = (int)(input("Toda la ecuacion es igual a:"))

print("Tercera ecuacion: ")

x3 = (int)(input("Ingrese el coefieciente de x: "))
y3 = (int)(input("Ingrese el coefieciente de y: "))
z3 = (int)(input("Ingrese el coefieciente de z: "))
respuestas3 = (int)(input("Toda la ecuacion es igual a:"))

matriz = [
    [x1, y1, z1],
    [x2, y2, z2],
    [x3, y3, z3]
]

respuestas = [respuestas1, respuestas2, respuestas3]

def cambiar_respuesta(respuesta, numero_para_mult, referencia_cambio):
    resp = 0
    if respuesta > 0:
        resp = respuesta - (numero_para_mult*referencia_cambio)
    else:
        resp = respuesta + (numero_para_mult*referencia_cambio)
    return resp

# setear la primera fila
for i in range(len(matriz[0])):
    matriz[0][i] = matriz[0][i]*(1/x1)
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
# convertir el numero del medio en 1
for i in range(len(matriz[1])):
    matriz[1][i] = matriz[1][i]*(1/numero_medio)
respuestas[1] = respuestas[1]*(1/numero_medio)  

numero_a_cambiar = matriz[2][1]
for i in range(len(matriz[2])):
    if numero_a_cambiar > 0:
        matriz[2][i] = matriz[2][i] - (numero_a_cambiar*matriz[1][i])    
    else:
        matriz[2][i] = matriz[2][i] + (numero_a_cambiar*matriz[1][i])  
respuestas[2] = cambiar_respuesta(respuestas[2], numero_a_cambiar, respuestas[1])  

# for i, fila in enumerate(matriz):
#     print(fila, respuestas[i])

for fila in matriz:
    print(fila)
z = round(respuestas[2]/matriz[2][2], 1)
y = round((respuestas[1] - (matriz[1][2]*z))/matriz[1][1], 1)
x = round((respuestas[0] - (matriz[0][1]*y) - (matriz[0][2]*z))/matriz[0][0], 1)

print(x, y, z)