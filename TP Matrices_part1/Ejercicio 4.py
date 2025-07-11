matriz = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
]

columna = int(input("Ingrese un numero: "))
numero = 0

for i in range(len(matriz)):
    if matriz[i][columna] > 0:
        numero = i

print(f"El numero mas grande esta en la fila  ", numero)