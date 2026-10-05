matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Inicialización de índices
i = 0  # Fila
while i < len(matriz):
    j = 0  # Columna
    while j < len(matriz[i]):
        print(matriz[i][j])
        j += 1
    i += 1   