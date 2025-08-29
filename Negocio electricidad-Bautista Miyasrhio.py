def encontrarInventario(inventario, categoria, compra):
    encontrado = 0
    for i in range(len(inventario[categoria])):
        if inventario[categoria][i][0] == compra:
            encontrado = 1
            inventario[categoria][i][1] = inventario[categoria][i][1] - 1
            if inventario[categoria][i][1] == 0:
                print(f"Las {inventario[categoria][i][0]} se han acabado")
                inventario[categoria].pop(i)
            break
    if encontrado == 0:
        print("No se ha encontrado este producto")

inventario = {"consolas": [["nintendo", 10,],
                           ["xbox", 10],
                           ["play", 1]], 
              "componentes":[["RAM", 10],
                             ["CPU", 10],
                             ["GPU", 10]],
              "perifericos": [["auriculares", 10],
                              ["mouse", 10],
                              ["teclado", 10]]}

categoria = input("Ingrese lo que quiere comprar: "
               " -consolas"
               " -componentes"
               " -perifericos")

match categoria:
    case "consolas":
        print(inventario["consolas"])
        compra = input("Que desea comprar?")
        encontrarInventario(inventario, "consolas", compra)
    case "componentes":
        print(inventario["componentes"])
        compra = input("Que desea comprar?")
        encontrarInventario(inventario, "componentes", compra)
    case "perifericos":
        print(inventario["perifericos"])
        compra = input("Que desea comprar?")
        encontrarInventario(inventario, "perifericos", compra)
    case _:
        print("Categoria invalida")
