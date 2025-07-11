matriz = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
]

suma = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        suma = suma + matriz[i][j]

print(suma)