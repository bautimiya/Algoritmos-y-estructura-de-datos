dato = input("Ingrese el dato que quiere busacar en la matriz: ")
matriz = [
    ["101", "102", "103", "104","105"],
    ["Ana Garcia", "Luis Perez", "Sofia Diaz", "Juan Soto", "Maria Lopez"],
    ["2024-05-01","2024-05-01","24-05-01","2024-05-01","2024-05-01"],
    ["95","88","98","75","92"],
    ["120.5","155.0","115.3","180.2","135.7"]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == dato:
            posicion = i, j


print(f"La posicion del dato encontrado es ", posicion)