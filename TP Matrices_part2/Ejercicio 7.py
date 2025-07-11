matriz = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
]

maxElemento = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maxElemento:
            maxElemento = matriz[i][j]
            fila = i
            columna = j

print(f"El mayor elemento esta en la fila ", fila, " y en la columna ",columna)