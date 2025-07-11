matriz = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
]

positivos = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > 0:
            positivos = positivos + 1

print (positivos)