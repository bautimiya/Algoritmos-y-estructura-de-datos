estudiantes = []

while True:
    print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedio general")
    print("4. Buscar estudiante por nombre")
    print("5. Mostrar estudiantes con nota mayor al promedio")
    print("6. Mostrar mejor y peor nota")
    print("7. Eliminar estudiante por nombre")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombre = input("Nombre del estudiante: ")
            try:
                edad = int(input("Edad: "))
                nota = float(input("Nota (0-10): "))
            except ValueError:
                print("Edad o nota inválidas. Intenta de nuevo.")
                continue

            if edad <= 0 or nota < 0 or nota > 10:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                nuevo_estudiante = {
                    "nombre": nombre,
                    "edad": edad,
                    "nota": nota
                }
                estudiantes.append(nuevo_estudiante)
                print(f"Estudiante {nombre} registrado con éxito.")

        case "2":
            if not estudiantes:
                print("No hay estudiantes registrados aún.")
            else:
                print("\nEstudiantes registrados:")
                print("-------------------------")
                for i, estudiante in enumerate(estudiantes, 1):
                    print(f"{i}. Nombre: {estudiante['nombre']}")
                    print(f"   Edad: {estudiante['edad']}")
                    print(f"   Nota: {estudiante['nota']}")
                    print("-------------------------")

        case "3":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                suma_notas = sum(e["nota"] for e in estudiantes)
                promedio = suma_notas / len(estudiantes)
                print(f"El promedio general de notas es: {promedio:.2f}")

        case "4":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                encontrado = 0
                nombre = input("Ingrese el nombre que desea buscar: ")
                for i in range(len(estudiantes)):
                    if nombre == estudiantes[i]["nombre"]:
                        print(estudiantes[i])
                        encontrado = 1

                if encontrado == 0:
                    print("No se a encontrado al estudiante")
        case "5":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                mayorAlPromedio = []
                mayorAlPromedio.clear
                suma_notas = sum(e["nota"] for e in estudiantes)
                promedio = suma_notas / len(estudiantes)
                for i in range(len(estudiantes)):
                    if estudiantes[i]["nota"] > promedio:
                        mayorAlPromedio.append(estudiantes[i])
                if not mayorAlPromedio:
                    print("No hay estudiantes con nota mayor al promedio")
        
        case "6":
                mayorNota = 0
                menorNota = 11
                alumnoMayorNota = []
                alumnoMenorNota = []
                if not estudiantes:
                    print("No hay estudiantes registrados.")
                else:
                    for i in range(len(estudiantes)):
                        if estudiantes[i]["nota"] > mayorNota:
                            mayorNota = estudiantes[i]["nota"]
                            alumnoMayorNota.clear
                            alumnoMayorNota.append(estudiantes)
                        elif estudiantes[i]["nota"] == mayorNota:
                            mayorNota = estudiantes[i]["nota"]
                            alumnoMayorNota.append(estudiantes)

                        if estudiantes[i]["nota"] < menorNota:
                            menorNota = estudiantes[i]["nota"]
                            alumnoMenorNota.clear
                            alumnoMenorNota.append(estudiantes)
                        elif estudiantes[i]["nota"] == menorNota:
                            menorNota = estudiantes[i]["nota"]
                            alumnoMenorNota.append(estudiantes)
                print(f"El alumno con mayor nota es {alumnoMayorNota}")
                print(f"El alumno con menor nota es {alumnoMenorNota}")                            
        case "7":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                encontrado = 0
                nombre = input("Ingrese el nombre del estudiante: ")

                for i in range(len(estudiantes)):
                    if nombre == estudiantes[i]:
                        estudiantes.remove(estudiantes[i])
                        enconrado = 1
                        print(f"El estudiante {nombre} fue eliminado con exito")
            
                if encontrado == 0:
                    print(f"El estudiante {nombre} no se a encontrado")
            
        case "8":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta otra vez.")
