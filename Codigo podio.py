vecesJugadas = int(input("Ingrese la cantidad de veces jugadas: "))
nombreJugadores = []
puntaje = []
for j in range(vecesJugadas):
    for i in range(3):
        if i == 0:
            nombre = str(input("Ingrese el jugador que quedo primero: "))
            for i in range(nombreJugadores):
                if nombreJugadores[i] == nombre:
                    puntaje[i].append(puntaje[i]+3)
                else:
                    nombreJugadores.append(nombre)
        else:
            if i == 1:
                nombre = str(input("Ingrese el jugador que quedo segundo: "))
                for i in range(nombreJugadores):
                    if nombreJugadores[i] == nombre:
                        puntaje[i].append(puntaje[i]+2)
                    else:
                        nombreJugadores.append(nombre)
                else: 
                    if i == 2:
                        nombre = input("Ingrese el jugador que quedo tercero: ")
                        for i in range(nombreJugadores):
                            if nombreJugadores[i] == nombre:
                                puntaje[i].append(puntaje[i]+1)
                            else:
                                nombreJugadores.append(nombre)