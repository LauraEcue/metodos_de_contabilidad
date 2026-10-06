matriz = [
    [5, 4, 3],
    [2, 1, 0],
    [4, 5, 5],
    [3, 2, 2],
    [1, 1, 1]
]

i = 0                # Fila
while i < len(matriz):
    j = 0            # Columna
    while j < len(matriz[i]):
         #   print(matriz[i][j])
            j += 1
    i += 1
#print ("======================================================")

#inicialización de columnas y luego filas

matriz = [
    [5, 4, 3],
    [2, 1, 0],
    [4, 5, 5],
    [3, 2, 2],
    [1, 1, 1]
]

filas = len(matriz) #i
columnas = len(matriz[0]) #j

j = 0
while j < columnas:
    i = 0
    while i < filas:
        #print(matriz[i][j])
        i += 1
    j += 1    

#print("###################################################")

#inicializacion de filas y columnas, de final al inicio

matriz = [
    [5, 4, 3],
    [2, 1, 0],
    [4, 5, 5],
    [3, 2, 2],
    [1, 1, 1]
]
i = 4  # Fila
while i < len(matriz):
    j = 2  # Columna
    while j < len(matriz[i]):
            print(matriz[i][j])
            j += 1
    i += 1





#inicializacion - for

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#for fila in matriz:
  #  for elemento in fila:
       # print(elemento)   

